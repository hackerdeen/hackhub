import hackhub
import time
from itertools import *
from datetime import date

class Member:
    
    schema = [
            'id',
            'username',
            'realname',
            'nickname',
            'email',
            'irc',
            'twitter',
            'github',
            'address',
            'key',
            'adm'
        ]
    
    def __init__(self, username):
        self.username = username
        if self.refresh_profile() == False:
            raise Exception("No such member")
                
    def refresh_profile(self):
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("select * from member where username=?", (
                    self.username,
                    ))
        profile = cur.fetchone()
        self.profile = {}
        if profile == None:
            return False
        for i in range(0, len(profile)):
            self.profile[Member.schema[i]] = profile[i]
        return True
        
    def get_profile(self):
        return self.profile
    
    def add_payment(self, month, year, admin=None):
        db = hackhub.get_db()
        cur = db.cursor()
        if admin == None:
            cur.execute("insert into payment (username, month, year) values (?, ?, ?)",
                        (self.username, month, year))
        else:
            cur.execute("insert into payment (username, month, year, recorded, admin) values (?, ?, ?, ?, ?)",
                        (self.username, month, year, int(time.time()), admin))
        db.commit()
        db.close()
        
    def get_payments(self):
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("select year, month, recorded, admin from payment where username=? order by year desc, month desc", (self.username,))
        return cur.fetchall()
    
    def is_active(self):
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("select * from dismembered where user=? and date_reset is null", (self.username,))
        if cur.fetchone() == None:
            return True
        return False
    
    def is_paid(self, delta=0):
        attrs = [self.username, int(time.strftime("%m")), int(time.strftime("%Y"))]
        attrs[1] += delta
        if attrs[1] <= 0:
            attrs[1] = 12 - attrs[1]
            attrs[2] -= 1
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("select * from payment where username=? and month=? and year=?", attrs)
        if cur.fetchone() == None:
            return False
        return True

    def payment_history(self, num_months=12):
        t = date.today()
        res = []
        payments = ["%4d/%02d"%(p[0], p[1]) for p in self.get_payments()]
        for m in xrange(1,num_months+1):
            month = (t.month-m)%12+1
            year = t.year+(t.month-m)/12
            month_str = "%4d/%02d"%(year, month)
            if month_str in payments:
                res.append((year, month, month_str, "paid"))
            elif len(payments) == 0 or month_str < payments[-1]:
                res.append((year, month, month_str, "prejoin"))
            elif m==1:
                res.append((year, month, month_str, "now")) 
            else:
                res.append((year, month, month_str, "gap"))
        return res
                
    def is_admin(self):
        return self.profile['adm']
    
    def is_keyholder(self):
        return self.profile['key']
    
    def update_profile(self, details):
        for key in details.keys():
            if key in Member.schema:
                db = hackhub.get_db()
                cur = db.cursor()
                cur.execute("update member set %s=? where username=?" % (key,),
                        (details[key], self.username))
                db.commit()
        self.refresh_profile()

    def get_email_prefs(self):
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("SELECT code, description, def FROM email_events")
        em_e = cur.fetchall()
        prefs = {}
        for ev in em_e:
            cur.execute("SELECT pref FROM email_prefs WHERE user = ? AND code = ?",
                        (self.username, ev[0]))
            p = cur.fetchall()
            if len(p) == 0:
                prefs[ev[0]] = ev[2]
            else:
                prefs[ev[0]] = p[0][0]
        return prefs

    def set_email_pref(self, code, pref):
        db = hackhub.get_db()
        cur = db.cursor()
        cur.execute("SELECT def FROM email_events WHERE code = ?", (code,))
        default = cur.fetchone()
        if not default:
            raise Exception("No event found with code %s", code)
        if pref == default[0]:
            cur.execute("DELETE FROM email_prefs WHERE user = ? and code = ?",
                        (self.username, code))
        else:
            cur.execute("SELECT * FROM email_prefs WHERE user = ? and code = ?",
                        (self.username, code))
            if cur.fetchone():
                cur.execute("UPDATE email_prefs SET pref = ? WHERE user = ? AND code = ?",
                            (pref, self.username, code))
            else:
                cur.execute("INSERT INTO email_prefs (user, code, pref) VALUES (?, ?, ?)",
                            (self.username, code, pref))
        db.commit()
    
                
def new_member(username, details):
    try:
        if Member(username).refresh_profile(): # Does the user exist?
            return False
    except Exception, e:
        if not "No such member" in str(e):
            raise e
    db = hackhub.get_db()
    cur = db.cursor()
    cur.execute("""insert into member (username, realname,
        nickname, email, address, key, adm) values (?, ?, ?, ?, ?, ?, ?)""",
        (username, details['realname'], details['nickname'], details['email'],
        details['address'], details['key'], details['adm']))
    db.commit()
    cur.close()
    try:
        m = Member(username)
    except Exception, e:
        if not "No such member" in str(e):
            raise e
    m.update_profile(details)
    
    return True

def undismember(username, reason):
    db = hackhub.get_db()
    cur = db.cursor()
    cur.execute("select * from dismembered where user=?", (username))
    if cur.fetchone() == None:
        raise ValueError("No such member to undismember")
    t = int(time.time())
    cur.execute("insert into dismembered (date_reset, reason_reset) values (?, ?) where user=?", (t, reason, username))
    db.commit()
    cur.close()

def all_member():
    db = hackhub.get_db()
    cur = db.cursor()
    cur.execute('select username from member')
    usernames = cur.fetchall()
    members = [Member(username[0]) for username in usernames]
    return members

def active_members():
    return [m.username for m in all_member() if m.is_active()]

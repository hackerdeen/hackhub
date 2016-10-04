import hackhub
from datetime import datetime
from monthdelta import monthdelta

class Payments:
    def __init__(self, month=None, year=None):
        if not month:
            month = datetime.utcnow().month
        if not year:
            year = datetime.utcnow().year
        self.month = month
        self.year = year
        self.refresh()

    def refresh(self):
        db = hackhub.get_db()
        curr = db.cursor()
        curr.execute("SELECT username FROM payment WHERE month = ? and year = ?",
                     (self.month, self.year))
        self.payments = curr.fetchall()

    def count(self):
        return len(self.payments)

def membership():
    month = datetime.utcnow()
    membership = []
    for i in xrange(36):
        membership.append((month.month,month.year,Payments(month.month, month.year).count()))
        month += monthdelta(-1)
    return [m for m in membership if not m[-1] == 0] 

def member_list():
    month = datetime.utcnow()
    members = {}
    curr = hackhub.get_db().cursor()
    for i in xrange(2):
        for user in Payments(month.month, month.year).payments:
            curr.execute("SELECT username, email FROM member WHERE username = ?", user)
            res = curr.fetchone()
            members[res[1]] = res[0]
        month += monthdelta(-1)
    return members

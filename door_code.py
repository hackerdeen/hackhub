from hackhub import get_db
import time, calendar
import random
import string

dict = "/usr/share/dict/british-english-small"

def word():
    with open(dict) as f:
        lines = f.readlines()
    w = random.choice(lines).strip().upper()
    w = w.replace("'S", "")
    return w

def now():
    return calendar.timegm(time.gmtime())

def new_code(username):
    code = " ".join([word(), word()])
    db = get_db()
    cur = db.cursor()
    cur.execute("""INSERT INTO door_codes (user, code, created) VALUES (?, ?, ?)""",
                (username, code, now()))
    db.commit()
    cur.close()
    return code

def active_codes():
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT code, created, user FROM door_codes WHERE used IS NULL""")
    return cur.fetchall()

def use_code(code):
    db = get_db()
    cur = db.cursor()
    cur.execute("""UPDATE door_codes SET used = ? WHERE code == ? """,
                (now(), code))
    db.commit()
    cur.close()

def add_url_code(username):
    code = ''.join([random.choice(string.ascii_lowercase+string.digits) for n in xrange(64)])
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT code, username FROM url_codes WHERE username = ?""", (username,))
    if cur.fetchall():
        cur.execute("""DELETE FROM url_codes WHERE username = ?""", (username,))
    cur.execute("INSERT INTO url_codes (code, username) VALUES (?, ?)""", (code, username))
    db.commit()
    cur.close()

def url_codes():
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT code, username FROM url_codes""")
    return cur.fetchall()

def user_url_code(username):
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT code FROM url_codes WHERE username = ?""", (username,))
    res = cur.fetchall()
    if res:
        return res[0][0]
    else:
        return ""

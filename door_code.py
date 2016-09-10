from hackhub import get_db
import time, calendar
import random

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
    

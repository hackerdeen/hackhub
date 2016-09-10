from hackhub import get_db
import time, calendar

def new_event(username, event_type, extra=''):
    db = get_db()
    cur = db.cursor()
    cur.execute("""INSERT INTO events (name, type, timestamp, extra) VALUES (?, ?, ?, ?)""",
                (username, event_type, calendar.timegm(time.gmtime()), extra))
    db.commit()
    cur.close()

def recent_events(num=10):
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT * FROM events ORDER BY timestamp DESC LIMIT ?""",
                (num,))
    return cur.fetchall()

import hackhub

class Status:
    
    def __init__(self, id=-1):
        
        db = hackhub.get_db()
        cur = db.cursor()
        
        if id == -1:
            cur.execute("select state, message, username, strftime('%s', thetime) from status order by thetime desc limit 1")
            status = cur.fetchone()
        else:
            cur.execute("select state, message, username, strftime('%s', thetime) where id=?", (id,))
            status = cur.fetchone()
            
        self.status = {'open': (status[0] == 1),
                       'message': status[1],
                       'trigger_person': status[2],
                       'lastchange': int(status[3])}
            
class StatusTable:
    
    def __init__(self, start = 0):
        
        db = hackhub.get_db()
        cur = db.cursor()
        
        cur.execute("select * from status order by thetime desc limit ?,10", (start,))
        
        self.status = cur.fetchall()


def new_status(state, message, username):
    db = hackhub.get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO status VALUES (null, ?, ?, ?, datetime('now'))",
                (state,
                message,
                username));
    db.commit()

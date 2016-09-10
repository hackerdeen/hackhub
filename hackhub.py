
from settings import *

import sqlite3

# Data storage helpers
def get_db():
    database = SQLITE_DB
    db = sqlite3.connect(database)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with open("schema.sql") as f:
        db = get_db()
        cur = db.cursor()
        cur.executescript(f.read())
        
# Web API

from flask import Flask
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.debug = True

from api_member import *
from api_status import *
from api_membership import *
from api_irc import *
from api_sms import *
from web import *
from admin import *

from filters import *

app.jinja_env.filters['ts2readable'] = ts2readable

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    

from hackhub import app, spaceapi
import pyme.core
import pyme.pygpgme
import time
from urllib import urlencode
import urllib2
from flask import json
from event import new_event

def unlock(user):
    message = json.dumps({'user':user,
                         'time': int(time.time())})
    plain = pyme.core.Data(message)
    plain.seek(0,0)
    signed = pyme.core.Data()
    ctx = pyme.core.Context()
    ctx.set_armor(1)
    ctx.op_keylist_start("hub@57north.co",0)
    key = ctx.op_keylist_next()
    ctx.op_sign(plain, signed, pyme.pygpgme.GPGME_SIG_MODE_CLEAR)
    signed.seek(0,0)
    signature = signed.read()
    form = {'command':str(signature)}
    data = urlencode(form)
    req = urllib2.Request("http://doorbot.57north.co/open", data)
    try:
        res = urllib2.urlopen(req)
        response = json.loads(res.read())
        resp_message = response['result']
        if 'exception' in response:
            resp_message += " " + response['exception']
        if response['result'] == "SUCCESS!":
            new_event(user, "door-unlock", "Unlocked the door")
            return True, resp_message
        else:
            new_event(user, 
                      "door-unlock-fail", 
                      "Failure trying to unlock the door " + resp_message)
            return False, resp_message
    except Exception as e:
        new_event(user, 
                  "door-unlock-fail", 
                  "Failure trying to unlock the door " + str(e))
        return False, str(e)


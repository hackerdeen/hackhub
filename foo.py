from flask import json 

import pyme.core
import pyme.pygpgme
import time

if __name__=="__main__":
    message = json.dumps({'user':'ormiret',
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
    signature =  signed.read()
    print type(signature)
    print signature

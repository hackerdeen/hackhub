from flask import request, jsonify, Response, json, session
from door_code import active_codes, use_code, now
from hackhub import app
from unlock import unlock
from member import Member

@app.route('/api/sms', methods=['POST'])
def recv_sms():
    message = request.form['Body'].upper()
    for code in active_codes():
        if code[0] in message:
            if Member(code[2]).is_active():
                success, resp = unlock(code[2])
                use_code(code[0])
                return Response(resp, content_type='text/plain')
            else:
                return Response("The owner of that code is not an active member.",
                                content_type='text/plain')
    else:
        return Response("Unknown code.", content_type='text/plain')





from flask import request, jsonify, Response, json
from hackhub import app
from member import Member

#@app.route("/api/auth", methods=['POST'])
#def webapi_auth():
#    try:
#        m = Member(request.json['username'])
#        return jsonify({'result': m.verify_password(request.json['password'])})
#    except (ValueError, KeyError, TypeError) as error:
#        print error
#        resp = jsonify({'err': 'JSON Format Error'})
#        resp.status = 400
#        return resp

#@app.route("/api/profile/<username>", methods=['POST'])
#def webapi_profile(username):
#    try:
#        if not Member(request.json['username']).verify_password(request.json['password']):
#            resp = jsonify('err', 'Unauthorised')
#            resp.status = 401
#            return resp
#        if username == request.json['username'] or Member(request.json['username']).is_admin(): 
#            m = Member(username)
#            return jsonify({'result', m.get_profile()})
#        else:
#            resp = jsonify('err', 'Forbidden')
#            resp.status = 403
#            return resp
#    except (ValueError, KeyError, TypeError) as error:
#            print error
#            resp = jsonify({'err', 'JSON Format Error'})
#            resp.status = 400
#            return resp

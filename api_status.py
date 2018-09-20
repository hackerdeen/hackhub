from flask import request, jsonify, Response, json, redirect, abort
import hackhub
from hackhub import app
from status import Status, StatusTable, new_status
from member import Member
import urllib
import random

@app.route("/api/statuses", methods=['GET'])
def webapi_statuses_home():
    return redirect('/api/statuses/0')

@app.route('/api/statuses/<start>', methods=['GET'])
def webapi_statuses_block(start):
    return jsonify({'result': StatusTable(start).status})

@app.route("/api/status")
def webapi_status_home():
    return redirect('/api/status/current')

@app.route("/api/status/<theid>", methods=['GET'])
def webapi_status(theid):
    if theid == "current":
        theid = -1
    return jsonify({'result': Status(theid).status})

#@app.route("/api/status/update", methods=['POST'])
#def webapi_status_update():
#    try:
#        if not Member(request.json['username']).verify_password(request.json['password']):
#            abort(403)
#        if request.json['state'] == 1 or request.json['state'] == 0:
#            new_status(request.json['state'], request.json['message'], request.json['username'])
#        else:
#            abort(400)
#    except (ValueError, KeyError, TypeError) as error:
#        abort(400)

@app.route("/api/testing/")
def api_testing():
    return redirect("/")

@app.route("/api/wisdom")
def api_wisdom():
    url = "http://idea.bodaegl.com/cah.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return jsonify(data)

def close_space(who):
    msg = random.choice(hackhub.close_msgs)
    hackhub.new_status(0, msg, who)
    return jsonify({"msg": "Opened: "+msg})

def open_space(who):
    msg = random.choice(hackhub.open_msgs)
    hackhub.new_status(0, msg, who)
    return jsonify({"msg": "Opened: "+msg})

@app.route("/api/status/<secret>/<action>")
def change_status(secret, action):
    secret = secret.lower()
    if not secret in hackhub.status_api_secrets:
        abort(404)
    who = hackhub.status_api_secrets[secret]
    current = hackhub.Status()
    action = action.lower()
    if action == "open":
        if current.status["open"]:
            return jsonify({"msg": "Already open"})
        else:
            return open_space(who)
    else if action == "close":
        if current.status["open"]:
            return close_space(who)
        else:
            return jsonify({"msg": "Already closed"})
    else if action =="toggle":
        if current.status["open"]:
            return close_space(who)
        else:
            return open_space(who)
    else:
        return abort(404)

from flask import request, jsonify, Response, json, redirect, abort
from hackhub import app
from status import Status, StatusTable, new_status
from member import Member
import urllib

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

from flask import request, jsonify, Response, json, session
from hackhub import app
from member import Member, active_members

def irc_nicks():
    members = [Member(m) for m in active_members()]
    irc_nicks = []
    for m in members:
        irc_nicks.append(m.username)
        if m.profile["irc"] and len(m.profile["irc"]) > 0:
            irc_nicks.append(m.profile["irc"])
    return list(set(irc_nicks))

@app.route("/api/irc/nicks")
def nicks():
    return jsonify({'nicks': irc_nicks()})

from flask import request, jsonify
from hackhub import app
import settings
#

@app.route("/api/membership", methods=['GET'])
def api_membership():
    from payments import membership
    return jsonify({'columns':('month','year','num_members'),
                    'membership':membership()})

@app.route("/api/membership/graph", methods=['GET'])
def api_membership_graph():
    from payments import membership
    import matplotlib
    import numpy as np
    # matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    from cStringIO import StringIO

    page='''
<html>
<body>
<img src="data:image/png;base64,{}"/>
</body>
</html>
'''
    plt.xkcd() 
    fig = plt.figure()
    members = membership()
    members.reverse()
    counts = [x[2] for x in members]
    dates = [str(x[1])[-2:]+"/"+str(x[0]) for x in members]
    ax = plt.subplot(111)
    ax.bar(range(len(dates)),counts,width=1)
    ax.set_xticks(np.arange(len(dates))+.5)
    ax.set_xticklabels(dates, rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Members')
    plt.subplots_adjust(bottom=0.15)
    io = StringIO()
    fig.savefig(io, format='png')
    data = io.getvalue().encode('base64')

    return page.format(data)
     
@app.route(settings.EMAIL_LIST_PATH, methods=['GET'])
def members_list():
    from payments import member_list
    page = ''
    for email, name in member_list().items():
        line = name + " " + email + "\n"
        page += line
    return page

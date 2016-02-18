from setsuna import app
from flask import json
from pymongo import MongoClient 

@app.route('/api/1/', methods='GET')
def do_api():
    db = setsua.DATABASE
    news = db.posts.find().sort({unique_id: -1}).limit(int(count))
    posts = []
    for post in news:
        posts.add(setsuna.Content(post))

    js = json.dumps(posts)

    response = Response(js, status=200, minetype='application/json')
    response = headers['Link'] = 'http://setsuna.org'

    return response

@app.route('/api/1/

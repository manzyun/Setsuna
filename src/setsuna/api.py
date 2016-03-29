import json
from datetime import datetime
from . import app, models, conf
from pymongo import MongoClient
from flask import abort, jsonify, Request, request, Response

from bson import objectid
import random

client = MongoClient()
ISODatetime = '%Y-%M-%DTHH:mmZ'


@app.errorhandler(400)
def bad_request(error):
    return Response("{error': 'Bad Request', 'message': 'Sorry, I can not get request.", 400)


@app.errorhandler(404)
def not_found(error):
    return Response("{'error': 'Not Found', 'message': 'This post was deleted maybe.'}", 404)


@app.errorhandler(500)
def internal_error(error):
    return Response("{'error': 'Internal Server Error', 'message': 'Sorry, Internal server error...}", 500)


def know_post(unique_id):
    if conf.posts.find({'_id': objectid.ObjectId(unique_id)}).count() > 0:
        return True
    else:
        abort(404)
        return False


@app.route('/api/v1.0')
def index():
    return jsonify({'title': 'Setsuna API', 'version': 'version 1.0'})


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    news = []
    bson_news = conf.posts.find().sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/posts?limit=<int:limit>', methods=['GET'])
def get_posts(limit):
    news = []
    bson_news = conf.posts.find().limit(limit).sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/<lang>/posts', methods=['GET'])
def get_posts(lang):
    news = []
    bson_news = conf.posts.find({'lang': lang}).sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/posts?start=<date_time_s>&end=<date_time_e>', methods=['GET'])
def get_posts_ontime(date_time_s, date_time_e):
    news = []
    bson_news = conf.posts.find({'timestanp':
                                {'$gte': datetime.strptime(date_time_s, ISODatetime),
                                 '$lte:': datetime.strptime(date_time_e, ISODatetime)}
                                 }).sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/<lang>/posts?start=<date_time_s>&end=<date_time_e>', methods=['GET'])
def get_posts_ontime(lang, date_time_s, date_time_e):
    news = []
    bson_news = conf.posts.find({{'lang': lang},
                                 {'timestanp':
                                 {'$gte': datetime.strptime(date_time_s, ISODatetime),
                                  '$lte:': datetime.strptime(date_time_e, ISODatetime)}
                                  }
                                 }).sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/post/<unique_id>', methods=['GET'])
def get_post(unique_id):
    print(unique_id)
    if know_post(unique_id):
        post = conf.posts.find_one({'_id': objectid.ObjectId(unique_id)})
        post["_id"] = str(post['_id'])
        return json.dumps(post)


@app.route('/api/v1.0/tell/<unique_id>', methods=['POST'])
def tell_post(unique_id):
    if know_post(unique_id):
        post = models.Post(unique_id=unique_id)
        post.tell()

        res = conf.posts.find_one({'_id': objectid.ObjectId(unique_id)})
        res['_id'] = str(res['_id'])
        return json.dumps(res)


@app.route('/api/v1.0/post/<unique_id>', methods=['DELETE'])
def delete_post(unique_id):
    if know_post(unique_id):
        if not Request.get_json(request):
            req = request.get_json(request)
            post = models.Post(unique_id=unique_id)
            if not 'delkey' in req:
                abort(400)

            if post.delete(request.json['delkey']):
                return json.dumps({'result': True})
            else:
                return json.dumps({'result': False, 'message': 'Not matching password.'})


@app.route('/api/v1.0/post', methods=['POST'])
def post_content():
    if not Request.get_json(request):
        abort(400)

    req = Request.get_json(request)
    if not 'content' in req:
        abort(400)

    post = models.Post()
    post.content = req['content']
    post.delkey = req['delkey'] if 'delkey' in req else make_delkey()
    result = post.post()

    # Create response data.
    res = conf.posts.find_one({'_id': result})
    res['_id'] = str(res['_id'])
    return json.dumps(res)


def make_delkey(length=6):
    # Make font map
    alphabets = []
    codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
    for r in codes:
        chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
        alphabets.extend(chars)

        password = [random.choice(alphabets) for _ in range(length)]
        delkey = ''.join(password)

        return delkey


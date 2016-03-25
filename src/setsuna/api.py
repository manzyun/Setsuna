from setsuna import app, models, conf
from pymongo import MongoClient
from flask import abort, jsonify, request, Response
import json
from bson import objectid

client = MongoClient()


@app.errorhandler(404)
def not_found(error):
    return Response("{'error': 'Not Found', 'message': 'This post was deleted maybe.'}", 404)


@app.errorhandler(500)
def internal_error(error):
    return Response("['error': 'Internal Server Error', 'message': 'Sorry Internal server error...}", 500)


def know_post(unique_id):
    if conf.posts.find({'_id': objectid.ObjectId(unique_id)}).count() > 0:
        return True
    else:
        abort(404)
        return False


@app.route('/api/v1.0/')
def index():
    print('hello')
    return jsonify({'title': 'Setsuna API version 1.0'})


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    news = []
    bson_news = conf.posts.find().limit(10)
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/post/<unique_id>', methods=['GET'])
def get_post(unique_id):
    if know_post(unique_id):
        post = conf.posts.find_one({'_id': objectid.ObjectId(unique_id)})
        post["_id"] = str(post['_id'])
        return json.dumps(post)


@app.route('/api/v1.0/tell/<unique_id>', methods=['POST'])
def tell_post(unique_id):
    if know_post(unique_id):
        post = models.Post(unique_id=unique_id)
        return json.dumps(conf.posts.find({'_id': post.tell()}))


@app.route('/api/v1.0/post/<unique_id>', methods=['DELETE'])
def delete_post(unique_id):
    if know_post(unique_id):
        post = models.Post(unique_id=unique_id)
        if not request.json or not 'delkey' in request.json:
            abort(400)

        if post.delete(request.json['delkey']):
            return jsonify({'result': True})
        else:
            return jsonify({'result': False, 'message': 'Not matching password.'})


@app.route('/api/v1.0/post/', methods=['POST'])
def post_content():
    if not request.json or not 'content' in request.json:
        abort(400)

    post = models.Post()
    post.content = request.json['content']
    post.delkey = request.json['delkey'] if 'delkey' in request.json else ''
    result = post.post()
    return json.dumps(conf.posts.find({'_id': result}))


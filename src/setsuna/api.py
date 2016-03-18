from setsuna import app, models, conf
from pymongo import MongoClient
from flask import abort, jsonify, request, make_response

client = MongoClient()


@app.errorhandler(404)
def not_found(error):
    return make_response({'error': 'Not Found', 'message': 'This post was deleted maybe.'}, 404)


def know_post(unique_id):
    if unique_id in conf.posts.find({'unique_id': unique_id}):
        return True
    else:
        abort(404)
        return False


@app.route('/api/v1.0/')
def index():
    return jsonify({'title': 'Setsuna API version 1.0'})


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    news = conf.posts.find().limit(10)
    print(news)
    return jsonify(news)


@app.route('/api/v1.0/post/<unique_id>', methods=['GET'])
def get_post(unique_id):
    if know_post(unique_id):
        post = conf.posts.find({'unique_id': unique_id})
        return jsonify(post)


@app.route('/api/v1.0/tell/<unique_id>', methods=['POST'])
def tell_post(unique_id):
    if know_post(unique_id):
        post = models.Post(unique_id=unique_id)
        return jsonify(conf.posts.find({'unique_id': post.tell()}))


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
    return jsonify(conf.posts.find({'unique_id': result}))


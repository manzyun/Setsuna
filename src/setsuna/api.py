import typing

from datetime import datetime
from . import app, models
from pymongo import MongoClient
from flask import abort, jsonify, Request, request, Response

from bson import objectid
import random




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


@app.route('/', methods=['GET'])
def index():
    re_text = ''
    with open('./readme.rst', encoding='utf-8') as readme:
         re_text = readme.read()
    return re_text

def make_template(json_id=1) -> str:
    data = {
    'links': {
#            'self':  # Make from address and id
            'res_to':''
        },
        data: {
        'type': 'post',
        'id': json_id,
        }
    }
    return data


@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = models.Posts()
    posts.get_now_posts

    return json.dumps(posts)


@app.route('/api/posts/limit/<int:limit>', methods=['GET'])
def get_posts_limit(limit: int):
    posts = models.Posts()
    posts.get_posts_save(limit)

    return json.dumps(news)


@app.route('/api/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_ontime(datetime_s: str, datetime_e: str):
    posts = models.Posts()
    posts.get_posts_between(datetime_s, datetime_e)

    return json.dumps(posts)


@app.route('/api/<lang>/posts', methods=['GET'])
def get_posts_lang(lang: str):
    posts = models.Posts()
    posts.get_lang_posts(lang)

    return json.dumps(posts)


@app.route('/api/<lang>/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_lang_ontime(lang: str, datetime_s: str, datetime_e: str):
    posts = models.Posts()
    posts.get_lang_posts_between

    return json.dumps(posts)


@app.route('/api/post/<uid>', methods=['GET'])
def get_post(uid: str):
    post = models.Post()
    post.getPost(uid)

    return json.dumps(post)




@app.route('/api/', methods=['POST'])
@app.route('/api/post/', methods=['POST'])
def post_content():
    if not Request.get_json(request):
        abort(400)

    req = Request.get_json(request)
    if not 'content' in req:
        abort(400)

    post = models.Post(content=req['content'], password=req['password'] if '' None, lang=req['rang'] if '' None)
    post.post_content()
    
    return json.dumps(post)

@app.route('/api/post/<uid>', methods=['POST'])
def res_post(uid: str):
    if know_post(uid):
        if not Request.get_json(request):
            abort(400)
            
        post = models.ResponsePost(link=uid, content=req['content'], password=req['password'] if '' None, lang=req['rang'] if '' None)
        post.post_contribution()

        return json.dumps(post)


@app.route('/api/post/<uid>', methods=['DELETE'])
def delete_post(uid):
    if know_post(uid):
        if not Request.get_json(request):
            
                
            if not 'password' in req:
                abort(400)

        req = request.get_json(request)
        post = models.PostFactory(uid)
        if post.password_checker(req['password']):
            post.delete_post()
        else:
            return json.dumps({})

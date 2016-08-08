import json
from .. import app
from .. models import post_factory, post, response_post, posts
from flask import abort, Request, request, Response


_err_dict = {'errors':[]}


@app.errorhandler(400)
def bad_request(error):
    err_obj = _err_dict['errors'].append({'status':'400',
                                'title': 'Bad Request',
                                'detail': 'Sorry, I can not get request.'})
    return Response(json.dumps(err_obj), 400)


@app.errorhandler(401)
def password_not_match():
    err_obj = _err_dict['errors'].append({'status':'401',
                                'title': 'Passwords do not match',
                                'detail': 'Are you really this contribution post ?'})
    return Response(json.dumps(err_obj), 226)


@app.errorhandler(404)
def not_found(error):
    err_obj = _err_dict['errors'].append({'status':'400',
                            'title': 'Not Found',
                            'detail': 'Your request page is not found.'})
    return Response(json.dumps(err_obj), 404)


@app.errorhandler(410)
def not_found(error):
    err_obj = _err_dict['errors'].append({'status':'410',
                            'title': 'Gone',
                            'detail': 'This post was deleted maybe.'})
    return Response(json.dumps(err_obj), 404)


@app.errorhandler(500)
def internal_error(error):
    err_obj = _err_dict['errors'].append({'status':'500',
                            'title': 'Internal Server Error',
                            'detail': 'Sorry, Internal server error...'})
    return Response(json.dumps(err_obj), 500)


def know_post(uid):
    is_post = post_factory(uid)
    if is_post is not None:
        return True
    else:
        return False


@app.route('/', methods=['GET'])
def index():
    with open('setsuna/readme.rst', encoding='utf-8') as readme:
         re_text = readme.read()
    return re_text


@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Posts()
    posts.get_now_posts

    return Response(json.dumps(posts), 200)


@app.route('/api/posts/limit/<int:limit>', methods=['GET'])
def get_posts_limit(limit: int):
    posts = Posts()
    posts.get_posts_save(limit)

    return Response(json.dumps(posts), 200)


@app.route('/api/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_ontime(datetime_s: str, datetime_e: str):
    posts = Posts()
    posts.get_posts_between(datetime_s, datetime_e)

    return Response(json.dumps(posts), 200)


@app.route('/api/<lang>/posts', methods=['GET'])
def get_posts_lang(lang: str):
    posts = Posts()
    posts.get_lang_posts(lang)

    return Response(json.dumps(posts), 200)


@app.route('/api/<lang>/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_lang_ontime(lang: str, datetime_s: str, datetime_e: str):
    posts = Posts()
    posts.get_lang_posts_between

    return Response(json.dumps(posts), 200)


@app.route('/api/post/<uid>', methods=['GET'])
def get_post(uid: str):
    post = Post()
    post.getPost(uid)

    return Response(json.dumps(post), 200)


@app.route('/api/', methods=['POST'])
@app.route('/api/post/', methods=['POST'])
def post_content():
    if not Request.get_json(request):
        abort(400)

    req = Request.get_json(request)
    if not 'content' in req:
        abort(400)

    if len(req['content']) <= 0:
        abort(123)

    post = Post(content=req['content'],
                password=None if '' else req['password'],
                lang=None if '' else req['lang'])
    post.post_content()
    
    return Response(json.dumps(post), 200)

@app.route('/api/post/<uid>', methods=['POST'])
def res_post(uid: str):
    if know_post(uid):
        if not Request.get_json(request):
            abort(400)

        req = Request.get_json(request)
        post = ResponsePost(link=uid, content=req['content'],
                            password=None if '' else req['password'] ,
                            lang=None if '' else req['rang'])
        post.post_contribution()

        return Response(json.dumps(post), 200)


@app.route('/api/post/<uid>', methods=['DELETE'])
def delete_post(uid):
    if know_post(uid):
        if not Request.get_json(request):
            req = Request.get_Json(request)
            if not 'password' in req:
                abort(400)

        req = Request.get_json(request)
        post = post_factory(uid)
        if not post.password_checker(req['password']):
            abort(123)
        else:
            post.delete_post()
            return Response(json.dumps({'message': 'Your post deleted ;)'}), 200)

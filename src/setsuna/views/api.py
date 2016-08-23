import json
from datetime import datetime
from .. import app
from .. models import post_factory, post, response_post, posts
from flask import abort, Request, request, Response


_err_dict = {'errors':[]}
_DATE_FORMAT = '%Y%m%dT%H%M%S%z'

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
    is_post = post_factory.post_factory(uid)
    if is_post is not None:
        return True
    else:
        return False


@app.route('/api/', methods=['GET'])
def index():
    with open('setsuna/readme.rst', encoding='utf-8') as readme:
         re_text = readme.read()
    return re_text


@app.route('/api/posts', methods=['GET'])
def get_posts():
    tmp_posts = posts.Posts()
    tmp_posts.get_now_posts()

    return Response(json.dumps(tmp_posts), 200)


@app.route('/api/posts/save/<int:limit>', methods=['GET'])
def get_posts_limit(limit: int):
    tmp_posts = posts.Posts()
    tmp_posts.get_posts_save(limit)

    return Response(json.dumps(tmp_posts), 200)


@app.route('/api/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_ontime(datetime_s: str, datetime_e: str):
    tmp_posts = posts.Posts()
    tmp_posts.get_posts_between(datetime.strptime(datetime_s, _DATE_FORMAT), datetime.strptime(datetime_e, _DATE_FORMAT))

    return Response(json.dumps(tmp_posts), 200)


@app.route('/api/<lang>/posts', methods=['GET'])
def get_posts_lang(lang: str):
    tmp_posts = posts.Posts()
    tmp_posts.get_lang_posts(lang)

    return Response(json.dumps(tmp_posts), 200)


@app.route('/api/<lang>/posts/save/<int:limit>', methods=['GET'])
def get_posts_lang_limit(lang:str, limit: int):
    tmp_posts = posts.Posts()
    tmp_posts.get_lang_posts_save(lang, limit)

    return Response(json.dumps(tmp_posts), 200)


@app.route('/api/<lang>/posts/start/<datetime_s>/end/<datetime_e>', methods=['GET'])
def get_posts_lang_ontime(lang: str, datetime_s: str, datetime_e: str):
    tmp_posts = posts.Posts()
    tmp_posts.get_lang_posts_between

    return Response(json.dumps(vars(tmp_posts)), 200)


@app.route('/api/post/<uid>', methods=['GET'])
def get_post(uid: str):
    tmp_post = post_factory.post_factory(uid)

    return Response(json.dumps(vars(tmp_post)), 200)


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

    tmp_post = post.Post(content=req['content'],
                password=req['password'] if 'password' in Request.get_json(request) else '',
                lang=req['lang'] if 'lang' in Request.get_json(request) else 'und')
    tmp_post.post_contribution()

    return Response(json.dumps(vars(tmp_post)), 200)

@app.route('/api/post/<uid>', methods=['POST'])
def res_post(uid: str):
    if know_post(uid):
        if not Request.get_json(request):
            apo_post = post_factory.post_factory(uid)
            apo_post.apothanasia()
            return Response(json.dumps(vars(apo_post)), 200)

        req = Request.get_json(request)
        tmp_post = response_post.ResponsePost(link=uid, content=req['content'],
                            password=req['password'] if 'password' in Request.get_json(request) else '',
                            lang=req['lang'] if 'lang' in Request.get_json(request) else 'und')
        tmp_post.post_contribution()

        return Response(json.dumps(vars(tmp_post)), 200)


@app.route('/api/post/<uid>', methods=['DELETE'])
def delete_post(uid):
    if know_post(uid):
        if not Request.get_json(request):
            req = Request.get_Json(request)
            if not 'password' in req:
                abort(400)

        req = Request.get_json(request)
        tmp_post = post_factory.post_factory(uid)
        if not tmp_post.password == req['password']:
            abort(401)
        else:
            tmp_post.delete_post()
            return Response(json.dumps({'message': 'Your post deleted ;)'}), 200)

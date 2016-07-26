import json
from datetime import datetime
from . import app, models, conf
from pymongo import MongoClient
from flask import abort, jsonify, Request, request, Response

from bson import objectid
import random

client = MongoClient()
ISODatetime = '%Y-%M-%dT%H:%M%z'


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
    return '''
====================
Setsuna Web API
====================

author
-------------

Hidetsugu Takahashi a.k.a manzyun <manzyun@gmail.com>


What's this?
---------------------

This is Micro SNS. Your post will delete 6 hour.

But, your post is gotten response of 1 hour plus every,


How to use
--------------

Contribution
~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password.
    "lang": Language code by ISO 639-2.
  }

.. note:: If "password" is nothing then make random 4 digit password.

2. Contribute this address your JSON on POST method.
3. 'Comming server response your contribut infomartion in "data" section::

  {
    "id": Your contribution id,
    "content": You contribute content,
    "password": Delete contribution password,
    "lang": Language code by ISO 639-2.
  }


Response(no_comment)
~~~~~~~~~~~~~~~~~~~~~~~

1. Access contribution on POST method.
2. Comming server response your responsed contribution information in "data" section::

  {
    "id": Your responsed contribution id,
    "content": Your responsed contribution
  }


Response(comment)
~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password,
    "lang": Language code by ISO 639-2.
  }

.. note:: If "password" is nothing then make random 4 digit password.


2. Contribute you want response contribution address on POST method
3. Comming server response your contribution information in "data" section::

  {
    "id": Your contribution id,
    "content": You contribute content,
    "password": Delete contribution password,
    "lang": Language code by ISO 639-2.
  }


Delete Contribution
~~~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "password": your contribution has delete password.
  }


2. Contribute this address your JSON on DELETE method.
3. 'Comming server response your contribute infomartion in "data" section::

  {
    "message": "Your post deleted ;)"
  }


.. note:: If contribution has response then delete with responsed contribution.

FAQ
-----

Where web page?
  Nothing special. Because, I want make a service and I am poor sense web design. Because so only Web and JSON API',

Am I not user requiring?
  Yes. This service is anonymity. And I can not manage a server that is managing the large amount of user information.'
'''


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

@app.route('/posts', methods=['GET'])
def get_posts():
    news = []
    bson_news = conf.posts.find().sort({'Timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/api/v1.0/posts?limit=<int:limit>', methods=['GET'])
def get_posts_limit(limit):
    news = []
    bson_news = conf.posts.find().limit(limit).sort({'timestamp': 1})
    for b_new in bson_news:
        if isinstance(b_new, dict):
            b_new['_id'] = str(b_new['_id'])

        news.append(b_new)

    return json.dumps(news)


@app.route('/<lang>/posts', methods=['GET'])
def get_posts_lang(lang):
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


@app.route('/<lang>/posts?start=<date_time_s>&end=<date_time_e>', methods=['GET'])
def get_posts_lang_ontime(lang, date_time_s, date_time_e):
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


@app.route('/post/<unique_id>', methods=['GET'])
def get_post(unique_id):
    print(unique_id)
    if know_post(unique_id):
        post = conf.posts.find_one({'_id': objectid.ObjectId(unique_id)})
        post["_id"] = str(post['_id'])
        return json.dumps(post)


@app.route('/tell/<unique_id>', methods=['POST'])
def tell_post(unique_id):
    if know_post(unique_id):
        post = models.Post(unique_id=unique_id)
        post.tell()

        res = conf.posts.find_one({'_id': objectid.ObjectId(unique_id)})
        res['_id'] = str(res['_id'])
        return json.dumps(res)


@app.route('/post/<unique_id>', methods=['DELETE'])
def delete_post(unique_id):
    if know_post(unique_id):
        if not Request.get_json(request):
            req = request.get_json(request)
            post = models.Post(unique_id=unique_id)
            if not 'password' in req:
                abort(400)

            if post.delete(request.json['password']):
                return json.dumps({'result': True})
            else:
                return json.dumps({'result': False, 'message': 'Not matching password.'})


@app.route('/post', methods=['POST'])
def post_content():
    if not Request.get_json(request):
        abort(400)

    req = Request.get_json(request)
    if not 'content' in req:
        abort(400)

    post = models.Post()
    post.content = req['content']
    post.password = req['password'] if 'password' in req else make_password()
    result = post.post()

    # Create response data.
    res = conf.posts.find_one({'_id': result})
    res['_id'] = str(res['_id'])
    return json.dumps(res)


def make_password(length=6):
    # Make font map
    alphabets = []
    codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
    for r in codes:
        chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
        alphabets.extend(chars)

        password = [random.choice(alphabets) for _ in range(length)]
        password = ''.join(password)

        return password

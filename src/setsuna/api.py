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



@app.route('/api/posts?limit=<int:limit>', methods=['GET'])



@app.route('/<lang>/posts', methods=['GET'])



@app.route('/api/v1.0/posts?start=<date_time_s>&end=<date_time_e>', methods=['GET'])



@app.route('/<lang>/posts?start=<date_time_s>&end=<date_time_e>', methods=['GET'])



@app.route('/post/<unique_id>', methods=['GET'])



@app.route('/post/<unique_id>', methods=['POST'])



@app.route('/post/<unique_id>', methods=['DELETE'])



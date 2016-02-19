import json
from setsuna import app
from flask_restful import reqparse, abort, Api, Resource

api = Api(app)

def abort_if_post_doesnot_exist(unique_id):
    if unique_id not in app.DATABASE.find({"unique_id": unique_id},
                                          {"unique_id": 1, "_id": 0}):
        abort(404, message="Post {} is nothing. Maybe, This post was delete \
                            or die.")

parser = reqparse.RequestParser()
parser.add_argument("content")
parser.add_argument("delkey")
parser.add_argument("unique_id")

class Posts(Resource):
    def get(self):
        args = parser.parse_args()
        posts = app.DATABASE.find().limit(args['limit'])
        for post in posts:
            del post["_id"]

        return posts

    def post(self):
        args = parser.parse_args()
        post = app.Content(0)
        post.content = args["content"]
        post.delkey = args["delkey"]
        post.post()
        return post_content, 201

class Post(Resource):
    def get(self, unique_id):
        abort_if_post_doesnot_exist(unique_id)
        post = app.DATABASE.find({"unique_id:": unique_id})
        del post["_id"]
        return json.dumps(post)

    def delete(self, unique_id):
        args = parser.parse_args()
        abort_if_post_doesnot_exist(args["unique_id"])
        post = app.Content(args["unique_id"])
        if post.delete(args["delkey"]):
            return "Delete {}".format(args["unique_id"]), 204
        else:
            return "Unmatched password.", 200

# Actualy setup the Api resource routing
api.add_resource(Posts, '/api/1/')
api.add_resource(Post, '/api/1/<unique_id>')

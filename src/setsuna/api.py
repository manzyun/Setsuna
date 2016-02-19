import json
from setsuna import app
from flask_restful import response, abort, Api, Resource

api = Api(app)

def abort_if_post_doesnot_exist(unique_id):
    if unique_id not in app.DATABASE.find({"unique_id": unique_id},
                                          {"unique_id": 1, "_id": 0}):
        abort(404, message="Post {} is nothing. Maybe, This post was delete \
                            or die.")

parser = reqperse.RequestParser()
parser.add_argment("content")
parser.add_argment("delkey")
parser.add_argment("unique_id")

class Post(Resource):
    def get(self, unique_id):
        
        abort_if_post_doesnot_exist(unique_id)
        post = app.DATABASE.find({"unique_id:": unique_id})
        del post["_id"]
        return json.dumps(post)

    def post(self):
        args = parser.parse_args()
        post = app.Content(0)
        post.content = args["content"]
        post.delkey = args["delkey"]
        post.post()

        return post_content, 201

    def delete(self):
        args = parser.parse_args()
        abort_if_post_doesnot_exist(args["unique_id"])
        post = app.Content(args["unique_id"])
        if post.delete(args["delkey"]):
            return "Delete {}".format(args["unique_id"]), 204
        else:
            return "Unmatched password.", 200


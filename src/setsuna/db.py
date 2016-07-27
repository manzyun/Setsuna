from pymongo import MongoClient
from bson import objectid
from . import models
from . import conf as db

'''
This module is access DB for Setsuna
'''

def read_from_db(uid: str):
'''
Read contributon from DB.

return -- Post object. If data have 'link' then return ResponsePost object.
'''
    tmp = db.posts.find_one({'_id': objectid.ObjectId(unique_id)})
    if 'link' in tmp:
        re_post = ResponsePost(tmp['link'], tmp['content'], tmp['password'], tmp['lang'])
        re_post.add_id(str(tmp['_id']))
        re_post.rewrite_limit(tmp['limit'])
        return re_post
    else
        re_post = Post(tmp['content'], tmp['password'], tmp['lang'])
        re_post.add_id(str(tmp['_id']))
        re_post.rewrite_limit(tmp['limit'])
        return re_post


def write_post(post):
'''
Write Post object to DB.

return -- Contribution id.
'''
    result = db.posts.insert_one({'content': self.content,
                            'limit': self.limit,
                            'password': self.password})
    return str(result.inserted_id)


def write_response(post: ResponsePost):
'''
Write ResponsePost to DB.

return -- Contribution id.
'''
    result = db.posts.insert_one({'content': self.content,
                            'limit': self.limit,
                            'password': self.password,
                            'link': self.link})
    return str(result.inserted_id)


def apothanasia(post):
'''
Contribution prolonging life.  

return -- wrote result.
'''
    conf.posts.update_one({'_id': objectid.ObjectId(post.id)},
                            {'$set': {'limit': post.limit}})

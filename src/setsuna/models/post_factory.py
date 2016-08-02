from bson import objectid
from .. import conf
from . import post, response_post


def post_factory(uid):
'''
Make Post or ResponsePost class from DB data.

uid -- Identity key in DB.  
return -- Post or ResponsePost object.  
'''
    re_post = None
    db_res = db.posts.find_one({'_id': uid})
    if 'link' in db_res:
        re_post = ResponsePost(db_res['_id'], db_res['link'],db_res['content'],
                                db_res['password'], db_res['lang'])
    else:
        re_post = Post(db_res['_id'], db_res['content'], db_res['password'],
                        db_res['lang'])
    return re_post.get(re_post.id)

from bson import objectid
from .. import conf as db
from . import post, response_post


def post_factory(uid):
    '''
    Make Post or ResponsePost class from DB data.

    uid -- Identity key in DB.  
    return -- Post or ResponsePost object.  
    '''
    re_post = None
    db_res = db.posts.find_one({'_id': objectid.ObjectId(uid)})
    if 'link' in db_res:
        re_post = response_post.ResponsePost('', '','', '')
        re_post.get_post(uid)
    else:
        re_post = post.Post('', '', '')
        re_post.get_post(uid)
    return re_post

import json
from . import models
from bson import objectid
from . import conf

timeformat = '%Y-%m-%d %H:%M:%S'

'''
JSON serialize from Setsuna models.
'''

# to JSON

def postToJson(self, obj: models.Post) -> dict:
'''
Post object to JSON Object
obj -- Want serialize Post object.  
'''
    re_dict = {k:v for k, v in obj}
    return re_dict
    raise TypeError(repr(obj) + ' is not JSON selializable')

def withId(self, obj: models.IdWithPost) -> dict:
'''
IdWithPost object to JSON object.  
obj -- Want serialize IdWithPost object.  
'''
    re_dict = {obj.unique_id: {k:v for k, v in obj.post}}
    return re_dict
    raise TypeError(repr(obj) + ' is not JSON selializable')

def listLang(self, obj: LangPosts) -> dict:
'''
LangPosts object to JSON object.  
obj -- Want serialize LangPosts object.  
'''
    inner_list = []
    for post in obj.posts:
        tmp = {uid: {k:v for k, v in data} for uid, post in post}
        inner_list.append(tmp)
    
    re_dict = {obj.lang: inner_list}
    return re_dict
    raise TypeError(repr(obj) + ' is not JSON selializable')


# to Python object


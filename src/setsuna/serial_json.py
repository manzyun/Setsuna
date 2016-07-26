import json
from . import models
from bson import objectid
from . import conf

timeformat = '%Y-%m-%d %H:%M:%S'

'''
JSON serialize from Setsuna models.
'''

# to JSON

def post_to_json(self, obj: models.Post):
'''
Post object to JSON Object
obj -- Want serialize Post object.  
'''
    isinstance(obj, models.LangPosts):
        re_dict = {k:v for k, v in obj}
        return re_dict
    raise TypeError(repr(obj) + ' is not JSON selializable')


# to Python object

def to_post(self, json_obj) -> models.Post:
'''
JSON data to Post object.  
json -- json data
'''
    tmp_dic = json.load(json_obj)
    re_post = models.Post(tmp_dic['content'], tmp_dic['limit'], tmp_dic['password'], tmp_dic['lang'])
    return re_post

import json
from . import models
from bson import objectid
from . import conf

timeformat = '%Y-%m-%d %H:%M:%S'

'''
JSON serialize from Setsuna models.
'''

class ModelEncoder(json.JsonEncoder):
    def default(self, obj: models.Post):
    '''
    Post object to JSON Object
    obj -- Want serialize Post object.  
    '''
        re_dict = {}
        for k, v in obj:
            re_dict[k] = v
        return re_dict

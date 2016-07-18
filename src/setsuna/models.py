from . import conf
from datetime import datetime, timedelta
from bson import objectid

timeformat = '%Y-%m-%d %H:%M:%S'


class Post(object):
    def __init__(self, content, limit, password):
        self.content = content
        self.limit = limit
        self.password = password
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    def __getitem__(self, key):
        return self.__dict__[key]
    def __setitem__(self, key, value):
        self.__dict__[key] = value

class IdWithPost(Post)
    def __init__(self, unique_id, post):
        self.unique_id = unique_id
        self.post = post
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    def __getitem__(self, key):
        return self.__dict__[key]
    def __setitem__(self, key, value):
        self.__dict__[key] = value

class LangPost(Post):
    def __init__(self, lang):
        self.lang = lang
        self.posts = []
    def __iter__(self):
        return self.__dict__.iteritems()
    def __str__(self):
        return str(self.__dict__)
    def __len__(self):
        return len(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    def __getitem__(self, unique_id):
        return self.__dict__[unique_id]
    def __setitem__(self, unique_id, post):
        self.__dict__[unique_id] = post


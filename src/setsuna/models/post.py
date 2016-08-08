from time import time
from .. import conf as db
from .. import conf
from bson import objectid
from math import random


class Post:
    '''
    Base post class.  

    uid -- identity key from DB.  
    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.
    lang -- Language code by ISO 639-3.  
    '''
    def __init__(self, uid: str, content: str, password: str, lang: str):
        '''
        Make post.  

        content -- Post content.  
        limit -- Delete time. Record style is Unix time.  
        password -- Password for manually delete.  
        lang -- Language code by ISO 639-3.  
        '''
        self.id = uid
        self.content = content
        self.limit = int(time.time()) + 3600 * conf.life
        self.password = self.make_password() if '' else password
        self.lang = lang if not lang in _LANG_LIST else 'und'


    def post_contribution(self) -> str:
        '''
        Post contribution.

        return -- identity key from DB
        '''
        result = db.posts.insert_one({'content': self.content,
                                'limit': self.limit,
                                'password': self.password,
                                'lang': self.lang
                                })
        self.id = result.inserted_id
        return self.id


    def apothanasia(self):
        '''
        Contribution prolonging life.  

        return -- new delete limit time.
        '''
        self.limit = self.limit + 3600
        db.posts.update_one({'_id': objectid.ObjectId(self.id)},
                            {'$set': {'limit': self.limit}})


    def get_post(self, uid: str):
        '''
        Get contribution from DB.  

        uid -- identity ID
        '''
        re = db.posts.find_one({'_id': objectid.ObjectId(uid)})
        if 'link' in re:
            raise TypeError(repr(re) + ' is not nomal contributon.')
        self.id = re['_id']
        self.content = re['content']
        self.limit = re['time']
        self.password = re['password']
        self.lang = re['lang']


    def password_checker(self, password: str):
        '''
        Password checker
        
        password -- Sample password
        '''
        if password == self.password:
            return True
        else:
            return False


    def delete_post(self):
        '''
        Delete Contribution from DB.  
        '''
        db.posts.delete_one({'_id': objectid.ObjectId(self.id)})


    def make_password(length=4) -> str:
        '''
        Make password

        length -- Make password digit.  
        return -- Password.  
        '''

        # Make font map
        alphabets = []
        codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
        for r in codes:
            chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
            alphabets.extend(chars)

            password = [random.choice(alphabets) for _ in range(length)]
            password = ''.join(password)

            return password

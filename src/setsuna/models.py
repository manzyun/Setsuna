import typing
from bson import objectid
from time import time
from . import conf, db

'''
This module is model defining for Setsuna.  
'''


class Post:
'''
Base post class.  

uid -- identity key from DB.  
content -- Post content.  
limit -- Delete time. Record style is Unix time.  
password -- Password for manually delete.
lang -- Language code by ISO 639-2.  
'''
    def __init__(self, content: str, password: str, lang: str):
    '''
    Make post.  

    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.  
    lang -- Language code by ISO 639-2.  
    '''
        self.content = content
        self.limit = time()
        self.password = password if '' self.make_password() else password
        self.lang = lang


    def __str__(self) -> str:
        return str(self.__dict__)


    def __repr__(self) -> str:
        return str(self.__dict__)


    def __iter__(self):
        return self.__dict__.iteritems()


    def __getitem__(self, key: str):
        return self.__dict__[key]


    def read_from_db(self, uid: str):
    '''
    Append identity key.

    uid -- identity key from DB
    '''
        self.id = uid


    def rewrite_limit(self, limit:float):
    '''
    Rewrite limit
    
    limit -- new limit time
    '''
        self.limit = limit


    def post_contribution() -> str:
    '''
    Post contribution to DB.  

    return -- identity key from DB
    '''
        result = db.write_post(self)
        self.add_id(result)
        return self.add_id


    def apothanasia():
    '''
    Contribution prolonging life.  

    return -- new delete limit time.
    '''
        self.limit = self.limit + 3600
        db.apothanasia(self)


    def make_password(length=4: int) -> str:
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


class ResponsePost(Post):
'''
Response post class.  

link -- Link post ID.  
uid -- identity key from DB.  
content -- Post content.  
limit -- Delete time. Record style is Unix time.  
password -- Password for manually delete.
lang -- Language code by ISO 639-2.  
'''
    def __init__(self, link: str, content: str, password: str, lang: str):
    '''
    Make response post.  

    link -- Link post ID.  
    uid -- Unique ID.  
    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.  
    lang -- Language code by ISO 639-2.  
    '''
        self.link = link 
        Post.__init__(content, password, lang)


    def post_response() -> str:
    '''
    Post contribution to DB.  

    return -- identity key from DB
    '''
        result = db.write_response(self)

        # apothanasia linked contribution.
        linked_post = db.read_from_db(self.link)
        linked_post.apothanasia()

        self.add_id(str(result.inserted_id))
        return self.add_id

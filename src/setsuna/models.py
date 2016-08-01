import typing
from bson import objectid
from time import time
from . import conf, db

ISODatetime = '%Y-%M-%dT%H:%M%z'

'''
This module is model defining for Setsuna.  
'''

class Posts(list):
'''
Many Contribution list class.
'''
    def __init__(self):
        list.__init__(self)


    def get_now_posts(asc=True: bool):
    '''
    Get all contribution from DB.  

    asc -- asc / desc
    lang -- Filter language by ISO 639-2.  
    '''
        now_all = db.posts.find().sort({'Timestamp': asc if True 1 else -1})
        self.post_filter(now_all)
        if lang is not None:
            for _ in self:
                if _.lang != lang:
                    del _


    def get_posts_save(limit=10: int, asc=True: bool):
    '''
    Get save number of contribution save from DB.  

    limit -- save number of contributoin
    asc -- asc / desc
    '''
        now_save = db.posts.find().limit(limit).sort({'timestamp': asc if True 1 else -1})
        self.posts_filter(now_save)


    def get_lang_posts(lang=None: str, asc=True: bool):
    '''
    Get narrow language contribution from DB.

    lang -- narrow language
    '''
        if lang is None
            get_now_posts(asc)
            return
        lang_post = db.posts.find({'lang': lang}).sort({'timestamp': asc if True 1 else -1})
        self.posts_filter(lang_post)


    def get_lang_posts_save(lang=None: str, limit=10: int, asc=True: bool):
    '''
    Get number of contribution save and narrow language from DB.  

    limit -- save number of contributoin
    lang -- narrow language
    asc -- asc / desc
    '''
        if lang is None:
            get_posts_save(limit, asc)
            return
        lang_post = db.posts.find({'lang': lang}).limit(limit).sort({'timestamp': asc if True 1 else -1})
        self.posts_filter(lang_post)

    def get_posts_between(start: Datetime, end:Datetime, asc=True: bool):
    '''
    Get between times contributions from DB.

    start -- Start time
    end -- End time
    asc -- asc / desc
    '''

        between_post = db.posts.find({'timestanp':
                                {'$gte': datetime.strptime(start, ISODatetime),
                                 '$lte:': datetime.strptime(end, ISODatetime)}
                                 }).sort({'timestamp': asc if True 1 else -1}})
        self.posts_filter(between_post)


    def get_lang_posts_between(lang=None: str, start: Datetime, end: Datetime, asc=True: bool):
    '''
    Get between times and  contributions and narrow language from DB.

    lang -- Narrow language
    start -- Start time
    end -- End time
    asc -- asc / desc
    '''
        if lang is None:
            get_posts_between(start, end, asc)
            return
        between_lang_post = db.posts.find({{'lang': lang},
                                 {'timestanp':
                                 {'$gte': datetime.strptime(start, ISODatetime),
                                  '$lte:': datetime.strptime(end, ISODatetime)}
                                  }
                                 }).sort({'timestamp': 1})
        post_collect(data)


    def post_collect(data):
    '''
    Load DB data collect Setsuna object.  

    data -- DB response.  
    '''
        for _ in response:
            if isinstance(_, dict):
                if 'link' in _: 
                    self.append(ResponsePost(_['link'],_['_id'], _['content'], _['password'], _['lang']))
                else
                    self.append(Post(_['_id'], _['content'], _['password'], _['lang']))


def PostFactory(uid):
'''
Make Post or ResponsePost class from DB data.

uid -- Identity key in DB.  
'''
    re_post = None
    db_res = db.posts.find_one({'_id': uid})
    if 'link' in db_res:
        re_post = ResponsePost(db_res['_id'], db_res['link'], db_res['content'], db_res['password'], db_res['lang'])
    else:
        re_post = Post(db_res['_id'], db_res['content'], db_res['password'], db_res['lang'])
    return re_post.get(re_post.id)

class Post:
'''
Base post class.  

uid -- identity key from DB.  
content -- Post content.  
limit -- Delete time. Record style is Unix time.  
password -- Password for manually delete.
lang -- Language code by ISO 639-2.  
'''
    def __init__(self, uid=None: str, content: str, password=None: str, lang=None: str):
    '''
    Make post.  

    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.  
    lang -- Language code by ISO 639-2.  
    link -- Link post ID.  
    '''
        self.id = uid
        self.content = content
        self.limit = time()
        self.password = password if None self.make_password() else password
        self.lang = lang
        self.link = link 

    def __str__(self) -> str:
        return str(self.__dict__)


    def __repr__(self) -> str:
        return str(self.__dict__)


    def __iter__(self):
        return self.__dict__.iteritems()


    def __getitem__(self, key: str):
        return self.__dict__[key]


    def post_contribution() -> str:
    '''
    Post self.id = uid
        self.content = content
        self.limit = time()
        self.password = password if None self.make_password() else password
        self.lang = lang
        self.link = link contribution to DB.  

    return -- identity key from DB
    '''
        result = db.posts.insert_one({'content': self.content,
                                'limit': self.limit,
                                'password': self.password})
        self.id = result.inserted_id
        return self.id


    def apothanasia():
    '''
    Contribution prolonging life.  

    return -- new delete limit time.
    '''
        self.limit = self.limit + 3600
        db.posts.update_one({'_id': objectid.ObjectId(self.id)},
                            {'$set': {'limit': self.limit}})


    def get_post(uid: str):
    '''
    Get contribution from DB.  

    uid -- identity ID
    '''
        re = db.posts.find_one({'_id': objectid.ObjectId(uid)})
        if 'link' in re:
            raise TypeError(repr(re) + ' is not nomal contributon.')
        self.id = re[_id]
        self.content = re['content']
        self.limit = re['time']
        self.password = re['password']
        self.lang = re['lang']


    def password_checker(password='': str):
    '''
    Password checker
    
    password -- Sample password
    '''
        if password == self.password:
            return True
        else
            return False


    def delete_post():
    '''
    Delete Contribution from DB.  
    '''
        db.posts.delete_one({'_id': objectid.ObjectId(self.id)})


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
    def __init__(self, uid=None: str, link: str, content: str, password=None: str, lang=None: str):
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
        Post.__init__(uid, content, password, lang)


    def post_contribution() -> str:
    '''
    Post contribution to DB.  

    return -- identity key from DB
    '''
        result = db.posts.insert_one({'content': self.content,
                                'limit': self.limit,
                                'password': self.password,
                                'link': self.link})

        # apothanasia linked contribution.
        linked_post = db.read_from_db(self.link)
        linked_post.apothanasia()

        self.id = str(result.inserted_id)
    return self.id


    def get_post(uid: str):
    '''
    Get contribution from DB.  

    uid -- identity ID
    '''
    if not 'link' in re:
            raise TypeError(repr(re) + ' is not link contributon.')
        self.id = re[_id]
        self.content = re['content']
        self.limit = re['time']
        self.password = re['password']
        self.lang = re['lang']

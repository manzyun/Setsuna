import typing
from bson import objectid
from time import time
from .. import conf as db
from . import post, response_post


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

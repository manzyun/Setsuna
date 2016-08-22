from datetime import datetime
from .. import conf as db
from . import post, response_post
from bson import objectid
import pymongo


class Posts(list):
    '''
    Many Contribution list class.
    '''
    def __init__(self):
        list.__init__(self)


    def get_now_posts(self, asc=True):
        '''
        Get all contribution from DB.  

        asc -- asc / desc
        lang -- Filter language by ISO 639-2.  
        '''
        now_all = db.posts.find().sort('timestamp', pymongo.ASCENDING if asc==True else pymongo.DESCENDING)
        self.post_collect(now_all)


    def get_posts_save(self, limit=10, asc=True):
        '''
        Get save number of contribution save from DB.  

        limit -- save number of contributoin
        asc -- asc / desc
        '''
        now_save = db.posts.find().limit(limit).sort({'timestamp': pymongo.ASCENDING if asc==True else pymongo.DESCENDING})
        self.post_collect(now_save)


    def get_lang_posts(self, lang='und', asc=True):
        '''
        Get narrow language contribution from DB.

        lang -- narrow language
        '''
        lang_post = db.posts.find({'lang': lang}).sort({'timestamp': pymongo.ASCENDING if asc==True else pymongo.DESCENDING})
        self.post_collect(lang_post)


    def get_lang_posts_save(self, lang='und', limit=10, asc=True):
        '''
        Get number of contribution save and narrow language from DB.  

        limit -- save number of contributoin
        lang -- narrow language
        asc -- asc / desc
        '''
        lang_post = db.posts.find({'lang': lang}).limit(limit).sort({'timestamp': pymongo.ASCENDING if asc==True else pymongo.DESCENDING})
        self.post_collect(lang_post)

    def get_posts_between(self, start: datetime, end:datetime, asc=True):
        '''
        Get between times contributions from DB.

        start -- Start time
        end -- End time
        asc -- asc / desc
        '''
        between_post = db.posts.find({'timestanp':
                                {'$gte': start.strptime(_DATE_FORMAT),
                                 '$lte:': start.strptime(_DATE_FORMAT)}
                                 }).sort({'timestamp': pymongo.ASCENDING if asc==True else pymongo.DESCENDING})
        self.post_collect(between_post)


    def get_lang_posts_between(self, start: datetime, end: datetime, lang='und', asc=True):
        '''
        Get between times and  contributions and narrow language from DB.

        lang -- Narrow language
        start -- Start time
        end -- End time
        asc -- asc / desc
        '''
        between_lang_post = db.posts.find({{'lang': lang},
                                 {'timestanp':
                                 {'$gte': start.strptime(_DATE_FORMAT),
                                  '$lte:': end.strptime(_DATE_FORMAT)}
                                  }
                                 }).sort({'timestamp': pymongo.ASCENDING if asc==True else pymongo.DESCENDING})
        self.post_collect(between_lang_post)


    def post_collect(self, data):
        '''
        Load DB data collect Setsuna object.  

        data -- DB response.  
        '''
        for _ in data:
            if isinstance(_, dict):
                if 'link' in _: 
                    tmp = response_post.ResponsePost('','', '', '')
                    tmp.get_post(objectid.ObjectId(_['_id']))
                    self.append(vars(tmp))
                else:
                    tmp = post.Post('', '', '')
                    tmp.get_post(objectid.ObjectId(_['_id']))
                    self.append(vars(tmp))

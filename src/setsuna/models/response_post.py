from . import post
from .. import conf as db
from bson import objectid

class ResponsePost(post.Post):
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
        content -- Post content.  
        password -- Password for manually delete.  
        lang -- Language code by ISO 639-2.  
        link -- Response to.  
        '''
        super().__init__(content, password, lang)
        self.link = link 


    def post_contribution(self) -> str:
        '''
        Post contribution to DB.  

        return -- identity key from DB
        '''
        result = db.posts.insert_one({'content': self.content,
                                'limit': self.limit,
                                'password': self.password,
                                'lang': self.lang,
                                'link': self.link})

        # apothanasia linked contribution.
        linked_post = post.Post('', '', '')
        linked_post.get_post(self.link)
        linked_post.apothanasia()

        self.id = str(result.inserted_id)
        return self.id


    def get_post(self, uid: str):
        '''
        Get contribution from DB.  

        uid -- identity ID
        '''
        re = db.posts.find_one({'_id': objectid.ObjectId(uid)})

        if not 'link' in re:
            raise TypeError(repr(re) + ' is not link contributon.')
        self.id = str(re['_id'])
        self.content = re['content']
        self.limit = re['limit']
        self.password = re['password']
        self.lang = re['lang']
        self.link = re['link']

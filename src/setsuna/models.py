import typing


'''
This module is model defining for Setsuna.  
'''

class Post:
'''
Base post class.  

content -- Post content.  
limit -- Delete time. Record style is Unix time.  
password -- Password for manually delete.
'''
    def __init__(self,uid: int, content: str, limit: int, password: str, lang: str) -> None:
    '''
    Make post.  
    uid -- Unique ID.  
    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.  
    lang -- Language code by ISO 639-2.  
    '''
        self.id = uid
        self.content = content
        self.limit = limit
        self.password = password
        self.lang = lang
    def __str__(self) -> str:
        return str(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
    def __iter__(self):
        return self.__dict__.iteritems()
    def __getitem__(self, key: str) -> int ~ str:
        return self.__dict__[key]
    def __setitem__(self, key: str, value) -> None:
        self.__dict__[key] = value


class ResponsePost(Post):
'''
Response post class.  
'''
    def __init__(self, link: int, uid: int, content: str, limit: int, password: str, lang: str) -> None:
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
        Post.__init__(uid, content, limit, password, lang)
    def __str__(self) -> str:
        return str(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
    def __iter__(self):
        return self.__dict__.iteritems()
    def __getitem__(self, key: str) -> int ~ str:
        return self.__dict__[key]
    def __setitem__(self, key: str, value) -> None:
        self.__dict__[key] = value

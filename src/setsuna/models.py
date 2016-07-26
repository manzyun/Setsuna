import typing


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
    def __init__(self, content: str, limit: int, password: str, lang: str) -> None:
    '''
    Make post.  

    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.  
    lang -- Language code by ISO 639-2.  
    '''
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
    def add_id(self, uid: int) -> None:
    '''
    Append identity key.
    uid -- identity key from DB
    '''
        self.id = uid


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
    def __init__(self, link: int, content: str, limit: int, password: str, lang: str) -> None:
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
        Post.__init__(content, limit, password, lang)
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

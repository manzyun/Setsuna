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
    def __init__(self, content: str, limit: int, password: str) -> None:
    '''
    Make post.  
    content -- Post content.  
    limit -- Delete time. Record style is Unix time.
    password -- Password for manually delete.
    '''
        self.content = content
        self.limit = limit
        self.password = password
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

class IdWithPost(Post)
'''
Plus unique id for post.  
'''
    def __init__(self, unique_id: int, post: Post) -> None:
    '''
    Initialize instance  
    
    unique_id -- ID from mongoDB.  
    post -- Post data.  
    '''
        self.unique_id = unique_id
        self.post = post
    def __str__(self) -> str:
        return str(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
            def __iter__(self):
        return self.__dict__.iteritems()
    def __getitem__(self, key: int):
        return self.__dict__[key]
    def __setitem__(self, key: int, value: Post) -> None:
        self.__dict__[key] = value

class LangPost():
'''
Segregation language posts.  
'''
    def __init__(self, lang: str) -> None:
    '''
    Initialize instance.  
    
    lang -- Language code. 2 digit.  
    '''
        self.lang = lang
        self.posts = []
    def __iter__(self):
        return self.__dict__.iteritems()
    def __str__(self) -> str:
        return str(self.__dict__)
    def __len__(self) -> int:
        return len(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
    def __getitem__(self, unique_id: int) -> IdWithPost:
        return self.post.index(unique_id)
    def __setitem__(self, unique_id: int, post: Post):
        self.posts.append(IdWithPost(unique_id, post))

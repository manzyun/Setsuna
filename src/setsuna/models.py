import typing
from . import conf
from datetime import datetime, timedelta
from bson import objectid

timeformat = '%Y-%m-%d %H:%M:%S'


class Post:
    def __init__(self, content: str, limit: int, password:str) -> None:
        self.content = content
        self.limit = limit
        self.password = password
    def __str__(self) -> str:
        return str(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
    def __getitem__(self, key: str) -> int ~ str:
        return self.__dict__[key]
    def __setitem__(self, key: str, value) -> None:
        self.__dict__[key] = value

class IdWithPost(Post)
    def __init__(self, unique_id: int, post: Post) -> None:
        self.unique_id = unique_id
        self.post = post
    def __str__(self) -> str:
        return str(self.__dict__)
    def __repr__(self) -> str:
        return str(self.__dict__)
    def __getitem__(self, key: int):
        return self.__dict__[key]
    def __setitem__(self, key: int, value: Post) -> None:
        self.__dict__[key] = value

class LangPost():
    def __init__(self, lang: str) -> None:
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
        return self.__dict__[unique_id]
    def __setitem__(self, unique_id: int, post: Post):
        self.__dict__[unique_id] = post


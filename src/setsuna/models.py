import typing
from . import conf
from datetime import datetime, timedelta
from bson import objectid

timeformat = '%Y-%m-%d %H:%M:%S'

'''
`JSON API`_ におけるdataオブジェクトの中身を定義しておくモジュールである。

.. _`JSON API`: http://jsonapi.org/
'''

class Post:
'''
投稿の基礎となるクラス
'''
    def __init__(self, content: str, limit: int, password: str) -> None:
    '''
    ポストの作成。
    @param content 投稿内容
    @param limit 削除時間(Unixtime)
    @param password 手動削除時のパスワード
    '''
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
'''
投稿にunique_idを付与したクラス
'''
    def __init__(self, unique_id: int, post: Post) -> None:
    '''
    投稿にunique_idを付与する
    
    @param unique_id mongodbから取得できるid
    @param post 投稿データ
    '''
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
'''
言語ごとに投稿を分けるクラス
'''
    def __init__(self, lang: str) -> None:
    '''
    言語設定したリストを作る
    
    @param lang 言語コード2桁
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

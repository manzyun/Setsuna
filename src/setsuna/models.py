from .conf import _conf
from pymongo import MongoClient
from datetime import datetime, timedelta
import random

timeformat = '%Y-%m-d %H:%M:%S'


class Post:
    # DB Connection
    connect = MongoClient(_conf['address'], _conf['port'])
    posts = connect[_conf['database']][_conf['collection']]

    def __init__(self, unique_id=None):
        if unique_id is None:
            self.unique_id = ''
            self.content = ''
            self.limit = 0.0
            self.delkey = ''
        else:
            # Read DB
            self.unique_id = unique_id
            post = Post.posts.find_one({'_id': self.unique_id})
            self.content = post['content']
            self.limit = post['limit']
            self.delkey = post['delkey']

    def post(self, delkey=''):
        self.delkey = delkey if delkey != '' else make_delkey()
        self.limit = (datetime.utcnow() + timedelta(seconds=86400)).strftime(timeformat)

        # Writing DB
        result = Post.posts.insert_one({'content': self.content,
                                        'limit': self.limit,
                                        'delkey': self.delkey})
        self.unique_id = str(result.inserted_id)
        return result.inserted_id

    def delete(self,  delkey=''):
        if self.delkey == delkey:
            # Remove post in DB
            Post.posts.delete_one({'_id': self.unique_id})
            return True
        else:
            return False


def make_delkey(length=6):
    # Make font map
    alphabets = []
    codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
    for r in codes:
        chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
        alphabets.extend(chars)

        password = [random.choice(alphabets) for _ in range(length)]
        delkey = ''.join(password)

        return delkey

if __name__ == '__main__':
    test = Post()

    test.connect = 'にくまん'
    test.delkey = 'hogefuga'
    test.limit = 123456.78

    read = test.post()

    samplepost = Post()


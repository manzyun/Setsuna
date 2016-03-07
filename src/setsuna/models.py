from .conf import _conf
from pymongo import MongoClient
import json
import datetime
import random
import bson


class Post():
    # DB Connection
    connect = MongoClient(_conf["address"], _conf["port"])
    posts = connect[_conf["database"]][_conf["collection"]]

    def __init__(self):
        # Read DB
        self._id = None
        self.content = ""
        self.limit = 0.0
        self.delkey = ""

    def read(self, _id):
        # Read DB
        self._id = _id
        post = Post.posts.find_one({"_id": self._id})
        self.content = post["content"]
        self.limit = post["limit"]
        self.delkey = post["delkey"]

    def post(self, content="", delkey=""):
        self.content = content
        self.delkey = delkey
        if self.delkey == "":
            self.delkey = make_delkey()
        self.limit = datetime.timedelta(seconds=28800)

        # Writing DB
        try:
            result = Post.posts.insert_one({"content": self.content,
                "limit": self.limit,
                "delkey": self.delkey})
            return str(result["_id"])
        except Exception as e:
            return e

    def delete(self, delkey):
        try:
            if self._id == _id and self.delkey == delkey:
                # Remove post in DB
                collection.delete_one({"_id": self._id})
                return True
            else:
                return False
        except Exception as e:
            return e

def make_delkey(length=6):
    # Make font map
    alphabets = []
    codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
    for r in codes:
        chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
        alphabets.extend(chars)

        password = [random.choice(alphabets) for _ in range(length)]
        delkey = "".join(password)

        return delkey

if __name__ == "__main__":
    test = Post()

    test.connect = "にくまん"
    test.delkey = "hogefuga"
    test.limit = 123456.78

    print(test.post())

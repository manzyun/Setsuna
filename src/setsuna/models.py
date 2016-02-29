from setsuna import conf
from pymongo import MongoClient
import json
import time
import datetime
import random


class Post():
    # DB Connection
    connect = MongoClient(conf._conf["address"], conf._conf["port"])
    posts = connect[conf._conf["database"]][conf._conf["collection"]]

    def __init__(self):
        # Read DB
        self.unique_id = None
        self.content = ""
        self.limit = 0.0
        self.delkey = ""

    def read(self, unique_id):
        # Read DB
        self.unique_id = unique_id
        post = Post.posts.find_one({"unique_id": self.unique_id})
        del post['_id']
        self.content = post["content"]
        self.limit = post["limit"]
        self.delkey = post["delkey"]
        print(post)

    def post(self):
        if self.delkey == "":
            self.delkey = make_delkey()
        self.limit = datetime.timedelta(seconds=28800)

        # Writing DB
        try:
            result = collection.insert_one(
                    json.dumps(self).translate(string.marketrans("",""),"[]"))
            return True
        except Exception as e:
            return e

    def delete(self, delkey):
        try:
            if self._id == unique_id and self.delkey == delkey:
                # Remove post in DB
                collection.delete_one({"unique_id": self.unique_id})
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


import setsuna
import json
import time
import datetime
import random


class Post(Object):
    # DB Connection
    db = setsuna.DATABASE
    posts = db.posts

    def __init__(_id = 0):
        # Read DB
        self._id = _id
        if self._id != 0:
            self.content = ""
            self.limit = 0.0
            self.delkey = ""
        else:
            post = posts.find_one({"_id":self._id})
            self.content = post.content
            self.limit = post.limit
            self.delkey = delkey

    def post(content, delkey=""):
        if delkey == "":
            delkey = make_delkey()
        self.content = content
        self.limit = datetime.timedelta(seconds=28800)
        self.delkey = delkey

        # Writing DB
        collection.save = json.dump(self)

    def delete(_id, delkey):
        if self._id == _id and self.delkey == delkey:
            # Remove post in DB
            collection.remove({"id":self._id})

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

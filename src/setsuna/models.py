import setsuna
import json
import time
import datetime
import random


class Post(Object):
    # DB Connection
    db = setsuna.DATABASE
    posts = db.posts

    def __init__(unique_id=0):
        # Read DB
        try:
            self.unique_id = unique_id
            if self.unique_id == 0:
                self.unique_id = app.DATABASE.find_one(
                        {}, {unique_id: 1, _id: 0})
                self.content = ""
                self.limit = 0.0
                self.delkey = ""
            else:
                post = posts.find_one({"unique_id": self.unique_id})
                self.content = post.content
                self.limit = post.limit
                self.delkey = delkey
        except Exception as e:
            return e

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
                collection.remove({"unique_id": self.unique_id})
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


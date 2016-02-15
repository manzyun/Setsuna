from pymongo import MongoClient
import json
import configparser
import time
import datetime
import random


config = configparser.ConfigParser()
config.read('config.ini')

class Content(object):
    # DB Connection
    connect = MongoClient(config['develop']['mongodb'], 27017)
    db = connect.test
    posts = db.posts
    print('Connection to ', db.name)

    def __init__(post_id = 0):
        # Read DB
        self.post_id = post_id
        if self.post_id != 0:
            self.content = ""
            self.limit = 0
            self.delkey = ""
        else:
            post = posts.find_one({"post_id":self.post_id})
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

    def delete(unique_id, delkey):
        if self.unique_id == unique_id and self.delkey == delkey:
            # Remove post in DB
            collection.remove({"id":self.unique_id})

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

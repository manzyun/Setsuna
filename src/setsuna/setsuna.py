from conf import _conf
from pymongo import MongoClient
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
import scheme

# configuration
CLIENT = MongoClient(_conf["address"], _conf["ip"])
DATABASE = CLIENT[_conf["database"]]
DEBUG = True

# create app
app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    scheme.init_db()

if __name__ == "__main__":
    app.run()


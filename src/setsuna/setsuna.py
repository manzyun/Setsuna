from pymongo import MongoClient
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
import scheme

# configuration
CLIENT = MongoClient('10.0.3.116', 27017)
DATABASE = CLIENT["setsuna"]["posts"]
DEBUG = True

# create app
app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    scheme.init_db()

if __name__ == "__main__":
    app.run()

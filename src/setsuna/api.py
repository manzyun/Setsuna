from setsuna import app, models, conf
from pymongo import MongoClient

client = MongoClient()

@app.route('/')
def index():
    return "Welcome, Setsuna!"


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():



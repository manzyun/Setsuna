from setsuna import app
from flask import render_template


@app.route('/')
def index():
    news = []
    bson_news = conf.posts.find().sort({'timestamp': 1})
    return render_template('views/index.html')


@app.route('/<unique_id>')
def content(unique_id):

    return render_template('views/unique.html')


@app.route('/new')
def post():
    return render_template('views/new.html')

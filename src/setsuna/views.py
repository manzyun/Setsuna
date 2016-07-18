from setsuna import app, conf
from flask import render_template


@app.route('/')
def top():
    contents = []
    bson_news = conf.posts.find()
    for b_new in bson_news:
        if isinstance(b_new, dict):
                b_new['_id'] = str(b_new['_id'])

        contents.append(b_new)

    return render_template('index.html')


@app.route('/<unique_id>')
def content(unique_id):

    return render_template('unique.html')


@app.route('/new')
def post():
    return render_template('form.html')

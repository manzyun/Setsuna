from setsuna import app
from flask import render_template


@app.route('/')
def index():
    return render_template('views/index.html')


@app.route('/<unique_id>')
def post(unique_id):
    return render_template('views/unique.html')

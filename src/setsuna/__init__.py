from flask import Flask
app = Flask(__name__)

from .models import post, response_post, posts, post_factory
from .views import api

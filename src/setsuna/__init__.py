from flask import Flask
app = Flask(__name__)

import setsuna.api, setsuna.view

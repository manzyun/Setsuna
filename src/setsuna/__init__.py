from flask import Flask
app = Flask(__name__)

# import setsuna.killer
import setsuna.api, setsuna.views

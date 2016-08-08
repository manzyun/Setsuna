from flask import Flask

# configuration
DEBUG = True

# create app
app = Flask(__name__)
app.config.from_object(__name__)


if __name__ == "__main__":
    app.run()


#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns 'Hello, HBNB!' on the main index route"""
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_index():
    """Returns 'HBNB' on route /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route():
    """Returns 'Hello, HBNB!' on the main route route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns 'HBNB' on route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns 'C <text>' on route /c"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text='is cool'):
    """Returns 'Python <text>' on route /python"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Returns '<n> is a number' on route /number/ if n is integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Returns '<n> is a number' on route /number/ if n is integer,
    as template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_template(n):
    """Returns '<n> is even|odd' on route /number/ if n is integer,
    as template"""
    div_2_txt = 'even' if n % 2 == 0 else 'odd'
    return render_template("6-number_odd_or_even.html",
                           n=n, div_2_bool=div_2_txt)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

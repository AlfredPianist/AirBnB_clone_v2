#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes connection with db"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def filters():
    """Returns the info for the page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template("100-hbnb.html", **(locals()))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

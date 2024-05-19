#!/usr/bin/python3
"""Routes:
/hbnb_filters: display a HTML page like 6-index.html, which was done during
the project 0x01. AirBnB clone - Web static
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page: (inside the tag BODY) H1 tag: “States"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

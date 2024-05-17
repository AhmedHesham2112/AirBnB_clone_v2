#!/usr/bin/python3
"""Starts a Flask web application.

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'
you must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Display 'Hello HBNB!' """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

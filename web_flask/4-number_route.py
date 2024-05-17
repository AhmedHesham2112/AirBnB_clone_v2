#!/usr/bin/python3
"""Starts a Flask web application.

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of the text
        variable, The default value of text is “is cool”.
    /number/<n>: display “n is a number” only if n is an integer
you must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Display 'C' followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """display “Python ”, followed by the value of the text
    variable, The default value of text is “is cool”."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """display 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

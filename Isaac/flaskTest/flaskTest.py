# flaskTest.py
#
# -To be used for locally (localhost) testing the web server/website.
# -Installing the flask package on a virtual environment (instead of system-wide)
# is recommended by Flask devs.
#
# http://flask.pocoo.org/docs/0.12/quickstart/#
#
# -Isaac Park, keonp2
#

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    greeting = 'Welcome to Reddit Unlocked, a CS 196 Project @ UIUC<br/><br/>-Isaac'
    return greeting


@app.route('/docs')
def docs():
    report = 'This page will contain an explanation of our project and findings'
    return report


@app.route('/program')
def program():
    page = 'This page will contain our Reddit analysis program'
    return page


@app.route('/hello')
def hello_world():
    return 'Hello, World'

# Use url_for method for links in the webpage; url_for generates URL
# based on the argument it is given (name of the function related to a URL.
#
# Example:
#
# @app.route('/user/<name>')
# def hello_user(name):
#   if name =='admin':
#      return redirect(url_for('hello_admin'))
#   else:
#      return redirect(url_for('hello_guest',guest = name))
#

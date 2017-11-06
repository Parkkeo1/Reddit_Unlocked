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

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/docs/<section>')
def docs(section):
    return render_template("docs.html", section=section)

"""
@app.route('/homeTest', methods=['GET', 'POST'])
def request_test():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


# testing ints in URL variables
@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post ID is %s" % post_id


@app.route('/program')
def program():
    page = 'This page will contain our Reddit analysis program'
    return page


@app.route('/authors')
def group():
    members = 'Made by Isaac Park, Jayam Shah, Gary Braznichenko, Ben Vacek, Ismail Dayan, and Keshav Shivam'
    return members
    
"""


if __name__ == "__main__":
    app.run(debug=True)

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

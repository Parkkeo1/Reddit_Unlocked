#
# -To be used for locally (localhost) testing the web server/website.
# -Installing the flask package on a virtual environment (instead of system-wide)
# is recommended by Flask devs.
#
# http://flask.pocoo.org/docs/0.12/quickstart/#
#
# -Isaac Park, keonp2
#


from flask import Flask, request, render_template, redirect, url_for, session
from run_praw import display_praw, stats_praw


app = Flask(__name__)
app.config['SECRET_KEY'] = '\x00\xe3~\xa1\xfc.2\x86\xc8\xb1J\xd9\x8e@2\xaf\xcb\x99\x86\xce\xed\x0b\xc8\xe0'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'basic-url' in request.form:
            name = request.form['basic-url']
            info = stats_praw(name)
            output = display_praw(name)
            session['info'] = info
            session['output'] = output
            return redirect(url_for('program', name=name))
        else:
            return render_template('home.html')
            # TODO: Implement subreddit input validity checking AKA Fix blank input error
    else:
        return render_template('home.html')


@app.route('/docs/<section>')
def docs(section):
    if section == "findings":
        return render_template("docs_findings.html")
    else:
        if section == "team":
            return render_template("docs_team.html")
        else:
            if section == "tools":
                return render_template("docs_tools.html")
            else:
                return "This docs page does not exist. Maybe it was a typo? <br><br> -Isaac <br><br><a href='/'>Back to Reddit_Unlocked Home</a>"
                # TODO: if I have time, implement html template for page DNE message


@app.route('/program/<name>')
def program(name):
    output = session.get('output')
    info = session.get('info')
    return render_template('program.html', name=name, output=output, info=info)


@app.route('/examples')
def examples():
    return render_template('examples.html')


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

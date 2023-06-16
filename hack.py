# Flask server to test this out
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import urllib
import json

app = Flask(__name__)
def qp(u):
    if isinstance(u, str):
        return urllib.parse.quote_plus(u)
    return ""
app.jinja_env.filters['quote_plus'] = qp


@app.route("/", methods=["GET", "POST"])
def hello():
    try:
        foo = request.form['foo']
    except:
        foo = None
    if isinstance(foo, str):
        # save foo to the MD file to pick up later
        open("foo.md", "w").write(foo)
    else:
        # if foo is None or empty string, try to read the MD file
        try:
            R = open("foo.md", "r").read()
            foo = urllib.parse.quote(R)
        except:
            foo = None
    return render_template('index.html', value=foo, note="1")

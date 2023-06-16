# Flask server to test this out
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/note', methods=['GET', 'POST'])
def note():
    foo = request.form['foo']
    if not foo:
        # if foo is None or empty string, try to read the MD file
        try:
            foo = open("foo.md", "r").read()
        except:
            pass
    else:
        # save foo to the MD file to pick up later
        open("foo.md", "w").write(foo)
    return render_template('index.html', value=foo, note="1")

import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'


app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<member>")
def member_page(member):
    path = '{}/{}'.format(POST_DIR, member)
    post = flatpages.get_or_404(path)
    return render_template('member.html', post=post)

@app.route("/projects")
def projects_page():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

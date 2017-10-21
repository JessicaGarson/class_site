import sys
import markdown
from flask import Flask, render_template, Markup

DEBUG = True
EXTENSION = '.md'
MD_DIR = 'content'



app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<member>")
def member_page(member):
    path = '{}/{}'.format(MD_DIR, member + EXTENSION)
    f = open(path, 'r')
    member_md = f.read()

    content = Markup( markdown.markdown( member_md ) )
    return render_template('member.html', **locals() )

@app.route("/projects")
def projects_page():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

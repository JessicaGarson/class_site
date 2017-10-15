import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

class Members():
    '''Ultimately, we should sub this out for a database of some kind.
    Rather than have a unique html file for each member, we can have one
    page called member.html, and use templates that call info from the
    database'''

    include = {
        'misha': 'misha.html',
        'kai': 'kai.html',
        'alice': 'alice.html',
        'dean': 'dean.html',
        'isobel': 'isobel.html',
        'sarah': 'sarah.html',
        'ana': 'ana.html',
        }


@app.route("/")
def index():
    return render_template('base.html')

@app.route("/<member>")
def member_page(member):
    if member not in Members.include.keys():
        return render_template('base.html')
    else:
        return render_template(Members.include[member])


if __name__ == "__main__":
    app.run(debug=True, port=5000)

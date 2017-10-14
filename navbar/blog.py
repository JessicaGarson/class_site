import sys
from flask import Flask, render_template


DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

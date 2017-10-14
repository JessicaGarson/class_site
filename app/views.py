from flask import Flask, render_template, request, url_for
from . import app

@app.route('/')
def index():
    return render_template('map3.html')

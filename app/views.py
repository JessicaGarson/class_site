from flask import Flask, render_template, request, url_for
from . import app

@app.route('/')
def index():
    return render_template('map3.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/<member>')
def memberpage(member):
    if member in members:
        return render_template(url_for( member ))
    else:
        return 'Member not found'

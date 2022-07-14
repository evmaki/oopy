""" This module implements a Flask app which allows server-side documents to be remotely
opened, written to, and saved.
"""
from flask import Flask, current_app, request

app = Flask(__name__)

# responds to HTTP GET at the site root by returning the static index.html file
@app.route('/', methods=['GET'])
def index():
    # current_app assumes static files are in ./static/ folder
    return current_app.send_static_file('index.html')

@app.route('/document/', methods=['POST'])
def edit_file():
    # TODO unpack the form inputs passed via the HTTP POST request and use them to edit the document.
    # HINT request.form.get() is your friend.

    # TODO return the edited document as a string.
    return ''
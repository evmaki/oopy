""" This module implements a Flask app which allows server-side documents to be remotely
opened, written to, and saved.

Note: This is for demo purposes only. In practice, this way of doing things is risky. 
You are taking unsanitized input from the web and using it to do file i/o (open, edit, 
and save files) in the filesystem of the backend. Be very careful with this sort of thing.
"""
from flask import Flask, current_app, request
import FileChooser

app = Flask(__name__)

# responds to HTTP GET at the site root by returning the static index.html file
@app.route('/')
def index():
    # current_app assumes static files are in ./static/ folder
    return current_app.send_static_file('index.html')

@app.route('/document/', methods=['POST'])
def edit_file():
    # unpack the form inputs passed via the HTTP POST request and use them to edit the document.
    document = FileChooser.open(f'./{request.form.get("path")}')
    document.append({'state': request.form.get('state'), 'capital': request.form.get('capital')})
    document.save()

    return str(document)
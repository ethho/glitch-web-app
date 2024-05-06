import os
from pathlib import Path
from flask import Flask, jsonify, render_template, request

# We can import from our custom package here
import glitch_web_app

template_folder = str(Path('templates').absolute())
app = Flask(__name__, template_folder=template_folder)


# unlike express, static files are automatic: http://flask.pocoo.org/docs/0.12/quickstart/#static-files

# http://flask.pocoo.org/docs/0.12/quickstart/#routing
# http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates
@app.route('/')
def hello():
    return render_template('index.html')

# Simple in-memory store
dreams = [
  'Find and count some sheep',
  'Climb a really tall mountain',
  'Wash the dishes',
]

@app.route('/dreams', methods=['GET'])
def get_dreams():
    return jsonify(dreams)

# could also use the POST body instead of query string: http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
@app.route('/dreams', methods=['POST'])
def add_dream():
    dreams.append(request.args.get('dream'))
    return ''


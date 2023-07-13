from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "icanttellyou"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submission')
def test_run():
    state = request.args.get('state')
    url = f'https://api.openbrewerydb.org/v1/breweries?by_state={state}'
    response = requests.get(url)
    data = response.json()
    return data

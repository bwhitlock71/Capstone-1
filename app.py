from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "icanttellyou"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('home.html')

"""I was able to get the route below this to work correctly but I am having trouble with the second one down. It returns an empty list and I can't seem to get it to work."""

# @app.route('/submission')
# def test_run():
#     state = request.args.get('state')
#     url = f'https://api.openbrewerydb.org/breweries?by_state={state}&per_page=5'
#     response = requests.get(url)
#     brewery_info = response.json()
#     return render_template('list.html', brewery_info=brewery_info)


@app.route('/submission')
def test_run():
    state = request.args.get('state')
    city = request.args.get('city')
    url = f'https://api.openbrewerydb.org/breweries?by_city={city}&by_state={state}&per_page=5'
    response = requests.get(url)
    brewery_info = response.json()
    return render_template('list.html', brewery_info=brewery_info)

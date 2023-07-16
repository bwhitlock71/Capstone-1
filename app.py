from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import SearchForm
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "icanttellyou"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# @app.route('/')
# def home():
#     return render_template('home.html')

"""I was able to get the route below this to work correctly but I am having trouble with the second one down. It returns an empty list and I can't seem to get it to work."""

# @app.route('/submission', methods=['GET', 'POST'])
# def test_run():
#     state = request.args.get('state')
#     city = request.args.get('city')
#     url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&by_state={state}'
#     response = requests.get(url)
#     if response.status_code != 200:
#         flash("No results :(", "Please try again")
#         return render_template('base.html')
#     brewery_info = response.json()
#     return render_template('list.html', brewery_info=brewery_info)
    
    
@app.route('/search', methods=['GET'])
def search_route():
    form = SearchForm()

    if form.validate_on_submit():
        city = form.city.data
        state = form.state.data
        url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&by_state={state}'
        response = requests.get(url)
        brewery_info = response.json()
        return render_template('search.html', brewery_info=brewery_info)
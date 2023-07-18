from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import SearchForm, SpecificForm
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "icanttellyou"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route('/', methods=['GET', 'POST'])
def search_route():
    form = SearchForm()

    if form.validate_on_submit():
        city = form.city.data
        state = form.state.data
        url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&by_state={state}'
        response = requests.get(url)
        if response.status_code != 200:
            flash("No results :( Please try again")
            return render_template('base.html')
        brewery_info = response.json()
        return render_template('home.html', form=form, brewery_info=brewery_info)
    

    return render_template('home.html', form=form)


@app.route('/type', methods=['GET', 'POST'])
def type_of_route():
    form = SpecificForm()

    
    if form.validate_on_submit():
        city = form.city.data
        state = form.state.data
        category = form.category.data
        url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&by_state={state}&by_type={category}'
        response = requests.get(url)
        if response.status_code != 200:
            flash("No results :( Please try again")
            return render_template('base.html')
        brewery_info = response.json()
        return render_template('specific.html', form=form, brewery_info=brewery_info)
    

    return render_template('specific.html', form=form)
from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import SearchForm, SpecificForm, UserAddForm, LoginForm, Ratings
from models import db, connect_db, User, Reviews

import requests
import os

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATA_BASE_URL")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.app_context().push()

debug = DebugToolbarExtension(app)
connect_db(app)

@app.before_request
def add_user_to_g():

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None


def do_login(user):

    session[CURR_USER_KEY] = user.id


def do_logout():


    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

# Returns the signup page for new users to register.
@app.route('/signup', methods=["GET", "POST"])
def signup():

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)

# Returns the login page for registered users.
@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit(): 
        user = User.authenticate(form.username.data, 
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():

    do_logout()

    flash("You have logged out.")
    return redirect("/login")

# Returns the home page with the search form present.
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

# Search that allows the user to filter their results by the selected fields.
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

# Returns random brewery.
@app.route('/random', methods=['GET', 'POST'])
def random():
    url = f'https://api.openbrewerydb.org/v1/breweries/random'
    response = requests.get(url)
    brewery_info = response.json()
    return render_template('random.html', brewery_info=brewery_info)

# Returns the review page for user to fill out.
@app.route('/review', methods= ['GET', 'POST'])
def review():

    brewery_id = request.args.get('brewery_id')
    url = f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}"
    response = requests.get(url)
    brewery_info = response.json()
    form = Ratings()

    if not g.user:
        flash("Please signup to leave reviews")
        return redirect('/signup')
    if request.method == 'POST':
        print(str(request.form))
        rating = Reviews(rating=form.rating.data, comments=form.comments.data, brewery_id=form.brewery_id.data, brewery_name=form.brewery_name.data, user_reviews=g.user.id)
        db.session.add(rating)
        db.session.commit()
        flash("Success, your review has been added to the reviews page")
    return render_template('users/review.html', brewery_info=brewery_info, form=form)

# Returns all reviews by all users.
@app.route('/pastreviews', methods=['GET', 'POST'])
def show_reviews():

    reviews = Reviews.query.all()
    return render_template('/pastreviews.html', reviews=reviews)




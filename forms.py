from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Length, Email

# Login form that is for the function on line 75 in app.py.
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

# Form for the signup function on line 47 in app.py.
class UserAddForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    
# Search form the search funciton on line 103 app.py.
class SearchForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])

# Specific form for the function on line 122 in app.py.
class SpecificForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    category = RadioField('Type:', 
                           choices=[('micro', 'Mirco- Most craft breweries. For example, Samual Adams is still considered a micro brewery.'), ('nano', 'Nano- An extremely small brewery which typically only distributes locally.'), ('brewpub', 'Brewpub- A beer-focused restaurant or restaurant/bar with a brewery on-premise.'), ('bar', 'Bar- A bar. No brewery equipment on premise.')]
                           )
# Form for the review function on line 150 in app.py.
class Ratings(FlaskForm):
    rating = RadioField('Rating', validators=[DataRequired()],
                         choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5','5')])
    comments = StringField('Comments', validators=[DataRequired()])
    brewery_id = HiddenField()
    brewery_name = HiddenField()
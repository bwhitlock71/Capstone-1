from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserAddForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    

class SearchForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])


class SpecificForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    category = RadioField('Type:', 
                           choices=[('micro', 'Mirco- Most craft breweries. For example, Samual Adams is still considered a micro brewery.'), ('nano', 'Nano- An extremely small brewery which typically only distributes locally.'), ('brewpub', 'Brewpub- A beer-focused restaurant or restaurant/bar with a brewery on-premise.'), ('bar', 'Bar- A bar. No brewery equipment on premise.')]
                           )
    
class Reviews(FlaskForm):
    rating = SelectField('Rating', validators=[DataRequired()])
    comments = StringField('Comments', validators=[DataRequired()])
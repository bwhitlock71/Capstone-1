from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])


class SpecificForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    category = RadioField('Type:', 
                           choices=[('micro', 'Mirco- Most craft breweries. For example, Samual Adams is still considered a micro brewery.'), ('nano', 'Nano- An extremely small brewery which typically only distributes locally.'), ('brewpub', 'Brewpub- A beer-focused restaurant or restaurant/bar with a brewery on-premise.'), ('bar', 'Bar- A bar. No brewery equipment on premise.')]
                           )
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    city = StringField('City')
    state = StringField('State')
    
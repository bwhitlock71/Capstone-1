from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )


    password = db.Column(
        db.Text,
        nullable=False,
    )

class Brewery(db.model):

    __tablename__ = 'brewery'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

class Reviews(db.model):

    __tablename__ = 'reviews'

    id = db.Column(
        db.Integer,
        primary_key=True
    )









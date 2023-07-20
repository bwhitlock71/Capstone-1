from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.Text, nullable=False,unique=True)
    username = db.Column( db.Text, nullable=False,unique=True)
    password = db.Column(db.Text, nullable=False)

    reviews = db.relationship('Reviews')

    @classmethod
    def signup(cls, username, email, password):

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(username=username, email=email, password=hashed_pwd)

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False



class Brewery(db.Model):

    __tablename__ = 'brewery'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)



class Reviews(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    brewery = db.Column(db.Integer, db.ForeignKey('brewery.id'))
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(150), nullable=False)


    user = db.relationship('User', backref='reviews')
    brewery = db.relationship('Brewery', backref='reviews')


def connect_db(app):

    db.app = app
    db.init_app(app)






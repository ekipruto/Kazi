from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime, default=func.now())

    #Relationships
    #cart_items = db.relationship('Cart', backref=db.backref('users', lazy=True))
    #orders = db.relationship('Order', backref=db.backref('users', lazy=True))

    @property
    def password(self):
        raise AttributeError('Password is not a readable Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    def __str__(self):
        return '<Users %r>' % Users.id
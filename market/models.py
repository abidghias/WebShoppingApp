from flask_sqlalchemy import SQLAlchemy
from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin
from flask import Flask

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
   # apps = db.relationship('Apps', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items


class Apps(db.Model):
    __tablename__ = 'Apps'
    AppId = db.Column(db.Integer(), primary_key=True)
    App = db.Column(db.String(length=90),    unique=True,primary_key=True)
    Category = db.Column(db.String(length=50),    unique=False)
    Rating = db.Column(db.String(length=50),    unique=False)
    Reviews = db.Column(db.String(length=50),    unique=False)
    Size = db.Column(db.String(length=50),    unique=False)
    Installs = db.Column(db.String(length=50),    unique=False)
    Type = db.Column(db.String(length=50),   unique=False)
    Price = db.Column(db.String(length=50),   unique=False)
    Content_Rating =db.Column(db.String(length=50),   unique=False)
    Genres = db.Column(db.String(length=50),   unique=False)
    Last_uploaded = db.Column(db.String(length=50),  unique=False)
    Current_Ver = db.Column(db.String(length=50),   unique=False)
    Android_Ver = db.Column(db.String(length=50), unique=False)
    
    def __repr__(self):
        return '<App %r>' % self.App


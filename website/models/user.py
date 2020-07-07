from datetime import datetime
from flask_login import UserMixin
from flask import Flask, current_app
from website.routes import get_db
db = get_db()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)


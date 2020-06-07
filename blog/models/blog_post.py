from datetime import datetime
from flask_login import UserMixin
from flask import Flask, current_app
from ..routes import get_db
db = get_db()

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(80), unique=True, nullable=False)
    blog_author = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, unique=True, nullable=False)
    blog_content = db.Column(db.Text,nullable=False)
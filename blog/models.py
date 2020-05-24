from datetime import datetime
from flask_login import UserMixin
from blog import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(80), unique=True, nullable=False)
    blog_author = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, unique=True, nullable=False)
    blog_content = db.Column(db.Text,nullable=False)
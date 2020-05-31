from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from blog.info.info import info
from blog.recepies.recepies import recepies_blueprint
from blog.general.general import general
from blog.auth.auth import *

mail = Mail()
app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(info)
app.register_blueprint(recepies_blueprint)
app.register_blueprint(general)

# Add bootstrap to the website
Bootstrap(app)

app.secret_key = os.environ.get('SECRET_KEY')

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
mail.init_app(app)

# Blog Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLITE_URI')
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from blog import app, db, bcrypt, mail
from datetime import datetime
from blog.forms import ContactForm, RegistrationForm, LoginForm
from models import User, BlogPost
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import os

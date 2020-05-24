from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from general_blueprint.general import general_blueprint
from authentication_blueprint.auth import auth_blueprint
from recepies_blueprint.recepies import recepies_blueprint
from blog_blueprint.blog import blog_blueprint
from contact_blueprint.contact import contact_blueprint
from about_blueprint.about import about_blueprint


mail = Mail()
app = Flask(__name__)
app.register_blueprint(general_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(recepies_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(contact_blueprint)
app.register_blueprint(about_blueprint)

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

from blog import routes
import os
from flask import Flask
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

def get_db():
    return SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    ac = AppConfig(app)
    app = ac.app_config()
    db = get_db()
    db.init_app(app)
    with app.app_context():
        app = ac.add_blueprints()  # Import routes
        return app

class AppConfig():
    def __init__(self, app):
        self.app = app
    
    def app_config(self):
        self.app.config["MAIL_SERVER"] = "smtp.gmail.com"
        self.app.config["MAIL_PORT"] = 465
        self.app.config["MAIL_USE_SSL"] = True
        self.app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
        self.app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
        self.app.secret_key = os.environ.get('SECRET_KEY')
        mail = Mail()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLITE_URI')
        mail.init_app(self.app)
        # Add bootstrap to the website
        Bootstrap(self.app)
        return self.app 

    def add_blueprints(self):
        from general_blueprint.general import general_blueprint
        from authentication_blueprint.auth import auth_blueprint
        from recepies_blueprint.recepies import recepies_blueprint
        from blog_blueprint.blog import blog_blueprint
        from contact_blueprint.contact import contact_blueprint
        from about_blueprint.about import about_blueprint
        self.app.register_blueprint(general_blueprint)
        self.app.register_blueprint(auth_blueprint)
        self.app.register_blueprint(recepies_blueprint)
        self.app.register_blueprint(blog_blueprint)
        self.app.register_blueprint(contact_blueprint)
        self.app.register_blueprint(about_blueprint)
        login_manager = LoginManager(self.app)
        login_manager.login_view = 'login'
        login_manager.login_message_category = 'info'
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        return self.app
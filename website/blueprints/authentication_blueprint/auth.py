from flask import Blueprint, render_template, request
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from website.forms.contact_form import ContactForm
from website.forms.registration_form import RegistrationForm
from website.forms.login_form import LoginForm
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from datetime import datetime
from website.routes import bcrypt, get_db
from website.models.user import *

auth_blueprint = Blueprint('auth_blueprint', __name__, 
                                        template_folder='templates',
                                        static_folder='static',
                                        static_url_path='/website.blueprints.auth_blueprint.static')

@auth_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth_blueprint.logIn'))
    return render_template('signup.html', title='Register', form=form)

@auth_blueprint.route("/login", methods=['GET', 'POST'])
def logIn():
    if current_user.is_authenticated:
        return redirect(url_for('general_blueprint.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('general_blueprint.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth_blueprint.route("/logout")
def logOut():
    logout_user()
    return redirect(url_for('general_blueprint.home'))

from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from datetime import datetime
from blog.forms import ContactForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import os

recepies_blueprint = Blueprint('recepies_blueprint', __name__,
                         template_folder='templates',
                         static_folder='static')

@recepies_blueprint.route("/recepies")
def recepies():
    return render_template("recepies.html") 

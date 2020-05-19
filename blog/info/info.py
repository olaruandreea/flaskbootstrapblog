from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from datetime import datetime
from blog.forms import ContactForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import os

info = Blueprint('info', __name__,
                         template_folder='templates',
                         static_folder='static')

@info.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')

@info.route('/contactme', methods=['GET','POST'])
def contactMe():
    form = ContactForm()  
    
    if request.method == 'POST':

        if form.validate() == False:
            return render_template('contactme.html', form=form)
        else:
            message = Message(sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_USERNAME')])
            message.body = "Name: " + form.name.data + '\n' + "Email: " + form.email.data + '\n' +  "Message: " + form.message.data
            mail.send(message)
            return render_template('contactme.html', success=True)
    
    elif request.method == 'GET':
        return render_template('contactme.html', form=form)

@info.route("/faqs")
def faqs():
    return render_template("faqs.html") 


from flask import Blueprint, render_template, request
from flask_mail import Mail, Message
from website.forms.contact_form import ContactForm
import os
from website.routes import mail

contact_blueprint = Blueprint('contact_blueprint', __name__,
                                                template_folder='templates',
                                                static_folder='static',
                                                static_url_path='/website.blueprints.contact_blueprint.static')

@contact_blueprint.route('/contactme', methods=['GET','POST'])
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


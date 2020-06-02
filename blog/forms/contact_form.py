from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError,StringField, PasswordField, SubmitField, BooleanField

class ContactForm(FlaskForm):
    name = TextField("NAME", validators=[DataRequired("Please enter your name")])
    email = TextField("EMAIL", validators=[DataRequired("Please enter your email address."), Email()])
    message = TextAreaField("MESSAGE", validators=[DataRequired("Please enter a message")])
    submit = SubmitField("SUBMIT")
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError,StringField, PasswordField, SubmitField, BooleanField


class ContactForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired("Please enter your name")])
    email = TextField("Email", validators=[DataRequired("Please enter your email address."), Email()])
    message = TextAreaField("Message", validators=[DataRequired("Please enter a message")])
    submit = SubmitField("Send")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
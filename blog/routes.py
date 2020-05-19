from blog import app, db, bcrypt, mail
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from datetime import datetime
from blog.forms import ContactForm, RegistrationForm, LoginForm
from blog.models import User, BlogPost
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import os

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addpost', methods=['GET','POST'])
def addPost():
    if request.method == 'POST':
        title = request.form['blogTitle']
        author = request.form['blogAuthorName']
        content = request.form['blogContent']

        blog_post = BlogPost(blog_title=title, blog_author=author, blog_content=content, date_posted=datetime.now())
       
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('displayPost', post_id=blog_post.id))
    else:
        return render_template('/admin/addpost.html')

@app.route('/blog')
def displayBlog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<post_id>')
def displayPost(post_id):
    # get the last post in the database
    post = BlogPost.query.filter_by(id=post_id).one()
    return render_template('blogpost.html', post=post)

@app.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')

@app.route('/contactme', methods=['GET','POST'])
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

@app.errorhandler(404) 
def notFound(e): 
    return render_template("/errors/404.html") 

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('logIn'))
    return render_template('/admin/signup.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def logIn():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('/admin/login.html', title='Login', form=form)

@app.route("/logout")
def logOut():
    logout_user()
    return redirect(url_for('home'))

@app.route("/recepies")
def recepies():
    return render_template("recepies.html") 

@app.route("/faqs")
def faqs():
    return render_template("faqs.html") 


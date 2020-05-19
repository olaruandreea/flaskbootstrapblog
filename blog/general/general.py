from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import Flask, abort, flash, Markup, redirect, flash, render_template,request, Response, session, url_for
from datetime import datetime
from blog.forms import ContactForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import os

general = Blueprint('general', __name__,
                         template_folder='templates',
                         static_folder='static')

@general.route('/')
def home():
    return render_template("home.html")

@general.route('/addpost', methods=['GET','POST'])
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
        return render_template('addpost.html')

@general.route('/blog')
def displayBlog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@general.route('/blog/<post_id>')
def displayPost(post_id):
    # get the last post in the database
    post = BlogPost.query.filter_by(id=post_id).one()
    return render_template('blogpost.html', post=post)


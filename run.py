from flask import Flask, abort, flash, Markup, redirect, flash
from flask import render_template,request, Response, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime
from forms import ContactForm, RegistrationForm, LoginForm
from flask_mail import Mail, Message
import os

mail = Mail()
app = Flask(__name__)

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


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(80), unique=True, nullable=False)
    blog_author = db.Column(db.String(120), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, unique=True, nullable=False)
    blog_content = db.Column(db.Text,nullable=False)

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
        return render_template('addpost.html')

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

@app.route('/signup')
def signUp():
    return render_template('signup.html')

@app.route('/login')
def logIn():
    return render_template('login.html')

@app.route('/contactme',methods=['GET','POST'])
def contactMe():
    form = ContactForm()  
    
    if request.method == 'POST':

        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contactme.html', form=form)
        else:
            msg = Message(form.subject.data, sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_USERNAME')])
            msg.body = """
            From: %s &lt;%s&gt;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
        return render_template('contactme.html', success=True)
    
    elif request.method == 'GET':
        return render_template('contactme.html', form=form)

@app.errorhandler(404) 
def notFound(e): 
    return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)
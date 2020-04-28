from flask import Flask, abort, flash, Markup, redirect
from flask import render_template,request, Response, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
Bootstrap(app)

# Blog Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/olaru/coding/blog/blog.db'
db = SQLAlchemy(app)



class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(80), unique=True, nullable=False)
    blog_author = db.Column(db.String(120), unique=True, nullable=False)
    blog_content = db.Column(db.Text)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addpost', methods=['GET','POST'])
def addPost():
    if request.method == 'POST':
        title = request.form['blogTitle']
        return redirect(url_for('displayPost', post_title=title))
    else:
        return render_template('addpost.html')

@app.route('/blog')
def displayBlog():
    return "my blog page"

@app.route('/blog/<post_title>')
def displayPost(post_title):
    return post_title

@app.route('/aboutme')
def aboutMe():
    return render_template('aboutme.html')

@app.route('/signup')
def signUp():
    return render_template('aboutme.html')


if __name__ == '__main__':
    app.run(debug=True)
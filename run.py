from flask import Flask, abort, flash, Markup, redirect, render_template,request
from flask_sqlalchemy import SQLAlchemy, Response, session, url_for
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
def addpost():
    blog_title = request.form.get('inputTitle')
    blog_author = request.form.get('blogAuthor')
    blog_content = request.form.get('blogContent')
    print blog_title
    print blog_author
    print blog_content
    return render_template('addpost.html')

@app.route('/blog', methods=['GET'])
def displayblog():

    return render_template('blog.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)
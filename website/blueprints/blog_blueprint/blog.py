from flask import Blueprint, render_template, request, redirect, url_for, Flask
from datetime import datetime
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from website.routes import bcrypt, get_db
from website.models.blog_post import BlogPost

blog_blueprint = Blueprint('blog_blueprint', __name__, 
                                        template_folder='templates',
                                        static_folder='static',
                                        static_url_path='/website.blueprints.blog_blueprint.static')

@blog_blueprint.route('/addpost', methods=['GET','POST'])
def addPost():
    if request.method == 'POST':
        title = request.form['blogTitle']
        author = request.form['blogAuthorName']
        content = request.form['blogContent']

        blog_post = BlogPost(blog_title=title, blog_author=author, blog_content=content, date_posted=datetime.now())
        db = get_db()
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('blog_blueprint.displayPost', post_id=blog_post.id))
    else:
        return render_template('addpost.html')

@blog_blueprint.route('/blog')
def displayBlog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@blog_blueprint.route('/blog/<post_id>')
def displayPost(post_id):
    # get the last post in the database
    post = BlogPost.query.filter_by(id=post_id).one()
    return render_template('blogpost.html', post=post)

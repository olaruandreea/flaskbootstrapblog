from blog import *
from blog.models.user import *
from blog.models.blog_post import *

def create_db():
    app = create_app()
    with app.app_context():
        db.create_all()


create_db()
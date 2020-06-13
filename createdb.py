from website import *
from website.models.user import *
from website.models.blog_post import *

def create_db():
    app = create_app()
    with app.app_context():
        db.create_all()


create_db()
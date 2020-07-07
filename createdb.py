from website.routes import create_app, get_db

def create_db():
    app = create_app()
    with app.app_context():
        db = get_db()
        from website.models.user import User
        from website.models.blog_post import BlogPost
        db.create_all()


create_db()
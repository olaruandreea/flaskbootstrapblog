import sys
import os
sys.path.append('..')
from config import TestConfig
from flask_testing import TestCase
from blog import create_app, get_db
import unittest
from flask_mail import Mail, Message
 
class BasicTests(unittest.TestCase):
 
    def setUp(self):
        app = create_app()
        app.config.from_object(TestConfig())
        self.app = app.test_client()
        with app.app_context():
            db = get_db()
            db.drop_all()
            db.create_all()

        mail = Mail()
        mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    def tearDown(self):
        pass
 
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_aboutme_page(self):
        response = self.app.get('/aboutme', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_contactme_page(self):
        response = self.app.get('/contactme', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_faqs_page(self):
        response = self.app.get('/faqs', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_addpost_page(self):
        response = self.app.get('/addpost', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_make_unique_nickname(self):
        u = User(nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        u = User(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname
if __name__ == "__main__":
    unittest.main()
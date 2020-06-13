import sys
import os
import unittest
sys.path.append('..')
from blog import app
from config import TestConfig
from forms.contact_form import ContactForm


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfig())
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

   

if __name__ == '__main__':
    unittest.main()
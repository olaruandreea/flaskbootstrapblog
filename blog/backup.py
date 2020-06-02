'''https://realpython.com/python-web-applications-with-flask-part-iii/'''
from flask_testing import TestCase
import sys
sys.path.append('..')
from blog import create_app, get_db
import unittest
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app = create_app()
        # app.config.from_object(TestConfig())

       
        self.app = app.test_client()
        with app.app_context():

            db = get_db()
            db.drop_all()
            db.create_all()
 
        self.assertEqual(app.debug, True)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()


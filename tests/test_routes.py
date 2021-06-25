import unittest
from unittest.mock import patch


import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from main import create_app, db
from main.models import Pokemon
from main.config import config


class RoutesTest(unittest.TestCase):
	def setUp(self):
		self.app = create_app(config['testDB'])
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		self.client = self.app.test_client(use_cookies=True)

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_home_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		bad_response = self.client.get('/some_page')
		self.assertEqual(bad_response.status_code, 404)


if __name__ == '__main__':
	unittest.main()

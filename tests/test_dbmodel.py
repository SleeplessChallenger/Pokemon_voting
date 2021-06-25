import unittest
from unittest.mock import patch


import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from main import create_app, db
from main.models import Pokemon
from main.config import config


class PokemonTest(unittest.TestCase):
	def setUp(self):
		self.app = create_app(config['testDB'])
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		self.pokemon = Pokemon(nickname='Charmeleon', superPower='Fire',
							   rating=4, poll_id=1)
		db.session.add(self.pokemon)
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_repr(self):
		self.assertEqual(repr(self.pokemon), 'Charmeleon with Fire')

	def test_poll_id(self):
		self.assertEqual(self.pokemon.poll_id, 1)

	@patch('main.models.Pokemon.current_results')
	def test_serialize(self, mock_oblect):
		mock_oblect.return_value = {
			'nickname': 'Charmeleon',
			'rating': 4
		}
		self.assertEqual(mock_oblect.return_value, {
			'nickname': self.pokemon.nickname,
			'rating': self.pokemon.rating
		})


if __name__ == '__main__':
	unittest.main()

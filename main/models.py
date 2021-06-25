from main import db
from flask_login import UserMixin
from flask import current_app, url_for
from sqlalchemy.orm import column_property


class Pokemon(db.Model, UserMixin):
	__tablename__ = 'pokemons'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(25), unique=True, nullable=False)
	superPower = db.Column(db.String(30), nullable=False)
	rating = db.Column(db.Integer, default='0')
	poll_id = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"{self.nickname} with {self.superPower}"

	@property
	def serialize(self):
		return {
			'id': self.id,
			'nickname': self.nickname,
			'superPower': self.superPower,
			'rating': self.rating,
			'poll_id': self.poll_id
		}

	@property
	def current_results(self):
		return {
			'nickname': self.nickname,
			'rating': self.rating
		}

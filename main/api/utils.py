from main.models import Pokemon
from main import db
from sqlalchemy import desc


def populate_db():
	db.create_all()
	data_poll_one = Pokemon.query.filter_by(poll_id=1).first()
	data_poll_two = Pokemon.query.filter_by(poll_id=2).first()

	if data_poll_one is None:
		p1 = Pokemon(nickname='Pikachu', superPower='Fire')
		p2 = Pokemon(nickname='Charizard', superPower='Blaze')
		p3 = Pokemon(nickname='Persian', superPower='Limber')
		db.session.add(p1)
		db.session.add(p2)
		db.session.add(p3)
		db.session.commit()
		return {'message': 'First poll was created, second one is available'}

	elif data_poll_two is None:
		p1 = Pokemon(nickname='Wartortle', superPower='Water', poll_id=poll_num)
		p2 = Pokemon(nickname='Metapod', superPower='Bug', poll_id=poll_num)
		p3 = Pokemon(nickname='Oddish', superPower='Grass', poll_id=poll_num)
		db.session.add(p1)
		db.session.add(p2)
		db.session.add(p3)
		db.session.commit()
		return {'message': 'Second poll was created, cannot create new polls'}

	return {'message': "You've already created 2 polls"}

def get_results(output, poll_id=1):
	if type(poll_id) is not int or poll_id > 2:
		return {'message': 'Unknown code value!'}
	if output == 'allData':
		# get all data from the table in `desc` order
		data = Pokemon.query.order_by(Pokemon.rating.desc()).all()
		return [p.serialize for p in data]
	elif output == 'result_poll':
		# get only results in `desc` order
		data = Pokemon.query.filter_by(poll_id=poll_id).order_by(Pokemon.rating.desc()).all()
		return [p.current_results for p in data]		

def give_error():
	return {'message': 'Check id/nickname'}

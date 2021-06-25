from flask import (Blueprint, render_template, url_for,
				   request, current_app, redirect)
from main.models import Pokemon
from main import db
from main.form import PokemonChoice
from sqlalchemy import desc
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

main_pokemons = Blueprint('main', __name__)


@main_pokemons.before_app_first_request
def populate_db():
	with open(os.path.join(APP_STATIC, 'cache.txt')) as file:
		poll_num = int(file.read())

	db.create_all()

	if poll_num > 2:
		return

	if poll_num == 1:
		p1 = Pokemon(nickname='Pikachu', superPower='Fire', poll_id=poll_num)
		p2 = Pokemon(nickname='Charizard', superPower='Blaze', poll_id=poll_num)
		p3 = Pokemon(nickname='Persian', superPower='Limber', poll_id=poll_num)
	elif poll_num == 2:
		p1 = Pokemon(nickname='Wartortle', superPower='Water', poll_id=poll_num)
		p2 = Pokemon(nickname='Metapod', superPower='Bug', poll_id=poll_num)
		p3 = Pokemon(nickname='Oddish', superPower='Grass', poll_id=poll_num)
	
	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.commit()

	with open(os.path.join(APP_STATIC, 'cache.txt'), 'w') as file:
		file.write(str(poll_num+1))

@main_pokemons.route('/createPoll', methods=['GET', 'POST'])
@main_pokemons.route('/', methods=['GET', 'POST'])
def about():
	form = PokemonChoice()
	if form.validate_on_submit():
		pokemon = Pokemon.query.filter_by(nickname=form.pokemon_options.data.nickname).first()
		pokemon.rating += 1
		db.session.commit()

		return redirect(url_for('main.results'))

	return render_template('poll.html', form=form)

@main_pokemons.route('/getResult')
def results():
	allPokemons = Pokemon.query.order_by(Pokemon.rating.desc()).all()
	return render_template('results.html', data=allPokemons)

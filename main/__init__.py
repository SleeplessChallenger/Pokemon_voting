from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.config import config
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=config['production']):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)

	from main.main_routes import main_pokemons
	app.register_blueprint(main_pokemons)
	

	from .api import api as pokemon_api
	app.register_blueprint(pokemon_api, url_prefix='/api')
	
	return app

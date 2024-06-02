from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from main.config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=config['production']):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from main.main_routes import main_pokemons
    # app.register_blueprint(main_pokemons)

    app.before_request_funcs[None].remove(main_pokemons)

    from .api import api as pokemon_api
    app.register_blueprint(pokemon_api, url_prefix='/api')

    return app

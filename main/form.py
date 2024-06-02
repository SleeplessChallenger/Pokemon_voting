from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField

from main.models import Pokemon


def pokemon_choice():
    return Pokemon.query


class PokemonChoice(FlaskForm):
    pokemon_options = QuerySelectField(query_factory=pokemon_choice, allow_blank=True,
                                       get_label='nickname')

from flask import jsonify, request

from main import db
from main.models import Pokemon
from . import api
from .utils import populate_db, get_results, give_error


@api.route('/createPoll', methods=['GET', 'POST'])
def create_poll():
    if request.method == 'GET':
        return jsonify(get_results('allData')), 201
    elif request.method == 'POST':
        return jsonify(populate_db()), 201


@api.route('/poll/<int:poll_id>', methods=['POST'])
def make_choice(poll_id):
    if poll_id > 2:
        return {'message': 'Choose between 1 or 2 poll'}

    nick = request.args.get('identifier', type=str)
    id_num = request.args.get('identifier', type=int)
    print(nick, id_num)

    if nick == '' and id_num == '':
        return jsonify(give_error())
    # to allow use either `id` or `nickname`
    # place `id_num` first as `nick` will be
    # not None if `id_num` is not None due
    # to query strings format being string

    pokemon = None
    if id_num or nick:
        pokemon = query_pokemon(id_num, nick, pokemon, poll_id)

        if pokemon is None:
            return jsonify(give_error())

        pokemon.rating += 1
        db.session.commit()
        return jsonify({'message': f"{pokemon.nickname} rating was increased!"})
    else:
        return jsonify({'message': 'Your input type was wrong, only int/str'})


def query_pokemon(id_num, nick, pokemon, poll_id):
    if id_num:
        pokemon = Pokemon.query.filter_by(
            poll_id=poll_id, id=id_num).first()
    else:
        pokemon = Pokemon.query.filter_by(
            poll_id=poll_id, nickname=nick).first()
    return pokemon


@api.route('/getResult/<int:poll_id>', methods=['GET'])
def results(poll_id):
    return jsonify(get_results('result_poll', poll_id)), 201

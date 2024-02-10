import datetime
import os
import pickle
from typing import Union

from app.game_file.models import GameFile as GameFileModel

from app import db
from app.game.game import Game


def get_games_dir():
    return os.path.abspath(os.getcwd()) + '/app/game/save_files'


def delete_game(code: str):
    filename = get_games_dir() + '/{}.pkl'.format(code)
    os.remove(filename)


def save_game(game: Game, code: str) -> str:
    filename = get_games_dir() + '/{}.pkl'.format(code)

    if not os.path.exists(get_games_dir()):
        os.makedirs(get_games_dir())

    with open(filename, 'wb') as f:
        pickle.dump(game, f, pickle.HIGHEST_PROTOCOL)

    with open(filename, 'rb') as f:
        data = f.read()
        existing_file = GameFileModel.query.filter_by(code="{}".format(code)).first()
        if existing_file is not None:
            existing_file.file = data
            existing_file.updated_at = datetime.datetime.now()
            db.session.commit()
        else:
            game_file = GameFileModel(file=data, updated_at=datetime.datetime.now(), code=code)
            db.session.add(game_file)
            db.session.commit()
    return code


def load_game(code: str) -> Union[Game, None]:
    file_details = GameFileModel.query.filter_by(code="{}".format(code)).first()
    filename = get_games_dir() + '/{}.pkl'.format(code)
    try:
        with open(filename, 'wb') as f1:
            f1.write(file_details.file)
        f = open(filename, 'rb')
        g = pickle.load(f)
        f.close()
        return g
    except:
        return None

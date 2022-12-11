from secrets import token_hex
from flask import Blueprint, render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user, login_required
from flask_socketio import join_room, send

from app import db, socketio
from app.game.game import Game
from app.game.utils import save_game, load_game
from app.game.models import Game as GameModel
from app.game.constants import PVP_MODE, STATUS_ACTIVE, STATUS_FINISHED
from app.game.fields import FIELDS
from app.game.forms import JoinGameForm
from app.models import User

game = Blueprint('game', __name__)

@game.route('/<user_id>')
@login_required
def home(user_id):
    if user_id == str(current_user.id):
        users_count = User.query.count()
        win = GameModel.query.filter_by(user_id=user_id, is_winner=True).count()
        loss = GameModel.query.filter_by(user_id=user_id, is_losser=True).count()
        return render_template('game/home.html', users_count=users_count, win=win, loss=loss)
    else:
        flash("error!", 'danger')
        users_count = User.query.count()
        return render_template('game/home.html', users_count=users_count)
@game.route('/')
def logout():
    users_count = User.query.count()
    return render_template('game/home.html', users_count=users_count)


@game.route('/menu')
def menu():
    return render_template('game/menu.html')

@game.route('/field_info/<field_id>')
def field_info(field_id):
    if current_user.__dict__ != {}:
        field_id = int(field_id)
        field_data = None
        for field in FIELDS:
            if field['id'] == field_id:
                field_data = field

        if not field_data:
            return make_response('not found'), 404

        return make_response(field_data), 200
    else:
        return redirect(url_for('auth.login'))

@game.route('/init_pvp')
def init_pvp():
    code = token_hex(16)
    g = Game(2, current_user.id)
    save_game(g, code)

    game_record = GameModel(code=code, user_id=current_user.id, mode=PVP_MODE, isHost=True)
    db.session.add(game_record)
    db.session.commit()

    return redirect(url_for('game.waiting_room', code=code))


@game.route('/waiting_room/<code>', methods=['POST', 'GET'])
def waiting_room(code):
    if request.method == 'POST':
        partner_has_joined: bool = bool(GameModel.query.filter_by(code=code, isHost=False).first())
        print(partner_has_joined)
        if partner_has_joined:
            game_record = GameModel.query.filter_by(code=code, isHost=True).first()
            game_record.status = STATUS_ACTIVE
            db.session.commit()
            return redirect(url_for('game.play_pvp', code=code))
        else:
            flash('You can not start the game, no player has joined.', 'danger')

    return render_template('game/waiting_room.html', code=code, is_host=True)


@game.route('/join_game', methods=['POST', 'GET'])
def join_game():
    form = JoinGameForm()
    if form.validate_on_submit():
        code = form.join_code.data
        game_records_count = GameModel.query.filter_by(code=code).count()
        if game_records_count == 1:
            g = load_game(code)
            g.pvp_add_joining_player(current_user.id)
            save_game(g, code)

            new_game_record = GameModel(code=code, user_id=current_user.id, mode=PVP_MODE)
            db.session.add(new_game_record)
            db.session.commit()
            return redirect(url_for('game.guest_waiting_room', code=code))
        else:
            flash('you can not join this game.', 'danger')

    return render_template('game/join_game.html', form=form)


@game.route('/guest_waiting_room/<code>', methods=['POST', 'GET'])
def guest_waiting_room(code):
    if request.method == 'POST':
        game_record = GameModel.query.filter_by(code=code, isHost=True).first()
        if game_record.status == STATUS_ACTIVE:
            return redirect(url_for('game.play_pvp', code=code))

    flash('now, wait for host to start the game.', 'primary')
    return render_template('game/waiting_room.html', is_host=False)


@game.route('/play_pvp/<code>', methods=['POST', 'GET'])
def play_pvp(code):
    payload = {
        'buy': bool(int(request.form.get('buy'))) if request.form.get('buy') else None,
        'build': request.form.get('build').split(';')[0:-1] if request.form.get('build') else None
    }
    g = load_game(code)
    if g.winner:
        save_game(g, code)
        if current_user.id == g.winner.db_id:
            GameModel.query.filter_by(code=code, user_id=current_user.id).update(dict(status=STATUS_FINISHED,
                                                                                      is_losser=True))
        else:
            GameModel.query.filter_by(code=code, user_id=current_user.id).update(dict(status=STATUS_FINISHED,
                                                                                      is_winner=True))
        db.session.commit()
        socketio.emit('game over', data={'msg': '{} won.'.format('You have' if current_user.id == g.winner.db_id else 'Enemy has')})
        flash('{} won.'.format('Enemy has' if current_user.id == g.winner.db_id else 'You have'))
        return redirect(url_for('game.home', user_id=current_user.id))
    if request.form.get('next_turn'):
        last_player = g.players[g.current_player_index].db_id
        g.next_turn(payload)
        if g.winner:
            socketio.emit('game over', data={
                'msg': '{} won.'.format('You have' if current_user.id == g.winner.db_id else 'Enemy has')})
            socketio.emit('refresh', data={'last_player': last_player}, broadcast=True)

            flash('{} won.'.format('Enemy has' if current_user.id == g.winner.db_id else 'You have'))

            save_game(g, code)
            if current_user.id == g.winner.db_id:
                GameModel.query.filter_by(code=code, user_id=current_user.id).update(dict(status=STATUS_FINISHED,
                                                                                          is_losser=True))
            else:
                GameModel.query.filter_by(code=code, user_id=current_user.id).update(dict(status=STATUS_FINISHED,
                                                                                          is_winner=True))
            db.session.commit()

            return redirect(url_for('game.home', user_id=current_user.id))
        save_game(g, code)
        socketio.emit('refresh', data={'last_player': last_player}, broadcast=True)

    is_active = current_user.id == g.players[g.current_player_index].db_id

    return render_template(
        'game/board/board.html',
        game=g, code=code,
        pvp=True,
        is_active=is_active
        )


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)

    send('', room=room)

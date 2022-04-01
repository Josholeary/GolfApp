from hashlib import sha256
from nis import cat
from operator import methodcaller
from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from .dbmodels import setgame,player
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        gamename = request.form.get('gamename')
        numholes = int(request.form.get('numholes'))
        spass = request.form.get('spass')
    
        if numholes > 18:
            flash('Maximum of 18 holes per course', category='error')
        elif len(spass) < 4:
            flash('Password must be greater than 4 characters', category='error')
        else:
            newgame = setgame(gamename = gamename, numholes=numholes, spass=generate_password_hash(spass, method='sha256'))
            db.session.add(newgame)
            db.session.commit()
            flash('Game created, join using session password', category='success')
            return redirect(url_for('auth.join_page'))
        

    return render_template('setup.html')

@auth.route('/join', methods=['GET', 'POST'])
def join_page():
    if request.method == 'POST':
        pname = request.form.get('pname')
        gamename = request.form.get('gamename')
        spass = request.form.get('spass')

        gameip = setgame.query.filter_by(gamename=gamename).first()
        if gameip:
            if check_password_hash(gameip.spass, spass):
                flash('Joined game', category='success')
                newplayer = player(pname=pname)
                db.session.add(newplayer)
                db.session.commit()
                return redirect(url_for('auth.game_page'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Game name does not exist', category='error')
    return render_template('join.html')

@auth.route('/game', methods=['GET', 'POST'])
def game_page():
    if request.method == 'POST':
        pname = request.form.get('pname')
        holenum = int(request.form.get('holenum'))
        newscore = int(request.form.get('score'))

        p_exists = player.query.filter_by(pname=pname).first()
        if p_exists:
            if not p_exists.score:
                p_exists.holenum = holenum
                p_exists.score = newscore
                db.session.commit()
            else:
                overall = newscore + p_exists.score
                p_exists.holenum = holenum
                p_exists.score = overall
                db.session.commit()
        else:
            flash('Player name not in session', category='error')


            
            

    players = player.query.all()
    return render_template('game.html', players=players)


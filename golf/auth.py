from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from .dbmodels import setgame
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        numholes = int(request.form.get('numholes'))
        spass = request.form.get('spass')
    
        if numholes > 18:
            flash('Maximum of 18 holes per course', category='error')
        elif len(spass) < 4:
            flash('Password must be greater than 4 characters', category='error')
        else:
            newgame = setgame(numholes=numholes, spass=spass)
            db.session.add(newgame)
            db.session.commit()
            flash('Game created', category='success')
            return redirect(url_for('views.homepage'))
        

    return render_template('setup.html')

@auth.route('/join', methods=['GET', 'POST'])
def join_page():
    return render_template('join.html')


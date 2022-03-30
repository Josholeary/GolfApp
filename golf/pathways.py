from crypt import methods
from wsgiref import validate
#pathways controls all routes to the different pages in the web app
from golf import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
from golf.dbmodels import setup, player
from golf import db

#Homepage route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#Set up game route
@app.route('/setup', methods=['GET','POST'])
def setup_page():
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        numholes = int(request.form.get('numholes'))
        spass = request.form.get('spass')
        
        if numholes > 18:
            flash('Maximum of 18 holes per course', category='error')
        elif len(spass) < 4:
            flash('Password must be greater than 4 characters', category='error')
        else:
            return render_template('game.html')

    return render_template('setup.html')

#Join game route
@app.route('/join', methods=['GET','POST'])
def join_page():
    return render_template('join.html')

@app.route('/game')
def game_page():
    return render_template('game.html')

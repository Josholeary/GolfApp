from golf import app
from flask import render_template
from golf.dbmodels import game
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html', num_players = 0)
from crypt import methods
from wsgiref import validate
#pathways controls all routes to the different pages in the web app
from golf import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from golf.dbmodels import setup, player
from golf.forms import SetupForm,JoinForm
from golf import db

#Homepage route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#Set up game route
@app.route('/setup', methods=['GET','POST'])
def setup_page():
    form = SetupForm()
    if form.validate_on_submit():
        setup_to_create = setup(host_name=form.host_name.data,
                                 num_holes=form.num_holes.data,
                                 session_password=form.session_password.data)
        db.session.add(setup_to_create)
        db.session.commit
        #return redirect(url_for('game'))
    if form.errors != {}:
        for errors in form.errors.values():
            flash(f'Error: {errors}')
    return render_template('setup.html', form=form)

#Join game route
@app.route('/join')
def join_page():
    form = JoinForm()
    if form.validate_on_submit():
        setup_to_create = setup(host_name=form.host_name.data,
                                 player_name=form.player_name.data,
                                 session_password=form.session_password.data)
        db.session.add(setup_to_create)
        db.session.commit
    return render_template('join.html', form=form)

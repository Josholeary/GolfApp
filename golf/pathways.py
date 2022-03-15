from crypt import methods
from wsgiref import validate
from golf import app
from flask import render_template, redirect, url_for
from golf.dbmodels import setup, player
from golf.forms import SetupForm
from golf import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
    return render_template('setup.html', form=form)

@app.route('/join')
def join_page():
    return render_template('join.html')

from golf import app
from flask import render_template
from golf.dbmodels import setup, player
from golf.forms import SetupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/setup')
def setup():
    form = SetupForm()
    return render_template('setup.html', form=form)

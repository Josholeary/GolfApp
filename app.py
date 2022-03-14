from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golf.db'
db=SQLAlchemy(app)

class game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    player_name = db.Column(db.String(length=40), nullable=False)
    hole = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer(), nullable=False)




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html', num_players = 0)



if __name__ == '__main__':
    app.run(debug=True)

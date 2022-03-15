from enum import unique
from golf import db
from enum import unique

class setup(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    session_code = db.Column(db.Integer(), nullable=False, unique=True)
    owner_name = db.Column(db.String(length=40), nullable=False)
    players = db.relationship('player', backref='joined_game', lazy=True)

class player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    player_name = db.Column(db.String(length=40), nullable=False)
    hole_num = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer(), nullable=False)
    joinCode = db.Column(db.Integer(), db.ForeignKey('setup.session_code'))

    def __repr__(self):
        return f'item {self.name}'
#dbmodels holds all the classes that create the database models for the site
from . import db
from flask_login import UserMixin

#Setup database model for setting up a game
class setgame(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    numholes = db.Column(db.Integer, nullable=False)
    spass = db.Column(db.String(length=20), nullable=False)
    players = db.relationship('player')

#player database model for every player in a game
class player(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    pname = db.Column(db.String(length=40), nullable=False)
    hole_num = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('setgame.id'))


    def __repr__(self):
        return f'item {self.name}'
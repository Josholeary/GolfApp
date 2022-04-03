#dbmodels holds all the classes that create the database models for the site
from . import db
from flask_login import UserMixin

#Setup database model for setting up a game
class setgame(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    gamename = db.Column(db.String(length=20), nullable=False)
    numholes = db.Column(db.Integer, nullable=False)
    spass = db.Column(db.String(length=20), nullable=False)
    players = db.relationship('User')

#player database model for every player in a game
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    pname = db.Column(db.String(length=40))
    holenum = db.Column(db.Integer)
    score = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('setgame.id'))


    def __repr__(self):
        return f'item {self.name}'
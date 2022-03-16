from enum import unique
#dbmodels holds all the classes that create the database models for the site
from golf import db
from enum import unique

#Setup database model for setting up a game
class setup(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    host_name = db.Column(db.String(length=40), nullable=False)
    num_holes = db.Column(db.Integer(), nullable=False)
    session_password = db.Column(db.String(length=20), nullable=False, unique=True)

#player database model for every player in a game
class player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    player_name = db.Column(db.String(length=40), nullable=False)

#Scorecard database for displaying the scorecard
class scorecard(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    hole_num = db.Column(db.Integer(), nullable=False)
    score = db.Column(db.Integer(), nullable=False)
    player_name = db.Column(db.String(), db.ForeignKey('player.player_name'))
    overall = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'item {self.name}'
from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golf.db'
app.config['SECRET_KEY'] = '1344dfa0b97b2fdbf50f85d7'
db=SQLAlchemy(app)

from golf import pathways
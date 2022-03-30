from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def homepage():
    return render_template('index.html')
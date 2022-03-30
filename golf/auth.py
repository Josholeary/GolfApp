from flask import Blueprint, render_template, request, flash, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        numholes = int(request.form.get('numholes'))
        spass = request.form.get('spass')
    
        if numholes > 18:
            flash('Maximum of 18 holes per course', category='error')
        elif len(spass) < 4:
            flash('Password must be greater than 4 characters', category='error')
        else:
            return render_template('game.html')

    return render_template('setup.html')

@auth.route('/join', methods=['GET', 'POST'])
def join_page():
    return render_template('join.html')


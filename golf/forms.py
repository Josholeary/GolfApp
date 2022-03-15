from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField

class SetupForm(FlaskForm):
    host_name = StringField(label='Host name:')
    num_holes = IntegerField(label='Number of holes to be played:')
    session_password = PasswordField(label='Set the Session Password:')
    submit = SubmitField(label='Begin Game')
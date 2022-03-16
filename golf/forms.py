#forms is responsible for all forms that will be filled out throughout the site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import Length, NumberRange, EqualTo, DataRequired

#form for the game setup page
class SetupForm(FlaskForm):
    host_name = StringField(label='Host name:', validators=[Length(min=1, max=40),DataRequired()])
    num_holes = IntegerField(label='Number of holes to be played:', validators=[NumberRange(min=1, max=18),DataRequired()])
    session_password = PasswordField(label='Set the Session Password:', validators=[Length(min=4, max=20),DataRequired()])
    submit = SubmitField(label='Begin Game')

#form for joining a game
class JoinForm(FlaskForm):
    host_name = StringField(label='Host name:')
    player_name = StringField(label='Player name:')
    session_password = PasswordField(label='Enter the Session Password:')
    submit = SubmitField(label='Begin Game')
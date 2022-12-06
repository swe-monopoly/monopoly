from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class JoinGameForm(FlaskForm):
    join_code = StringField('ENTER THE CODE TO JOIN', validators=[DataRequired()])
    submit = SubmitField('Join')

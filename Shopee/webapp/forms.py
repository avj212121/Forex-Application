from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# Register Form Skeleton; User enters currency rates for particular date which he/she wants to track
class RegisterRate(FlaskForm):
    date = StringField('Date')
    from_country = StringField('FromCountry', validators=[DataRequired()])
    to_country = StringField('ToCountry', validators=[DataRequired()])
    rate = StringField('Rate')
    submit = SubmitField('Submit')

# Track Form Skeleton; User enters date to track the currency rates on that given date
class TrackRate(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Enter')

# Delete Form Skeleton; User enters currency he/she no longer wants to track
class DeleteRate(FlaskForm):
    from_country = StringField('FromCountry', validators=[DataRequired()])
    to_country = StringField('ToCountry', validators=[DataRequired()])
    submit = SubmitField('Submit')
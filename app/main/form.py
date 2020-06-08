from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a few biographical facts about yourself.',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Mystery','Mystery'),('Thriller','Thriller'),('Romance','Romance')],validators=[Required()])
    submit = SubmitField('Post')
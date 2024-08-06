from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    image = FileField('Upload an Image', validators=[DataRequired()])
    submit = SubmitField('Upload')

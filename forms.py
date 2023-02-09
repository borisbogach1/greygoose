from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class SugForm(FlaskForm):
    input1 = StringField('1', validators=[DataRequired()])
    input1 = StringField('1', validators=[DataRequired()])
    input1 = StringField('1', validators=[DataRequired()])
    input1 = StringField('1', validators=[DataRequired()])
    submit = SubmitField('Создать маршрут')



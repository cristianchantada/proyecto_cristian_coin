from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class purchaseForm(FlaskForm):
    
    from_sell = FloatField("From", validators=[DataRequired()])
    to_buy = FloatField("to", validators=[DataRequired()])
    q_buy = FloatField("Q", validators=[DataRequired()])
    calc_submit = SubmitField()
    accept_submit = SubmitField()
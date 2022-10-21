from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired
from config import ACCEPTED_COINS
from flask_wtf import FlaskForm

class PurchaseForm(FlaskForm):   
    moneda_from = SelectField("Vender :", choices= ACCEPTED_COINS, validate_choice=True, validators=[DataRequired()])
    moneda_to = SelectField("Comprar :", choices= ACCEPTED_COINS, validate_choice=True, validators=[DataRequired()])
    quantity_from = FloatField("Cantidad a vender :", validators=[DataRequired()])
    quantity_to = FloatField("Cantidad que compro :")
    unitary_prize = FloatField("Precio Unitario: ")
    date = StringField("Fecha :")
    time = StringField("Hora :")

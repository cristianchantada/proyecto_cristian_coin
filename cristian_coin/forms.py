from flask_wtf import FlaskForm
from config import ValidationError
from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired

def min_quantity_from_value(form, field):
    if field.data <= 0:
        raise ValidationError("El valor de la cantidad a vender debe ser mayor de cero")

class PurchaseForm(FlaskForm):
    
    moneda_from = SelectField("Vender", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True, validators=[DataRequired()])
    moneda_to = SelectField("Comprar", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True, validators=[DataRequired()])
    quantity_from = FloatField("Cantidad a vender", validators=[DataRequired(), min_quantity_from_value])
    quantity_to = FloatField("Cantidad que compro", validators=[])
    unitary_prize = FloatField("Precio Unitario", validators=[])
    date = StringField("Fecha", validators=[])
    time = StringField("Hora", validators=[])

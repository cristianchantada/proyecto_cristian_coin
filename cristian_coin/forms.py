from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired

class PurchaseForm(FlaskForm):
    
    moneda_from = SelectField("Vender", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    moneda_to = SelectField("Comprar", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    quantity_from = FloatField("Cantidad a vender", validators=[DataRequired()])
    quantity_to = FloatField("Cantidad que compro", validators=[])
    unitary_prize = FloatField("Precio Unitario", validators=[])

class ValidationForm(FlaskForm):
    
    moneda_from_validated = StringField("Vender")
    moneda_to_validated = StringField("Comprar")
    quantity_from_validated = FloatField("Cantidad a vender", validators=[])
    quantity_to_validated = FloatField("Cantidad que compro", validators=[])
    unitary_prize_validated = FloatField("Precio Unitario", validators=[])




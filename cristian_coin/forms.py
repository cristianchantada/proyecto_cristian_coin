from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired

class PurchaseForm(FlaskForm):
    
    moneda_from = SelectField("Vender", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    moneda_to = SelectField("Comprar", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    quantity_from = FloatField("Cantidad a vender", validators=[DataRequired()])
    quantity_to = FloatField("Cantidad que compro", validators=[])
    unitary_prize = FloatField("Precio Unitario", validators=[])

    class ValidationForm(FlaskForm):
    
    moneda_from = SelectField("Vender", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    moneda_to = SelectField("Comprar", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True)
    quantity_from = FloatField("Cantidad a vender", validators=[DataRequired()])
    quantity_to = FloatField("Cantidad que compro", validators=[])
    unitary_prize = FloatField("Precio Unitario", validators=[])




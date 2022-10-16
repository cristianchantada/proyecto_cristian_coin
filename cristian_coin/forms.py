from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired

class PurchaseForm(FlaskForm):
    
    moneda_from = SelectField("Vender", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True, validators=[DataRequired()])
    moneda_to = SelectField("Comprar", choices=["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"], validate_choice=True, validators=[DataRequired()])
    quantity_from = FloatField("Cantidad a vender", validators=[DataRequired()])
    quantity_to = FloatField("Cantidad que compro", validators=[])
    unitary_prize = FloatField("Precio Unitario", validators=[])
    date = StringField("Fecha", validators=[])
    time = StringField("Hora", validators=[])

class ValidationForm(FlaskForm):
    moneda_from = StringField("Validación vender", validators=[])
    moneda_to = StringField("Validación comprar", validators=[])
    quantity_from = FloatField("Validación cantidad a vender", validators=[])
    quantity_to = FloatField("Validación antidad que compro", validators=[])
    unitary_prize = FloatField("Valicdación precio Unitario", validators=[])
    date = StringField("Fecha", validators=[])
    time = StringField("Hora", validators=[])

    # validators.NumberRange(min=0, max=0, mensaje=ninguno)



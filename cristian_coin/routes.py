from cristian_coin import app
from flask import render_template, request
from cristian_coin.models import select_all
from cristian_coin.forms import PurchaseForm

@app.route("/")
def index():
    consult_all = select_all()
    return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)

@app.route("/purchase")
def coin_operation():
    operation = PurchaseForm
    if request.method == "GET":
        return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
    else:
        pass

@app.route("/status")
def wallet_status():
    return render_template("status.html", pageTitle= "Monedero")


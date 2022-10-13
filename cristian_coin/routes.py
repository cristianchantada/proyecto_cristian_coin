from cristian_coin import app
from flask import render_template, request
from cristian_coin.models import select_all, choose_my_coins, dict_moneda_from
from cristian_coin.forms import PurchaseForm

@app.route("/")
def index():
    consult_all = select_all()
    return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)

@app.route("/purchase", methods=["GET", "POST"])
def coin_operation():
    operation = PurchaseForm()
    if request.method == "GET":
        return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
    else:
        all_my_dict_coins = choose_my_coins()
        my_dict_coin = dict_moneda_from(operation.data["moneda_to"], all_my_dict_coins )
        precio_unitario = 1 / my_dict_coin["rate"]
        return render_template("operations.html", pageTitle= "Compra", operation_form= operation, unitary_prize= precio_unitario)

        #, quantity= cantidad, unitary_prize= precio_unitario

@app.route("/status")
def wallet_status():
    return render_template("status.html", pageTitle= "Monedero")

@app.route("/pruebas")
def pruebas():
    my_coins = choose_my_coins()
    return my_coins


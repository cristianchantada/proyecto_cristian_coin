from cristian_coin import app
from flask import render_template, request
from cristian_coin.models import select_all, choose_my_coins, dict_moneda
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
    elif request.method == "POST": 
        all_my_dict_coins = choose_my_coins()
        my_dict_coin_to = dict_moneda(operation.data["moneda_to"], all_my_dict_coins )
        my_dict_coin_from = dict_moneda(operation.data["moneda_from"], all_my_dict_coins )
        
        convers_eur_coin_to = 1 / my_dict_coin_to["rate"]
        convers_eur_coin_from = 1 / my_dict_coin_from["rate"]
        cantidad_to = convers_eur_coin_from / convers_eur_coin_to

        return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity= cantidad_to, unitary_prize=convers_eur_coin_from)

@app.route("/status")
def wallet_status():
    return render_template("status.html", pageTitle= "Monedero")

@app.route("/pruebas")
def pruebas():
    my_coins = choose_my_coins()
    return my_coins


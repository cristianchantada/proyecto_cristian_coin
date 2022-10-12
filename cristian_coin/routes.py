from cristian_coin import app
from flask import render_template, request
from cristian_coin.models import select_all
from cristian_coin.forms import purchaseForm

@app.route("/")
def index():
    consult_all = select_all()
    return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)

@app.route("/purchase")
def coin_operation():
    if request.method == "GET":
        operation_form = purchaseForm
        return render_template("operations.html", operation_form= operation_form)
    else:
        pass


from cristian_coin.models import commit_operation, select_all, calculate, my_wallet, secure_operation, validation_on_server
from flask import render_template, request, flash, redirect, url_for
from cristian_coin.forms import PurchaseForm
from config import ACCEPTED_COINS
from cristian_coin import app
import sqlite3

@app.route("/")
def index():
    try:
        consult_all = select_all()
        return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return render_template("index.html", pageTitle= "Error en la base de datos")

@app.route("/purchase", methods=["GET", "POST"])
def coin_operation():
    operation = PurchaseForm()
    
    if request.method == "GET":      
        return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
    else:
        if request.form["enviar"] == "calculate":
            try:
                form_validated = validation_on_server(operation.data)
                if form_validated == False:
                    return render_template("operations.html", pageTitle= "compra", operation_form= operation)
                else:             
                    result = calculate(operation.data["moneda_from"], operation.data["moneda_to"], operation.data["quantity_from"])
                    return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity_to= result["quantity_to"], unitary_prize= result["unitary_prize"], date = result["date"], time= result["time"])

            except sqlite3.Error as e:
                flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
                return render_template("operations.html", pageTitle= "Error en la base de datos", operation_form= operation)
                
        if request.form["enviar"] == "validate":
            try:            
                comprobation = secure_operation(operation.data)

                if comprobation and operation.validate():
                        commit_operation(operation.data)
                        if operation.data["moneda_from"] == "EUR":
                            flash("Enhorabuena, la operación de compra de nada por dinero real ha sido realizada con exito.")
                        else:
                            flash("La operación de compra de monedas ha sido realizada con éxito.")

                        return redirect(url_for("index"))
                else:
                    flash("La operación de compra a realizar no ha sido calculada o bien no coincide con los valores calculados previamente. Por favor, recalcule de nuevo para validar la operación correctamente.")
                    return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
            except sqlite3.Error as e:
                flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
                return render_template("operations.html", pageTitle= "Eror en la base de datos", operation_form= operation)

@app.route("/status")
def wallet_status():
    try:
        wallet_value = my_wallet()
        beneficio = wallet_value["total_crypto_value"] - wallet_value["purchase_value"]
        return render_template("status.html", pageTitle= "Monedero", wallet_value= wallet_value, beneficio= beneficio)
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return render_template("status.html", pageTitle= "Monedero", wallet_value = {})

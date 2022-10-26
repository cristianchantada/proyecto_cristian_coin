from cristian_coin.models import commit_operation, select_all, calculate, my_wallet, secure_operation, validation_on_server
from flask import render_template, request, flash, redirect, url_for
from cristian_coin.forms import PurchaseForm
from cristian_coin import app
import sqlite3

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
        if request.form["enviar"] == "calculate":
            form_validated = validation_on_server(operation.data)
            if form_validated == False:
                return render_template("operations.html", pageTitle= "compra", operation_form= operation)
            else:             
                result = calculate(operation.data["moneda_from"], operation.data["moneda_to"], operation.data["quantity_from"])
                if result == {}:
                    return render_template("operations.html", pageTitle= "compra", operation_form= operation)
                else:
                    return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity_to= result["quantity_to"], unitary_prize= result["unitary_prize"], date = result["date"], time= result["time"])
                
        if request.form["enviar"] == "validate":         
                comprobation = secure_operation(operation.data)
                if comprobation != {}:
                    if comprobation and operation.validate():
                        ok = commit_operation(operation.data)
                        if ok:
                            if operation.data["moneda_from"] == "EUR":
                                flash("Enhorabuena, la operación de compra de nada por dinero real ha sido realizada con exito.")
                            else:
                                flash("La operación de compra de monedas ha sido realizada con éxito.")

                            return redirect(url_for("index"))
                        else:
                            return render_template("operations.html", pageTitle= "Eror en la base de datos", operation_form= operation)
                    else:
                        flash("La operación de compra a realizar no ha sido calculada o bien no coincide con los valores calculados previamente. Por favor, recalcule de nuevo para validar la operación correctamente.")
                        return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
                else:
                    return render_template("operations.html", pageTitle= "Eror en la base de datos", operation_form= operation)

@app.route("/status")
def wallet_status():
        wallet_value = my_wallet()
        if wallet_value != {}:
            beneficio = wallet_value["total_crypto_value"] - wallet_value["purchase_value"]
            return render_template("status.html", pageTitle= "Monedero", wallet_value= wallet_value, beneficio= beneficio)
        else:
            return render_template("status.html", pageTitle= "Monedero", wallet_value = {})

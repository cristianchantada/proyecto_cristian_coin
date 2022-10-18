import sqlite3
from cristian_coin import app
from config import ACCEPTED_COINS
from flask import render_template, request, flash, redirect, url_for
from cristian_coin.models import commit_operation, select_all, calculate, my_wallet, secure_operation
from cristian_coin.forms import PurchaseForm

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
                # Falta arreglar parte de "el formulario está siendo alterado"

                if not operation.data["moneda_from"] in ACCEPTED_COINS or not operation.data["moneda_to"] in ACCEPTED_COINS or operation.data["quantity_from"] <= 0 or (operation.data["quantity_to"] or operation.data["unitary_prize"] or operation.data["date"] or operation.data["time"]) != None or operation.data["moneda_from"] == operation.data["moneda_to"]:
                    if not operation.data["moneda_from"] in ACCEPTED_COINS:
                        flash("Solo puede operar con las monedas incluidas en el selector de 'Vender'; seleccione una de ellas para continuar con el proceso de compra.")
                    if not operation.data["moneda_to"] in ACCEPTED_COINS:
                        flash("Solo puede comprar monedas incluidas en el selector de 'Comprar'; seleccione una de ellas para continuar con el proceso de compra.")
                    if operation.data["quantity_from"] <= 0:
                        flash("La cantidad de divisas a vender tiene que ser positiva.")
                    if operation.data["quantity_to"] or operation.data["unitary_prize"] or operation.data["date"] or operation.data["time"] != None:
                        flash("El formulario de compra está siendo alterado desde el navegador y se ha denegado la operación solicitada; refresque la página e inténtelo de nuevo, contestándo únicamente a lo que se le pregunta.")
                    if operation.data["moneda_from"] == operation.data["moneda_to"]:
                        flash("La moneda a vender y la moneda a comprar deben ser distintas.")

                    return render_template("operations.html", pageTitle= "compra", operation_form= operation)

                else:             
                    result = calculate(operation.data["moneda_from"], operation.data["moneda_to"], operation.data["quantity_from"])
                    return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity_to= result["quantity_to"], unitary_prize= result["unitary_prize"], date = result["date"], time= result["time"])
            except sqlite3.Error as e:
                flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
                return render_template("operations.html", pageTitle= "Error en la base de datos", operation_form= operation)
                
        if request.form["enviar"] == "validate":
            try:

                # Aquí hay que volver a realizar validación grande que está arriba en el primer "post" con "validate" (Ahora creo que ya no hace falta porque con la operación de secure_operation si alteras alguno ya no permite)

                comprobation = secure_operation(operation.data)

                if comprobation and operation.validate():
                        commit_operation(operation.data)
                        flash("La operación de compra de monedas ha sido realizada con éxito")
                        return redirect(url_for("index"))
                else:
                    flash("La operación de compra a realizar no ha sido calculada o bien no coincide con los valores calculados. Por favor, recalcule de nuevo para validar la operación correctamente.")
                    return render_template("operations.html", pageTitle= "Compra", operation_form= operation)
            except sqlite3.Error as e:
                flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
                return render_template("operations.html", pageTitle= "Eror en la base de datos", operation_form= operation)



@app.route("/status")
def wallet_status():
    try:
        wallet_value = my_wallet()
        return render_template("status.html", pageTitle= "Monedero", wallet_value= wallet_value)
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return render_template("status.html", pageTitle= "Monedero", wallet_value = {})

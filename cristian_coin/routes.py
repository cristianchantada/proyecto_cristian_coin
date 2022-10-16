from cristian_coin import app
from flask import render_template, request, flash, redirect, url_for
from cristian_coin.models import commit_operation, select_all, calculate, my_wallet, secure_operation
from cristian_coin.forms import PurchaseForm, ValidationForm

@app.route("/")
def index():
    consult_all = select_all()
    return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)

@app.route("/purchase", methods=["GET", "POST"])
def coin_operation():
    operation = PurchaseForm()
    validation = ValidationForm()
    
    if request.method == "GET":      
        return render_template("operations.html", pageTitle= "Compra", operation_form= operation, validation_form= validation)
    else:
        if request.form["enviar"] == "calculate":         
            result = calculate(operation.data["moneda_from"], operation.data["moneda_to"], operation.data["quantity_from"])
            quantity_to = result["quantity_to"]
            unitary_prize = result["unitary_prize"]

            return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity_to= quantity_to, unitary_prize= unitary_prize, moneda_from_v=operation.data["moneda_from"], moneda_to_v= operation.data["moneda_to"], quantity_from_v= operation.data["quantity_from"],  validation_form = validation, date = result["date"], time= result["time"])

        if request.form["enviar"] == "validate":

            comprobation = secure_operation(operation.data)

            

            if operation.data == validation.data:
                if operation.validate():
                    commit_operation(validation.data)
                    flash("La operación de compra de monedas ha sido realizada con éxito")
                    return redirect(url_for("index"))
                else:
                    pass
                
            else:
                flash("La operación de compra a realizar no coincide con los valores calculados. Por favor, recalcule de nuevo para validar la operación correctamente.")

                return render_template("operations.html", pageTitle= "Compra", operation_form= operation, quantity_to= quantity_to, unitary_prize= unitary_prize)


@app.route("/status")
def wallet_status():
    wallet_value = my_wallet()
    return render_template("status.html", pageTitle= "Monedero")
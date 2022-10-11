from cristian_coin import app
from flask import render_template
from cristian_coin.models import select_all

@app.route("/")
def index():
    consult_all = select_all()
    return render_template("index.html", pageTitle= "Índice", consult_all= consult_all)
from config import API_KEY, DATA_BASE, URL_COINAPI_IO_EXCHANGERATE, ACCEPTED_COINS
from werkzeug import exceptions
from datetime import datetime
from requests import get
from flask import flash
import sqlite3

def db_select_fetchall(query):
    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute(query)
    all_rows = cur.fetchall()
    con.close()
    return all_rows

def db_delete(query):
    con =sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()

def db_insert_antihack(query, secret_values_query): 
    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute(query, secret_values_query)
    con.commit()
    con.close()

def coinapi_io_connect(crypto_base, crypto_quote):
    result = get(URL_COINAPI_IO_EXCHANGERATE.format(crypto_base, crypto_quote, API_KEY))
    if result.status_code != 200:
        raise ServerConectionError(f"Ramón, has cambiado el API_KEY o la URL de coinapi.io en 'config.py'; por favor, devuelve dichas constantes a sus valores originales. Si no ha sido así, se trataría de un error 'real', tipificado como:\n\nError en la consulta de los valores de divisas: código de estado de respuesta HTTP {result.status_code}. Por favor, reinténtelo de nuevo más tarde.")
    return result.json()

def calculate(coin_from, coin_to, quantity_from):
    if coin_from != "EUR":
        try:
            max_cripto =db_select_fetchall(f"SELECT sum(cantidad_to) FROM operations_table WHERE moneda_to = '{coin_from}'")
            max_cripto = max_cripto[0][0]

            if max_cripto == None:
                max_cripto = 0
            if quantity_from > max_cripto:
                raise MaxCriptoError(f"No dispone de suficientes criptomonedas '{coin_from}' para realizar la operación. Su máximo en cartera de {coin_from} son {max_cripto}.\nSi desea vender todas sus divisas, copie la cantidad y péguela en 'cantidad de moneda a vender' en el formulario de operaciones anterior.")
        except sqlite3.Error as e:
            flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
            return {}

    result = coinapi_io_connect(coin_from, coin_to)
    quantity_to = quantity_from * result["rate"]
    unitary_prize = quantity_from / quantity_to

    date = datetime.now().isoformat()[:10]
    time = datetime.now().isoformat()[11:19]

    try:
        db_delete("DELETE FROM stand_by_operation_table;")
        db_insert_antihack("INSERT INTO stand_by_operation_table (moneda_from, quantity_from, moneda_to, quantity_to, date, time, unitary_prize) VALUES (?,?,?,?,?,?,?)", (coin_from, quantity_from, coin_to, quantity_to, date, time, unitary_prize))
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return {}
        
    result ={"quantity_to": quantity_to  , 'unitary_prize': unitary_prize, "date": date, "time": time }
    
    return result

def secure_operation(dict_validated_operation):

    try:
        saved_operation = db_select_fetchall("SELECT moneda_from, quantity_from, moneda_to, quantity_to, date, time, unitary_prize FROM stand_by_operation_table;")
        db_delete("DELETE FROM stand_by_operation_table;")
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return {}

    if not saved_operation:
        return False
    if saved_operation[0] == (dict_validated_operation["moneda_from"], dict_validated_operation["quantity_from"], dict_validated_operation["moneda_to"],dict_validated_operation["quantity_to"], dict_validated_operation["date"], dict_validated_operation["time"], dict_validated_operation["unitary_prize"]):
        return True
    return False 

def select_all():
    try:
        selection = db_select_fetchall("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, unitary_prize FROM operations_table;")
        return selection
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return {}

def commit_operation(values_dict):
    try:
        db_insert_antihack("INSERT INTO operations_table (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, unitary_prize) VALUES (?,?,?,?,?,?,?)", (values_dict["date"], values_dict["time"], values_dict["moneda_from"], values_dict["quantity_from"], values_dict["moneda_to"], values_dict["quantity_to"], values_dict["unitary_prize"]))
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return False
    return True

def my_wallet():
    try:
        investment_eur = db_select_fetchall("SELECT sum(cantidad_from) FROM operations_table WHERE moneda_from = 'EUR'")
        recovered_eur = db_select_fetchall("SELECT sum(cantidad_to) FROM operations_table WHERE moneda_to = 'EUR'")
    except sqlite3.Error as e:
        flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
        return {}

    invest = investment_eur[0][0]
    recover = recovered_eur[0][0]
    
    if invest == None:
        invest = 0
    if recover == None:
        recover = 0

    purchase_value = invest - recover

    crypto_values = { "BTC": 0, "ETH": 0, "USDT": 0, "BNB": 0, "XRP": 0, "ADA": 0, "SOL": 0, "DOT": 0, "MATIC": 0}

    for crypto in crypto_values:
        try:
            result_this_crypto_to = db_select_fetchall(f"SELECT sum(cantidad_to) FROM operations_table WHERE moneda_to = '{crypto}'")
            result_this_crypto_from = db_select_fetchall(f"SELECT sum(cantidad_from) FROM operations_table WHERE moneda_from = '{crypto}'")
        except sqlite3.Error as e:
            flash(f"Se ha producido un error en la base de datos ({e}). Por favor, contacte con el administrador o reinténtelo más tarde.")
            return {}
        
        result_this_coin_to = result_this_crypto_to[0][0]
        result_this_coin_from = result_this_crypto_from[0][0] 

        if result_this_coin_to == None:
            result_this_coin_to = 0
        if result_this_coin_from == None:
            result_this_coin_from = 0

        result_this_crypto = result_this_coin_to - result_this_coin_from

        crypto_values[crypto]= result_this_crypto
        
        if crypto_values[crypto] != 0:
            result = coinapi_io_connect(crypto, "EUR")
            crypto_values[crypto] = crypto_values[crypto] * result["rate"]

    total_crypto_value = 0
    for cantidad_misma_cripto in crypto_values.values():
        total_crypto_value += cantidad_misma_cripto
        
    all = {"investment_eur": invest, "recovered_eur": recover, "purchase_value": purchase_value, "total_crypto_value": total_crypto_value}

    return all

def validation_on_server(operation_data):
    if not operation_data["moneda_from"] in ACCEPTED_COINS or not operation_data["moneda_to"] in ACCEPTED_COINS or operation_data["quantity_from"] <= 0 or operation_data["moneda_from"] == operation_data["moneda_to"]:
        if not operation_data["moneda_from"] in ACCEPTED_COINS:
            flash("Solo puede operar con las monedas incluidas en el selector de 'Vender'.")
            flash("Seleccione una de ellas para continuar con el proceso de compra.")
        if not operation_data["moneda_to"] in ACCEPTED_COINS:
            flash("Solo puede comprar monedas incluidas en el selector de 'Comprar'.")
            flash("Seleccione una de ellas para continuar con el proceso de compra.")
        if operation_data["quantity_from"] <= 0:
            flash("La cantidad de divisas a vender tiene que ser positiva.")
        if operation_data["moneda_from"] == operation_data["moneda_to"]:
            flash("La moneda a vender y la moneda a comprar deben ser distintas.")
        return False
    return True

class MaxCriptoError(exceptions.HTTPException):
    code = 418
    pass

class ServerConectionError(exceptions.HTTPException):
    code = 401
    pass
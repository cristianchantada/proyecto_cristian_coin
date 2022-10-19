from config import API_KEY, DATA_BASE, MaxCriptoError
import sqlite3
from requests import get
from datetime import datetime

def calculate(coin_from, coin_to, quantity_from):

    if coin_from != "EUR":
        con = sqlite3.connect(DATA_BASE)
        cur = con.cursor()
        cur.execute("SELECT sum(cantidad_to) FROM operations_table WHERE moneda_to = ?", (coin_from,))
        max_cripto = cur.fetchone()
        con.close()
        max_cripto = max_cripto[0]

        if quantity_from > max_cripto:
            raise MaxCriptoError(f"No dispone de suficientes criptomonedas '{coin_from}' para realizar la operación. Su máximo en cartera de {coin_from} son {max_cripto}")


    result = get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(coin_from, coin_to, API_KEY))

    if result.status_code != 200:
        raise Exception(f"Error en la consulta de los valores da divisas: {result.status_code}. Por favor, reinténtelo de nuevo más tarde.")

    result = result.json()

    quantity_to = quantity_from * result["rate"]
    unitary_prize = quantity_from / quantity_to

    hora_aquí = datetime.now().isoformat()
    result["time"] = hora_aquí


    date = hora_aquí[:10]
    time = hora_aquí[11:19]

    con =sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("DELETE FROM stand_by_operation_table;")
    con.commit()
    con.close()

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("INSERT INTO stand_by_operation_table (moneda_from, quantity_from, moneda_to, quantity_to, date, time, unitary_prize) VALUES (?,?,?,?,?,?,?)", (coin_from, quantity_from, coin_to, quantity_to, date, time, unitary_prize))

    con.commit()
    con.close()

    result ={"quantity_to" : quantity_to  , 'unitary_prize': unitary_prize, "date": date, "time": time }
    
    return result

def secure_operation(dict_validated_operation):

    con =sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT moneda_from, quantity_from, moneda_to, quantity_to, date, time, unitary_prize FROM stand_by_operation_table;")

    save_operation = cur.fetchone()

    con.close()

    tuple_validated_operation = (dict_validated_operation["moneda_from"], dict_validated_operation["quantity_from"], dict_validated_operation["moneda_to"],dict_validated_operation["quantity_to"], dict_validated_operation["date"], dict_validated_operation["time"], dict_validated_operation["unitary_prize"])

    con =sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("DELETE FROM stand_by_operation_table;")
    con.commit()
    con.close()

    if save_operation == tuple_validated_operation:
        return True
    return False 

def select_all():

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, unitary_prize FROM operations_table;")

    selection = cur.fetchall()

    con.close()

    return selection

def commit_operation(values_dict):

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("INSERT INTO operations_table (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, unitary_prize) VALUES (?,?,?,?,?,?,?)", (values_dict["date"], values_dict["time"], values_dict["moneda_from"], values_dict["quantity_from"], values_dict["moneda_to"], values_dict["quantity_to"], values_dict["unitary_prize"]))

    con.commit()
    con.close()

def my_wallet():
    
    # Cálculo de lo invertido en €:

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT sum(cantidad_from) FROM operations_table WHERE moneda_from = 'EUR'")
    investment_eur = cur.fetchall()
    con.close()

    # Cálculo de lo recuperado en €:

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT sum(cantidad_to) FROM operations_table WHERE moneda_to = 'EUR'")
    recovered_eur = cur.fetchall()
    con.close()

    # Cálculo del valor de compra (invertido en € - recuperado en €)

    invest = investment_eur[0][0]
    recover = recovered_eur[0][0]
    purchase_value = invest - recover

    # Calculando el valor actual del wallet con la suma de todas las cryptomonedas, cantidad y precio actual:


    ##crypto_values = { "BTC": 0, "ETH": 0, "USDT": 0, "BNB": 0, "XRP": 0, "ADA": 0, "SOL": 0, "DOT": 0, "MATIC": 0}

    crypto_values = { "BTC": 0, "ETH": 0}

    for crypto in crypto_values:
        con = sqlite3.connect(DATA_BASE)
        cur = con.cursor()
        cur.execute("SELECT ((Select sum(cantidad_to) FROM operations_table WHERE moneda_to = ?) - (select sum(cantidad_from) FROM operations_table WHERE moneda_from = ?))", (crypto, crypto))

        result_this_crypto = cur.fetchall()
        result_this_crypto = result_this_crypto[0][0]

        
        crypto_values[crypto]= result_this_crypto 
        con.close()

        # Revisar si "EUR" y crypto están bien colocadas:

        result = get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(crypto, API_KEY))

        if result.status_code != 200:
            raise Exception(f"Error en la consulta de los valores de divisas: código de estado de respuesta HTTP {result.status_code}. Por favor, reinténtelo de nuevo más tarde.")

        result = result.json()
        
        crypto_values[crypto] = crypto_values[crypto] * result["rate"]

        # Iteración para sumar todos los valores de las distintas cryptos:

    total_crypto_value = 0

    for cantidad_misma_cripto in crypto_values.values():
        total_crypto_value += cantidad_misma_cripto
        
    all = {"investment_eur": invest, "recovered_eur": recover, "purchase_value": purchase_value, "total_crypto_value": total_crypto_value}

    return all
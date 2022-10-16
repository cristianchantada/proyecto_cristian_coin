from config import API_KEY, DATA_BASE
import sqlite3
from requests import get

def calculate(coin_from, coin_to, quantity_from):
    result = get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(coin_from, coin_to, API_KEY))
    result = result.json()
    result_eur_rate = get("https://rest.coinapi.io/v1/exchangerate/EUR/{}?apikey={}".format(coin_from, API_KEY))
    result_eur_rate = result_eur_rate.json()

    quantity_to = quantity_from / result["rate"]
    unitary_prize = 1 / result_eur_rate["rate"]

    date_and_time = result["time"]
    date = date_and_time[:10]
    time = date_and_time[11:19]

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
    cur.execute("SELECT moneda_from, quantity_from, moneda_to, quantity_to, date, time, unitary_prize FROM stand_by_operation_table")

    save_operation = cur.fetchone()




    con.close()

    return save_operation

def select_all():

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM operations_table;")

    selection = cur.fetchall()

    con.close()

    return selection

def commit_operation(values_dict):

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("INSERT INTO operations_table (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)", (values_dict["date"], values_dict["time"], values_dict["moneda_from"], values_dict["quantity_from"], values_dict["moneda_to"], values_dict["quantity_to"]))

    con.commit()
    con.close()

def my_wallet():
    pass
    





# En desuso:
'''
def choose_my_coins():
    abreviations = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
    result = get("https://rest.coinapi.io/v1/exchangerate/EUR?apikey={}".format(API_KEY))
    all_coins = result.json()
    
    my_dicts_coins = []

    for rate in all_coins["rates"]:
        if rate["asset_id_quote"] in abreviations:
            my_dicts_coins.append(rate)

    eur_dict = {"asset_id_quote": "EUR", "rate": 1, "time": rate["time"]}
    my_dicts_coins.append(eur_dict)

    return my_dicts_coins

    def dict_moneda(moneda_to, my_dicts_coins):
    for dict_coin in my_dicts_coins:
        if dict_coin['asset_id_quote'] == moneda_to:
            dict_coin_true = dict_coin
            
    return dict_coin_true '''
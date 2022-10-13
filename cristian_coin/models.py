
from config import API_KEY, DATA_BASE
import sqlite3
from requests import get   



def choose_my_coins():
    abreviations = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
    result = get("https://rest.coinapi.io/v1/exchangerate/EUR?apikey={}".format(API_KEY))
    all_coins = result.json()

    all_rates = []
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
            
    return dict_coin_true


    pass








def select_all():

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM operations_table;")

    selection = cur.fetchall()

    con.close()

    return selection
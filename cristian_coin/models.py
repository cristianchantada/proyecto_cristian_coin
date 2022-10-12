
from config import API_KEY, DATA_BASE
import sqlite3


'''
coins_list = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
coins = get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(coins_list, API_KEY))'''

def select_all():

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to FROM operations_table;")

    selection = cur.fetchall()

    con.close()

    return selection
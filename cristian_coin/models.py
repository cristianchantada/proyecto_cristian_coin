
from config import API_KEY, DATA_BASE
import sqlite3


'''
coins_list = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
coins = get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(coins_list, API_KEY))'''

def select_all():

    con = sqlite3.connect(DATA_BASE)
    cur = con.cursor()
    cur.execute("SELECT id, date, hour, from_sell, q_sell, to_buy, q_buy FROM operations_table;")

    selection = cur.fetchall()

    con.close()

    return selection
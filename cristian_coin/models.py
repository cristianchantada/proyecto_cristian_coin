from requests import get
from config import API_KEY

coins_list = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]
coins = get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(coins_list, API_KEY))
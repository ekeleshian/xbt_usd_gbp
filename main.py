import requests
import json
from matplotlib import pyplot
api_endpoint ='https://api.coindesk.com/v1/bpi/historical/close.json'

def fetch_us_btc_data():
	r = requests.get(api_endpoint+'?start=2018-04-01&end=2018-07-01')
	json_file_btc = r.json()
	btc_price_dict = json_file_btc['bpi']
	btc_prices = []

	for i in btc_price_dict:
		btc_prices.append(btc_price_dict[i])

	return btc_prices

def fetch_uk_btc_data():
	r = requests.get(api_endpoint+'?currency=GBP&start=2018-04-01&end=2018-07-01')
	json_file_btc = r.json()
	btc_price_dict = json_file_btc['bpi']
	btc_prices = []

	for i in btc_price_dict:
		btc_prices.append(btc_price_dict[i])

	return btc_prices


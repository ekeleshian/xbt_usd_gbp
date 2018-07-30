import requests
import json


def fetch_btcn_data():
	api_endpoint ='https://api.coindesk.com/v1/bpi/historical/close.json'

	r = requests.get(api_endpoint+'?start=2018-04-01&end=2018-07-01')


	json_file_btcn = r.json()
	btcn_price_dict = json_file_btcn['bpi']
	btcn_prices = []

	for i in btcn_price_dict:
		btcn_prices.append(btcn_price_dict[i])

	return btcn_prices


print(fetch_btcn_data())
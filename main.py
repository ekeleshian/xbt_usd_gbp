import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

api_endpoint ='https://api.coindesk.com/v1/bpi/historical/close.json'

def fetch_us_btc_data():
	r = requests.get(api_endpoint+'?start=2018-04-01&end=2018-07-01')
	json_file_btc = r.json()
	btc_price_dict = json_file_btc['bpi']
	btc_prices = []
	btc_dates = []

	for i in btc_price_dict:
		btc_prices.append(btc_price_dict[i])
		btc_dates.append(i)


	return btc_dates, btc_prices

def fetch_uk_btc_data():
	r = requests.get(api_endpoint+'?currency=GBP&start=2018-04-01&end=2018-07-01')
	json_file_btc = r.json()
	btc_price_dict = json_file_btc['bpi']
	btc_prices = []
	btc_dates = []

	for i in btc_price_dict:
		btc_prices.append(btc_price_dict[i])
		btc_dates.append(i)

	return btc_dates, btc_prices


us_dates, us_prices = fetch_us_btc_data()

uk_dates, uk_prices = fetch_uk_btc_data()

plt.plot_date(x = us_dates, y=us_prices, color = 'b')
plt.plot_date(x=uk_dates, y=uk_prices, color = 'r')
plt.legend(['US = Blue, UK = Red'])
plt.show()
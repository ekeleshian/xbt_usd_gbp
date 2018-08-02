import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pdb import set_trace


api_endpoint ='https://api.coindesk.com/v1/bpi/historical/close.json'

def fetch_us_btc_data():
	set_trace()
	r = requests.get(api_endpoint+'?start=2018-04-01&end=2018-07-01')
	# set_trace()
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

# set_trace()
us_dates, us_prices = fetch_us_btc_data()
# set_trace()
uk_dates, uk_prices = fetch_uk_btc_data()

# plt.plot_date(x = us_dates, y=us_prices, color = 'b')
# plt.plot_date(x=uk_dates, y=uk_prices, color = 'r')
# plt.legend(['US = Blue, UK = Red'])
# plt.show()

x = us_prices
y = uk_prices

n = len(us_prices)

def sum_of_products(x,y):
	array_of_products = []
	for a, b in zip(x,y):
		array_of_products.append(a*b)
	return sum(array_of_products)


def sum_of_variables(x):
	sigma = 0
	for i in x:
		sigma += i
	return sigma


def sum_of_squares(x):
	array_of_squares = []
	for i in x:
		array_of_squares.apend(i*i)
	return array_of_squares


def estimated_slope(x, y):
	numerator = n * sum_of_products(x, y) - sum_of_squares(x)*sum_of_squares(y)
	denominator = n * sum_of_squares(x) - sum_of_squares(x)*sum_of_squares(x)

	return float(numerator / denominator)


def estimated_y0(x,y):
	m = estimated_slope(x, y)
	first_term = float(1/n)*sum_of_variables(y)
	second_term = float(m/n)*sum_of_variables(x)
	return first_term - second_term

# print(min(x), max(x))
# print(min(y), max(y))
ind_var = []
d_var = []
for i in range(5000,10000, 200):
	ind_var.append(i)
	d_var.append(estimate_slope(x,y)*i + estimated_y0(x,y))

plt.scatter(ind_var, d_var, 'r' )

plt.show()
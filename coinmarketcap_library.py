#author: mrsmn/coinmarketcap-api

try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

class Market(object):

	def __init__(self, base_url='https://api.coinmarketcap.com/v1/'):
		self.base_url = base_url
		self.opener = urllib2.build_opener()
		self.opener.addheaders.append(('Content-Type', 'application/json'))
		self.opener.addheaders.append(('User-agent', 'coinmarketcap - python wrapper \
		around coinmarketcap.com (github.com/mrsmn/coinmarketcap-api)'))

	def _urljoin(self, *args):
		""" Internal urljoin function because urlparse.urljoin sucks """
		return "/".join(map(lambda x: str(x).rstrip('/'), args))

	def _get(self, api_call, query):
		url = self._urljoin(self.base_url, api_call)
		if query == None:
			response = self.opener.open(url).read()
		else:
			response_url = self._urljoin(url, query)
			response = self.opener.open(response_url).read()
		return response

	def ticker(self, param=None):
		""" ticker() returns a dict containing all the currencies
			ticker(currency) returns a dict containing only the currency you
			passed as an argument.
		"""
		data = self._get('ticker/', query=param)
		return data

	def stats(self):
		""" stats() returns a dict containing cryptocurrency statistics. """
		data = self._get('global/', query=None)
		return data



##################################################################
# moje trida pro zpracovani dat a vraceni hodnot
#
########################

class CoinMarket:
	
	usd_price = 0.0
	last_updated = 0
	
	def get_data(self, cointype):
		coinmarketcap = Market()
		
		# get ticket as utf-8 string
		# see example below
		mydatastr = coinmarketcap.ticker(cointype).decode("utf-8")	
		
		# example:
			# "id": "bitcoin",
			# "name": "Bitcoin",
			# "symbol": "BTC",
			# "rank": "1",
			# "price_usd": "2511.91",
			# "price_btc": "1.0",
			# "24h_volume_usd": "1552280000.0",
			# "market_cap_usd": "41120876011.0",
			# "available_supply": "16370362.0",
			# "total_supply": "16370362.0",
			# "percent_change_1h": "0.57",
			# "percent_change_24h": "1.78",
			# "percent_change_7d": "14.11",
			# "last_updated": "1496563150"			
		
		# get position of price
		pozice = mydatastr.find('price_usd')
		pozice_end = mydatastr.find('",', pozice) # searching for: ",

		# get price as string, convert to float
		usd_price = float(mydatastr[pozice+13:pozice_end])
		
		# test print - data
		# print(mydatastr)
		# test print - price
		# print(usd_price)
	
		# get position of time stamp
		pozice = mydatastr.find('last_updated')
		pozice_end = mydatastr.find('"\n', pozice) # searching for: "\n

		# get time stamp as string, convert to int
		last_updated = int(mydatastr[pozice+16:pozice_end])
		
		# test print - time stamp
		# print(last_updated)
		
		return usd_price, last_updated 

		

##################################################################
# moje funkce pro TRADE coins
#
########################

# bool - used as decision if next action is BUY or SELL 
buy = False

def trade(coinname, budget, increse_perc, decrease_perc, refreshsec):
	global buy #needs to be global to be able change it from here. From each other place everytime buy=False
	
	# create new class instance 
	coin = CoinMarket()

	# update data before decision
	coin_usd_price, timestamp_now = coin.get_data(coinname)

	# search for BUY
	if buy:
		print("BUY")

		# if price dropped 5% from last sale -> buy again
		if (stock_bought_for*0.95) >= coin_usd_price:
			tmp_volume = money_i_have/coin_usd_price
			money_i_have = 0
			tmp_price = coin_usd_price # save price 
			print("BOUGHT! Volume:",tmp_volume, "PAID for each:", coin_usd_price, 
				  "  sell when price >=", coin_usd_price*1.05)
			buy = False
		else:
			#say "no buy"
			print("else")
			if timestamp_now != timespamp_before:
				print("  no buy. Last stock bought for:", stock_bought_for, "Seeking for new price:", stock_bought_for*0.95, "Actual price is:", coin_usd_price)
				timespamp_before = timestamp_now

	
	# search for SELL
	else:
		print("SELL")
		buy = True

		if coin_usd_price >= (tmp_price*1.05):
			#sell
			money_i_have = coin_usd_price * tmp_volume
			print("SOLD!  Money I have:", money_i_have, "SOLD each for:", coin_usd_price)
			
			buy = True
			#NEFUNGUJE timespamp_before = 0 # vynuluj citac a vypis "no buy" at vis jakou cenu hledas
			stock_bought_for = coin_usd_price
			
		else:
			#say "no sale"
			if timestamp_now != timespamp_before:
				print("  no sale. Seeking for new price:", stock_bought_for*1.05, "Actual price is:", coin_usd_price)
				timespamp_before = timestamp_now

	return [] #





def buycoin(coinname, budget, coin_usd_price, timestamp_now, increse_perc, decrease_perc, refreshsec):

	global buy # mark variable as GLOBAL otherwise you will change value only localy
	
	return []




				
				
				
				

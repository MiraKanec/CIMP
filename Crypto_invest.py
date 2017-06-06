
import os
from numpy import genfromtxt
from coinmarketcap_library import Market
from coinmarketcap_library import CoinMarket	
from time import sleep


#clean screen
os.system('cls')
print ('\n')


# bool - used as decision if next action is BUY or SELL 
buy = False


##############################
#definuj pocatecni hodnoty
money_i_have = 0.0
tmp_price    = 0.00598069 #price in USD
tmp_volume   = 100.0/tmp_price
timestamp_now = 1496582052
timespamp_before = 1496582052

# price of single stock I bought last time
stock_bought_for = tmp_price

print("Start: \nstart price:", tmp_price, "start volume:", tmp_volume)
print("  Seeking for new price:", stock_bought_for*1.05, "Actual price is:", tmp_price)
##############################


# create new class instance 
bitcoin = CoinMarket()

while True:

	# update data for 
	bitcoin_usd_price, timestamp_now = bitcoin.get_data("digitalnote")
	# print(bitcoin_usd_price)
	# print(digitalnote_last_updated)



	# search for BUY
	if buy:
		
		# if price dropped 5% from last sale -> buy again
		if (stock_bought_for*0.95) >= bitcoin_usd_price:
			tmp_volume = money_i_have/bitcoin_usd_price
			money_i_have = 0
			tmp_price = bitcoin_usd_price # save price 
			print("BOUGHT! Volume:",tmp_volume, "PAID for each:", bitcoin_usd_price, 
				  "  sell when price >=", bitcoin_usd_price*1.05)
			buy = False
		else:
			#say "no buy"
			if timestamp_now != timespamp_before:
				print("  no buy. Last stock bought for:", stock_bought_for, "Seeking for new price:", stock_bought_for*0.95, "Actual price is:", bitcoin_usd_price)
				timespamp_before = timestamp_now
			
	# search for SELL
	else:		
		if bitcoin_usd_price >= (tmp_price*1.05):
			#sell
			money_i_have = bitcoin_usd_price * tmp_volume
			print("SOLD!  Money I have:", money_i_have, "SOLD each for:", bitcoin_usd_price)
			
			buy = True
			#NEFUNGUJE timespamp_before = 0 # vynuluj citac a vypis "no buy" at vis jakou cenu hledas
			stock_bought_for = bitcoin_usd_price
			
		else:
			#say "no sale"
			if timestamp_now != timespamp_before:
				print("  no sale. Seeking for new price:", stock_bought_for*1.05, "Actual price is:", bitcoin_usd_price)
				timespamp_before = timestamp_now

	# 
	sleep(60)	
	
	
	
	
	
	
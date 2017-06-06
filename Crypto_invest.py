
from numpy import genfromtxt
import os
#clean screen
os.system('cls')

# array of currency price
CURR_coindesk = genfromtxt('C:\Prog\Crypto_invest_my_proj\\training_CSV\ETH1.csv', delimiter=',')


##############################

money_I_have =   0.0
tmp_price    =  161.18
tmp_volume   =  100.0/tmp_price

##############################

# bool - used as decision if next action is BUY or SELL 
buy = False
# 
new_max_price = tmp_price


for actual_price in CURR_coindesk:
	# search for BUY
	if buy:
		print("new_max_price =", new_max_price, "new_max_price*0.95 =", new_max_price*0.95, "actual_price =", actual_price)
		# if price dropped 5% from last sale -> buy again
		if (new_max_price*0.95) >= actual_price:
			tmp_volume = money_I_have/actual_price
			money_I_have = 0
			tmp_price = actual_price # save price 
			print("BOUGHT! tmp_volume =",tmp_volume, "PAID each:", actual_price)
			print("  sell when price =", actual_price*1.05)
			buy = False
		else:
			print("no buy")
			
	# search for SELL
	else:		
		if actual_price >= (tmp_price*1.05):
			#sell
			money_I_have = actual_price * tmp_volume
			print("SOLD!  money_I_have =", money_I_have, "SOLD each:", actual_price)
			
			buy = True
			new_max_price = actual_price
			
		else:
			#say "no sale"
			print("no sale  ", actual_price)

print("money_I_have =", money_I_have)
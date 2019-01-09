import random

def profitcalc(initial_sum=1000,percent=10,days=365):
	'''function return profit for specific period
	
	arguments:
		initial_sum(float)
		percent(float): simple percent
		days(float)
		
	return:
		float
		'''
	return initial_sum*percent/100*days/365
	
keyss=('initial_sum','percent','days')
offer=[]
profit=[]
for i in range(2):
	offer.append(input('Enter the {} initial sum,percent,days \
(separated by a comma): '.format(i+1)).split(','))	
	offer[i]={keyss[j]:float(offer[i][j]) for j in range(3)}
print(offer)
for i in range(2):
	profit.append(profitcalc(**offer[i]))
	print('{} profit: {:.2f}'.format(i+1, profit[i]))
comp=int(profit[0]<profit[1])
if profit[0]!=profit[1]:
	print('{} profit is higher, than {}'.format(1+comp,2-comp))
else:
	print('Equilibrium')

	




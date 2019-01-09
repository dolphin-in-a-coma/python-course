import random

def amountdigits(num):
	'''return amount of digits
	
	argumet:
		*num(int): natural number   
	
	result:
		int
		'''	
	if num>10:
		num//=10
		return amountdigits(num)+ 1
	else:
		return 1

def sumdigits(num):
	'''return sum of digits
	
	argumet:
		*num(int): natural number   
	
	result:
		int
		'''	
	if num>10:
		return sumdigits(num//10)+ num%10
	else:
		return num

num=random.randrange(10000)
print(num)
print(amountdigits(num))
print(sumdigits(num))




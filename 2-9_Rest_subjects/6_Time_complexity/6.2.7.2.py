import random
import time

def get_time(func,arg):
	time1=time.time()
	func(arg)
	time2=time.time()
	return round((time2-time1)*1000,2)

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
res=[['n','1(ms)','2(ms)']]
form_str='{:10}'*len(res[0])
for n in (100,1000,10000,100000,1000000):
	res.append((n,get_time(amountdigits,n),get_time(sumdigits,n)))
for i in res:
	print(form_str.format(*i))





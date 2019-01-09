import random

def posneg(*args):
	'''return two tuples: of negatives and positives numbers
	
	argumets:
		*args(float):numbers are in tuple   
	
	result:
		tuple: tuple of two tuples
		'''	
	neg=[i for i in args if i<=0]
	pos=set(args).difference(set(neg))
	pos=list(pos)
	neg.sort(reverse=True)
	pos.sort(reverse=True)
	neg=tuple(neg)
	pos=tuple(pos)
	return (neg, pos)

nums=[]
for i in range(50):
	nums.append(random.randrange(-100,100))
print (posneg(*nums))

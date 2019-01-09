import random

def powfor(base=2,exp=2):
	'''function return exponentiation of base in exp through cycle 'for'
	
	arguments:
		base(float)
		exp(int): exponent, natural
		
	return:
		float
		'''
	exp=int(exp)
	result=1
	for i in range(exp):
		result*=base
	return result
	
def powrec(base=2,exp=2):
	'''function return exponentiation of base in exp through recusion
	
	arguments:
		base(float)
		exp(int): exponent, natural or zero
		
	return:
		float
		'''
	if exp==0:
		return 1
	return powrec(base,exp-1)*base
	
lst=input('Enter the base,exponent (separated by a comma): ').split(',')	
for i in range(2):
	lst[i]=float(lst[i])

print('Through cycle \'for\': {:.2f}\nThrough recursion: {:.2f}'\
.format(powfor(*lst),powrec(*lst)))

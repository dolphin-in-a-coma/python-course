def leastmult(*args):
	"""function return least common multiple of some numbers
	
	arguments:
		*args: int
		
	result:
		int
	"""
    
	def leastmulttwo(a, b):
		"""function return least common multiple of two numbers
		
		arguments:
			a: int
			b: int
		
		result:
			int
		"""
		for i in range(b):
			if not a*(i+1)%b:
				return a*(i+1)
    
	p=1
	for i in args:
		p=leastmulttwo(p,i)
	return p	

nums= [int(x) for x in input(
'Enter the numbers separate by comma: ').split(',')]
print('Least common multiple: {}'.format(leastmult(*nums)))

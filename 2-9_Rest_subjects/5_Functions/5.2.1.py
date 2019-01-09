
def somespecial(x, y):
    """return z=(sgn(x)+y**2)/(sgn(y)-(abs(x))**0.5)
    
    arguments:
		x: float
		y: float
		
	result:
		float
		"""
    def sgn(x):
        """return value of signum function
        
        argument:
			x: float
        
        result:
			float
        """
        
        if x>0:
            return 1
        elif x==0:
            return 0
        else:
            return -1

    return (sgn(x)+y**2)/(sgn(y)-(abs(x))**0.5)



params = [float(i) for i in input('Enter (x y): ').split()]
print(somespecial(*params))

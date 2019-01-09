import random

def islucky(number):
    """function to check is lucky ticket or not
    return True, if it's lucky, else return False
    
    argument:
		number(int): natural six-digit
		
	result:
		bool
    """
    def sumdig(num):
        """function return sum of three digits
	
		argument:
			num: natural three-digit
		
		result:
			int
	"""
        return ((num%10)+(num//10)%10+num//100)

    luck = (sumdig(number//1000))==(sumdig(number%1000))
    return 'Lucky: {}'.format(luck)

i=random.randint(100000,999999)
print('Number of ticket: {}'.format(i),islucky(i), sep='\n')

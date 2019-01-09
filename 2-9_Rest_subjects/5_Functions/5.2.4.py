def dayin(month, year):
	"""function return quantity of days in month
		
	arguments:
		day: int, >=1, <=31
		month: int, >=1, <=12
		
	result:
		int
	"""
	feb=2
	months31=(1,3,5,7,8,10,12)
	if month in months31:
		return 31
	elif month != feb:
		return 30
	elif (year%4==0 and year%100!=0) or year%400:
		return 29
	else:
		return 28	
    
	
def tomorrow(day, month, year):
	"""function return tomorrow date
		
	arguments:
		day: int, >=1, <=31
		month: int, >=1, <=12
		year: int
		
	result:
		lst: list of integer, length = 3
	"""
	dec=12
	if day == dayin(month, year) and month==dec:
		return (1,1,year+1)
	elif day == dayin(month, year):
		return (1,month+1,year)
	else:
		return (day+1, month, year)

def yesterday(day, month, year):
	"""function return yesterday date	
	
	arguments:
		day: int, >=1, <=31
		month: int, >=1, <=12
		year: int
		
	result:
		lst: list of integer, length = 3
	"""
	jan=1
	dec=12
	if day == 1 and month==jan:
		return (31,12,year-1)
	elif day == 1:
		return (dayin(month-1,year),month-1,year)
	else:
		return (day-1, month, year)

date = a = [int(x) for x in input(
'Enter the date with comma: ').split(',')]
print('Yesterday: {}\nTomorrow: {}'.format(tomorrow(*date),
yesterday(*date)))

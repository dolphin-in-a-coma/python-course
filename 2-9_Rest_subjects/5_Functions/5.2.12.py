def amountfree(car):
	'''function return amount of free seats in carriage
	
	argument:
		car(list): list of dicts	
			
	result:
		int
	'''
	amount=0
	for i in car:
		amount+=list(i.values()).count(None)
	return amount
def whollyempty(car):
	'''function return numbers of comletely empty room
	
	argument:
		car(list): list of dicts	
		
	result:
		int
	'''
	empty=[]
	for i in range(len(car)):
		if list(car[i].values()).count(None)==4:
			empty.append(i)
	return empty
def isgender(car,gender='м'):
	'''function return list of numbers of room of define gender, 
	which have free seat. if there aren't, function return False
		
	argument:
		car(list): list of dicts
		gender(char)	
		
	result:
		int, if there are any
		False, if there are none
	'''
	rooms=[]
	for i in range(len(car)):
		room=list(car[i].values())
		if gender in room and None in room and room.count(None)+\
		room.count(gender)==4:
			rooms.append(i)
	if rooms:	
		return rooms
	return False
def isfemale(car):
	'''function return list of numbers of female room, 
	which have free seat. if there aren't, function return False
		
	argument:
		car(list): list of dicts	
		
	result:
		int, if there are any
		False, if there are none
	'''
	return isgender(car,'ж')
def lowandup(car,level=0):
	'''function return list of numbers of room with bottom free seats, 
	if level=0. if level=1, it return list of number of room with
	free top seats
			
	argument:
		car(list): list of dicts
		level(int)
		
	result:
		int, if there are any
		False, if there are none
	'''
	rooms=[]
	for i in range(len(car)):
		if not car[i][1+level] or not car[i][3+level]:
			rooms.append(i)
	return rooms
def upper(car):
	return lowandup(car,level=1)	

a=[{1:'м',2:'ж',3:None,4:'м'},{1:'м',2:'м',3:None,4:None},
{1:None,2:None,3:None,4:None},{1:None,2:None,3:None,4:None},
{1:'ж',2:'ж',3:None,4:None},{1:'ж',2:None,3:'м',4:None},
{1:None,2:'м',3:None,4:'м'}]
print(amountfree(a),whollyempty(a),isgender(a),isfemale(a),lowandup(a),
upper(a),sep='\n')

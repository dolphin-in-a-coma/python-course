def isseatfree(path,row,seat):
	try:
		seats=[]
		with open(path,encoding='utf-8') as fl:
			rows=fl.readlines()
		for i,rw in enumerate(rows):
			seats.append([])		
			for st in rw.split(','):
				seats[int(i)].append(int(st))
		return bool(seats[row-1 ][seat-1])
				
	except Exception as err:
		print('Error occured during execution:',err)
		raise

path='data.txt'	
row=int(input('Enter the number of row: '))
seat=int(input('Enter the number of seat: '))

no=''
if isseatfree(path,row,seat):
    no='not '
print('This seat is {}available'.format(no))

import random

def listtofile(lst,path):
	try:
		fl=None
		fl=open(path,mode='w',encoding='utf-8')
		for i in lst:
			print(i,file=fl)
	
	except Exception as err:
		print('Error occured during execution:',err)
		raise
	
	finally:
		if fl:
			fl.close()

lst=random.sample(range(10000),random.randrange(10,50))
path='data.txt'			
listtofile(lst,path)		

import random

def summaxinfile(path):
	try:
		fl=None
		fl=open(path,mode='r+',encoding='utf-8')
		lst=[int(i) for i in fl.readlines()]
		print(sum(lst),file=fl)
		fl.write(str(max(lst))+'\n')	
		return lst	
	
	except Exception as err:
		print('Error occured during execution:',err)
		raise
	
	finally:
		if fl:
			fl.close()

path='data.txt'			
print(summaxinfile(path))

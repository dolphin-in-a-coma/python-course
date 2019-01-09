import random

def election(votes):
	'''return voting result, list of parties in decreasing order
	
	argument:
		votes(list): list of votes in numbers  
	
	result:
		amountvotes(tuple): structure(tuple of dictionaries)
		whose dictionaries have keys: title and percent
		'''	
	amountvotes=[]
	n=len(votes)
	
	parties =('Родина','Коммунисты России', 
	'Российская партия пенсионеров за справедливость',
	'Единая Россия','Зелёные','Гражданская платформа','ЛДПР',
	'Партия народной свободы','Партия роста','Гражданская сила',
	'Яблоко','КПРФ', 'Патриоты России','Справедливая Россия')
	numparties={-1: 'Испорченный бланк'}
	for i in range(14):
		numparties[i+1]=parties[i]
		
	for i in numparties.keys():
		party={'title':numparties[i], 'percent':votes.count(i)*100/n}
		amountvotes.append(party)
		
	amountvotes.sort(key=lambda x:x['percent'],reverse=True)
	return tuple(amountvotes)

path='data.txt'
'''nums=list(range(1,15))
nums.append(-1)
votes=[]
for i in range(1000000):
	votes.append(random.choice(nums))'''
try:
	with open(path,mode='r+',encoding='utf-8') as fl:
		'''for i in votes:
			print(i,file=fl)'''
		vts=[int(i.strip()) for i in fl.readlines()]
except Exception as err:
	print('Error occured during execution:',err)	
print(election(vts))

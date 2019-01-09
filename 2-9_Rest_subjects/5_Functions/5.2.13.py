'''students=[{'height':200,'name':'Jeal','age':20},
{'height':172,'name':'Jean','age':23},
{'height':181,'name':'Adgar','age':18},
{'height':168,'name':'Alber','age':26},
{'height':220,'name':'Franz','age':14}]'''

students=[]
keyss=('name','age','height')
while True:
	data=input('Enter the student\'s name,age,height: ')\
	.split(',')
	if len(data)>2:
		dct={}
		for i in data:
			dct[keyss[data.index(i)]]=int(i) if i.isdigit() else i
		students.append(dct)
	else:
		break

students.sort(key=lambda x:x['name'])
print('increase of name:',students, sep='\n\t', end='\n\n')
students.sort(key=lambda x:x['age'])
print('increase of age:',students, sep='\n\t', end='\n\n')
print('the youngest:',students[0], end='\n\n')
students.sort(key=lambda x:x['height'])
print('increase of height:',students, sep='\n\t', end='\n\n')
print('the highest:',students[-1], end='\n\n')

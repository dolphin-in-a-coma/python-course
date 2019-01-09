import json

try:
	path='book.json'
	with open(path,'r') as fl:
		jsonbook=fl.read()
	if jsonbook:
		book=json.loads(jsonbook)
	else:
		book=({},{})

	answer=1.5
	print('Welcome to The Phone Book!\n\n\
What do you want?')
	
	while answer:
		answer=int((input('\nSerch - Enter 1\n\
Delete - Enter 2\n\
Add - Enter 3\n\
Show all - Enter 4\n\
Close - Enter 0\n>>')))
		assert 0<=answer<=4,'Answer must be int between 0 and 3!'
		
		if answer==1:
			answer=int((input('Do you want serarch by name(1)\
 or by number(2)?\n>>')))
			if answer==1:
				name=input('Enter the name: ')
				print(name, ':', book[0].get(name,'There isn\'t this name'))
			elif answer==2:
				number=int(input('Enter the number: '))
				print(number, ':', book[1].get(number,'There isn\'t this number'))
			else:
				print('Wrong answer')
		
		elif answer==2:
			answer=int((input('Do you want delete by name(1)\
 or by number(2)?\n>>')))
			if answer==1:
				name=input('Enter the name: ')
				if not book[0].get(name):
					print('There isn\'t this name')
					continue
				print(name, ':', book[0][name],'deleted')
				del book[1][book[0][name]]
				del book[0][name]
			elif answer==2:
				number=input('Enter the number: ')
				if not book[1].get(number):
					print('There isn\'t this number')
					continue
				print(number, ':', book[1][number],'deleted')
				del book[0][book[1][number]]
				del book[1][number]
			else:
				print('Wrong answer')
		
		elif answer==3:
			name=input('Enter the name: ')
			number=input('Enter the number: ')
			book[0][name]=number
			book[1][number]=name
			print(name,':',number,'added')
		elif answer == 4:
			print(book[0])
	
except Exception as err:
	print('Error occured during execution:',err)

finally:
	jsonbook=json.dumps(book,indent=4,ensure_ascii=True)
	with open(path,'w',encoding='utf-8') as fl:
		fl.write(jsonbook) 
	

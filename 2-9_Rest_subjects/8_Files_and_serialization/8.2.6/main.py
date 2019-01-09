import json

try:
	oldaboutme={}
	oldaboutme['fio']='Рудаков Евгений Артемович'
	oldaboutme['birthday']='22.07.1995'
	oldaboutme['birthplace']='Москва'
	oldaboutme['хобби']=['dratsing', 'krasting', 'toltshoking']
	oldaboutme['хобби'].append('programming')
	oldaboutme['животные']=()
	oldaboutme['ЕГЭ']=dict()
	oldaboutme['ЕГЭ']['Русский язык']=82
	oldaboutme['ЕГЭ']['Математика']=77
	oldaboutme['ЕГЭ']['Информатика и ИКТ']=88
	oldaboutme['ЕГЭ']['Физика']=79
	oldaboutme['ЕГЭ']['История']=None
	del oldaboutme['ЕГЭ']['История']
	oldaboutme['вузы']=dict()
	oldaboutme['вузы']['МГУ']=407
	oldaboutme['вузы']['МГТУ им. Баумана']=240
	oldaboutme['вузы']['МИЭМ НИУ ВШЭ']=267
	oldaboutme['вузы']['НИЯУ МИФИ']=232
	oldaboutme['вузы']['МТУ']=205
	
	me_in_json=json.dumps(oldaboutme, ensure_ascii=False, indent=4)
	path='data.json'
	
	with open(path,mode='w',encoding='utf-8') as fl:
		fl.write(me_in_json)
	
	with open(path,mode='r',encoding='utf-8') as fl:
		txtaboutme=fl.read()
	
	aboutme=json.loads(txtaboutme)
	
	Equality=True
	
	for i in aboutme.keys():
		if isinstance(aboutme[i],(str,int)):
			if aboutme[i]!=oldaboutme[i]:
				Equality=False
		elif isinstance(aboutme[i],dict):
			for j in aboutme[i].keys():
				if aboutme[i][j]!=oldaboutme[i][j]:
					Equality=False
		elif isinstance(aboutme[i],list):
			for j,item in enumerate(aboutme[i]):
				if oldaboutme[i][j]!=item:
					Equality=False
					
	print('Старая структура:\n\n',oldaboutme)
	print('\n'+60*'-'+'\n')
	print('Структура из JSON-файла:\n\n',aboutme)
	print('\n'+60*'-'+'\n')
	if Equality:
		no=''
	else:
		no='не '
	print('Cтруктуры {}равны.'.format(no))
	print('\n'+60*'-'+'\n')
	print('Вузы:',tuple(aboutme['вузы'].keys()))
	print('предметы:',tuple(aboutme['ЕГЭ'].keys()))

	print('\n'+60*'-'+'\n')	

	vowels=["А","Е","Ё","И","О","У","Ы","Э","Ю","Я"]

	i=0
	while(aboutme['fio'][i]!=' '):
		i+=1
	i+=1
	print('Мое имя начинается на гласную букву:',aboutme['fio'][i] in vowels)
	month=int(aboutme['birthday'][3:5])
	print('Родился зимой или летом:', 1<=month<=2 or 6<=month<=8 or month==12)
	print('У меня {} хобби, первое - '.format(len(aboutme['хобби']))+aboutme['хобби'][0])
	print('Я сдавал',len(aboutme['ЕГЭ']),'экзамена')
	print('Максимальный балл:',max(aboutme['ЕГЭ'].values()))
	mark=sum(aboutme['ЕГЭ'].values())
	print('Сумма баллов:',mark)
	amount=int(mark>=aboutme['вузы']['МГУ'])\
        +int(mark>=aboutme['вузы']['МГТУ им. Баумана'])\
        +int(mark>=aboutme['вузы']['МИЭМ НИУ ВШЭ'])\
        +int(mark>=aboutme['вузы']['НИЯУ МИФИ'])\
        +int(mark>=aboutme['вузы']['МТУ'])
	print('Кол-во вузов, в которые прохожу:', amount)

except Exception as err:
	print('Error occured during execution:',err)
	raise


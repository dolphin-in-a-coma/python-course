aboutme={}
#aboutme+={'fio':'Рудаков'}
aboutme['fio']='Рудаков Евгений Артемович'
aboutme['birthday']='22.07.1995'
aboutme['birthplace']='Москва'
aboutme['хобби']=['dratsing', 'krasting', 'toltshoking']
aboutme['хобби'].append('programming')
aboutme['животные']=()
aboutme['ЕГЭ']=dict()
aboutme['ЕГЭ']['Русский язык']=82
aboutme['ЕГЭ']['Математика']=77
aboutme['ЕГЭ']['Информатика и ИКТ']=88
aboutme['ЕГЭ']['Физика']=79
aboutme['ЕГЭ']['История']=None
del aboutme['ЕГЭ']['История']
aboutme['вузы']=dict()
aboutme['вузы']['МГУ']=407
aboutme['вузы']['МГТУ им. Баумана']=240
aboutme['вузы']['МИЭМ НИУ ВШЭ']=267
aboutme['вузы']['НИЯУ МИФИ']=232
aboutme['вузы']['МТУ']=205

print(aboutme)
print('\n'+60*'-'+'\n')
print('Вузы:',tuple(aboutme['вузы'].keys()))
print('предметы:',tuple(aboutme['ЕГЭ'].keys()))

print('\n'+60*'-'+'\n')
#if aboutme['fio'][0]==

vowels=["А","Е","Ё","И","О","У","Ы","Э","Ю","Я"]
#for i in aboutme['fio']:
 #   if i==' ':
  #      break
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

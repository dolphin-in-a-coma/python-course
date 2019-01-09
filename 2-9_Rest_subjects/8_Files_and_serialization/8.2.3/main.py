def voworcons(path):
	try:
		vowel='аеёиоуыэюя'
		cons='бвгджзклмнпрстфхцчшщ'
		count=0
		fl=None
		fl=open(path,mode='r',encoding='cp1251')
		poem=fl.read()
		poem.lower
		for i in poem.split():
			if i[0] in vowel:
				count+=1
			elif i[0] in cons:
				count-=1
		if count>0:
			whatsmore='The amount of vowels is more than \
the consonants for '+str(count)
		elif count<0:
			whatsmore='The amount of consonants is more than \
the vowels for '+str(abs(count))
		else:
			whatsmore='Equilibrium'	
		return (poem,whatsmore)
				
	except Exception as err:
		print('Error occured during execution:',err)
		raise
	
	finally:
		if fl:
			fl.close()

path='data.txt'			
print(voworcons(path)[0],voworcons(path)[1],sep='\n\n')


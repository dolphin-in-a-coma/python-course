def ceasar(text, offset=1):
	"""функция возвращает текст, зашифрованный шифром Цезаря с
	указанным сдвигом, либо расшифрованный с указанным сдвигом *(-1)
	
	аргументы:
		text: str
		offset(int): >=-33,<=33
	результат:
		str
	"""
	
	def inabc(l,offset,abc):
		"""функция возвращает один символ, зашифрованный шифром Цезаря с
		указанным сдвигом, либо расшифрованный с указанным сдвигом *(-1)
	
		аргументы:
			i(str): one char
			offset(int): >=-33,<=33
			abc: str
		результат:
			str, one char
	"""
		
		if l in abc[:-offset]:
			return abc[abc.find(l)+offset]
		elif l in abc[-offset:]:
			return abc[abc.find(l)+offset-len(abc)]
			
	abc=''
	for i in range(1040,1072):
		abc+=chr(i)
		if i==1045:
			abc+='Ё'
	lowabc=abc.lower()
	newtext=''
	for l in text:
		if l in abc:
			newtext+=inabc(l,offset,abc)
		elif l in lowabc:
			newtext+=inabc(l,offset,lowabc)
		else:
			newtext+=l 
	return newtext

text=input('Введите текст: ')
offset=int(input('Введите сдвиг, для расшифровки *(-1): '))
print(ceasar(text,offset))

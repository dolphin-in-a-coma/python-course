def strtodict(text):
	"""function return a dictionary, whose keys are letters and 
	values are their amount in the text
	
	argument:
		text: str
		
	result:
		dict
	"""
	text=text.upper()
	dct={}
	for i in text:
		dct[i]=text.count(i)
	return dct
		
a=(input('Enter the sentence: '))
print('Dictionary of amount of letters: ', strtodict(a))

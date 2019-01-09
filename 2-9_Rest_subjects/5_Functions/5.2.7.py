def charscount(text, chars):
	"""function return amount of all specified chars in the text
	
	arguments:
		text: str
		chars: str
		
	result:
		int
	"""
	total=0
	for i in chars:
		total+=text.count(i)
	return total
			
digits=[str(x) for x in range(10)]
sents=[x for x in input(
'Enter the 3 sentences separate by point: ').split('.')]
amount=[charscount(sents[x],digits) for x in range(3)]
print('Sentence with the most amount of digits: {}\
'.format(amount.index(max(amount))+1))

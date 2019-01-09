def print2(text, frame='*'):
	"""function print text in frame
	
	arguments:
		text: str
		frame: str
		
	result:
		0
	"""
	print (frame*(len(text)+2)+'\n'+frame+text+frame+'\n'+
	frame*(len(text)+2))
	return 0
		
			
print2(input('Enter your text: '),input('Enter symbol of frame: '))

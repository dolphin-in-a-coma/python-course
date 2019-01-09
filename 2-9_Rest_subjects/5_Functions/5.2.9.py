def from10toN(number, base=2):
	"""function return number in N numeral system
	
	arguments:
		number: int, might be str
		base(int): >=2, <=36
		
	result:
		int
	"""
	number=int(number)
	abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	newnumber=''
	while(number>0):
		residue=number%base
		if (residue)>9:
			residue=abc[residue-10]
		newnumber=str(residue)+newnumber
		number//=base
	return newnumber

def fromNto10(number, base=2):
	"""function return number in decimal numeral system
	
	arguments:
		number: int or str
		base(int): >=2, <=36
		
	result:
		int
	"""
	number=str(number).upper()
	abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'	
	newnumber=0		
	while(number!=''):
		end=number[0]
		if abc.find(end)>-1:
			end=abc.find(end)+10
		newnumber*=base
		newnumber+=int(end)
		number=number[1:]
	return int(newnumber)

a=(input('Enter the number in decimal notation to convert to N: '))
b=(input('Enter the number in N notation to convert to decimal: '))
c=int(input('Enter the N-base: '))
print('From 10 to N:', from10toN(a,c))
print('From N to 10:', fromNto10(b,c))


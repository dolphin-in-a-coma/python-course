import random

def gdp(c=0,i=0,g=0,ex=0,im=0):
	'''function return Gross Domestic Product
	
	arguments:
		c(float): consumption >=0
		i(float): investments >=0
		g(float): goverment spending >=0
		ex(float): export >=0
		im(float): import >=0
		
	return:
		float
		'''
	return c+i+g+ex-im
	
keyss=('c','i','g','ex','im')
lst=[]
dct={}
product=[]
lst=input('Enter the consumption, investments, \
goverment spending, export, import(separated by a comma): ').split(',')	
for i in range(5):
	lst[i]=float(lst[i])
	dct[keyss[i]]=lst[i]
print(lst,dct)

product.append(gdp(*lst))
product.append(gdp(**dct))
comp=int(product[0]<product[1])
if product[0]!=product[1]:
	print('{} product is higher, than {}'.format(1+comp,2-comp))
else:
	print('Equilibrium')

	




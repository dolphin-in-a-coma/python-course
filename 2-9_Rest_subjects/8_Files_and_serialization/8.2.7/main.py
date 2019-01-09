import csv

try:
	path='08_02_07_data.csv'
	newpath='newdata.csv'
	with open(path,mode='r',encoding='utf-8') as fl:
		lines=fl.readlines()
		gdp=list(csv.reader(lines, delimiter=';'))
	form='{} | {} | {}'
	rf='Россия'
	m=max(gdp, key=lambda a:int(a[1]))
	print(form.format(gdp.index(m)+1,m[0],m[1]))
	for i in gdp:
		if i[0]==rf:
			print(form.format(gdp.index(i)+1,i[0],i[1]))
	m=min(gdp, key=lambda a:int(a[1]))
	print(form.format(gdp.index(m)+1,m[0],m[1]))
	edge=int(input('Enter the low edge: '))
	newgdp=''
	j=0
	while (int(gdp[j][1])>edge):
		newgdp+=lines[j]
		j+=1
	with open(newpath,mode='w',encoding='utf-8') as fl:
		fl.write(newgdp)

except Exception as err:
	print('Error occured during execution:',err)
	raise

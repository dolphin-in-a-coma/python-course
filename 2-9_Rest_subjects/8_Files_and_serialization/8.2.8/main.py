import csv

try:
	ranking={}
	path='data.csv'
	newpath='ranking.csv'
	with open(path,mode='r') as fl:
		group=list(csv.reader(fl, delimiter=','))
	for i in group:
		i[0].strip()
		name=i[0].split()[1]
		if ranking.get(name, False):
			ranking[name]+=1
		else:
			ranking[name]=1
	listranking=list(ranking.items())

	with open(newpath,mode='w') as fl:
		writer=csv.writer(fl, quoting=csv.QUOTE_ALL)
		writer.writerows(sorted(listranking,key=lambda a:1/a[1]))

except Exception as err:
	print('Error occured during execution:',err)
	raise

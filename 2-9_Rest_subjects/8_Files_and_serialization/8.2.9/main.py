import csv
import json

try:
	ranking={}
	csvpath='data.csv'
	jsonpath='data.json'
	analysispath='analysis.json'
	with open(csvpath,mode='r') as fl:
		group=list(csv.DictReader(fl, fieldnames=["name", "e-mail", "IKT","EGE"],delimiter=';'))
	jsongroup=json.dumps(group, ensure_ascii=False, indent=4)
	with open(jsonpath,mode='w') as fl:
		fl.write(jsongroup)
	with open(jsonpath,mode='r') as fl:
		newgroup=json.loads(fl.read())
	
	withege=0
	withinf=0
	totalege=0
	totalinf=0
	email_ranking={}
	for i in newgroup:
		if i['EGE'].isdigit():
			totalege+=int(i['EGE'])
			withege+=1
		if i['IKT'].isdigit():
			totalinf+=int(i['IKT'])
			withinf+=1
		service=i['e-mail'].split('@')[-1]

		if email_ranking.get(service,False):
			email_ranking[service]+=1
		elif service!='-':
			email_ranking[service]=1
	avr_ege=totalege/withege
	avr_inf=totalinf/withinf
	topservice=sorted(list(email_ranking.items()),key=lambda a:a[-1])[-1][0]
	analysis={'Average EGE':round(avr_ege),'Average IKT':round(avr_inf),'Top Post Service':topservice}
	jsonanalysis=json.dumps(analysis,ensure_ascii=False,indent=4)
	with open(analysispath, mode='w') as fl:
		fl.write(jsonanalysis)
		
except Exception as err:
	print('Error occured during execution:',err)
	raise

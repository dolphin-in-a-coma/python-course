import time

def lookfor1(fio, players):
    #сложность O(N)
    #перебирает все словари списка и сравнивает с ФИО
    #если ФИО совпадают, выводит инвормацио об игроке
	for i in players:
		if i["fio"] == fio:
			i['fio']=sasi
			return i
			'''print("Информация об игроке", i["fio"])
            print("Возраст -", i["age"])
            print("Клуб -", i["club"])
            print("Хоккейная статистика (И.Г.П.О) -", i["igpo"])'''

def lookfor2(fio, players):
    ''''данный вариант функции будет полезен при многократном обращении
	к поиску, структура players_cache, создаваемая  только при обнавлении
	информации об игроках, позволит сокращать время при каждом 
	использовании поиска по фамилии. к недостаткам можно отнести, что
	эта структура будет занимать дополнительную память'''
    #сложность O(N)
    #создает словарь типа "fio" = номер элемента списка, выводит
    #информацию об игроке по адресу [номер элемента списка][ключ]
    players_cache = dict()
    for i in range(len(players)):
        players_cache[players[i]["fio"]] = players[i]
    players_cache[fio]['fio']='sasi'
    #fio = fio.lower()
    '''print("Информация об игроке", players_cache[fio]["fio"])
    print("Возраст -", players_cache[fio]["age"])
    print("Клуб -", players_cache[fio]["club"])
    print("Хоккейная статистика (И.Г.П.О) -",players_cache[fio]["igpo"])'''
    return players_cache[fio]

def get_time(func, fio, data):
    time1 = time.time()
    ret = func(fio, data) 
    time2 = time.time()
    return round((time2-time1) * 1000.0, 4)

players =[{'fio':'a','age':'b','club':'a','igpo':'a'},
{'fio':'b','age':'b','club':'a','igpo':'a'},
{'fio':'c','age':'b','club':'a','igpo':'a'},
{'fio':'d','age':'b','club':'a','igpo':'a'},
{'fio':'e','age':'b','club':'a','igpo':'a'}]

'''n = int(input("Введите количество игроков: "))
for i in range(n):
    pl = dict()
    pl["fio"] = str(input("Введите ФИО {} игрока: ".format(i + 1)))
    pl["age"] = str(input("Введите возраст {} игрока: ".format(i + 1)))
    pl["club"] = str(input("Введите клуб {} игрока: ".format(i + 1)))
    pl["igpo"] = str(input(
    "Введите хоккейную статистику (И.Г.П.О) {} игрока: ".format(i + 1)))
    players.append(pl)
    print("\n")'''
print(players)
fio = str(input("Введите ФИО игрока для поиска: "))
lookfor2(fio,players)
print(players)


'''res = ('i',"lookfor1", "lookfor2")
#res.append([get_time(lookfor1, fio, players),
#get_time(lookfor2, fio, players)])
format_str = "{:<15}" * len(res)
print(format_str.format(*res))
for r in (10,100,1000,10000,100000,1000000,10000000,100000000):
	for i in range(r):
		players.append({'fio':i,'age':i,'club':i,'igpo':i})
	print(format_str.format(r,get_time(lookfor1, players[-10]['fio'],
	players),get_time(lookfor2, players[-10]['fio'], players)))
	players=[]'''

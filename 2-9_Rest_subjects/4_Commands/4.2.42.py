import random
amount_players=int(input('Enter amount of players: '))
players=[['' for j in range(4)] for i in range(amount_players)]
n=1
for k in players:
    print(n,'player')
    n+=1
    k[0]=input('Enter the player\'s name: ')
    k[1]=int(input('Enter the player\'s age: '))
    k[2]=int(input('Enter the player\'s score: '))
    k[3]=input(
    'Enter the player\'s e-mail. If it isn\'t, press Enter: ')
mini=players[0][1]
mini_name=players[0][0]
for k in players:
    if k[1]<mini:
        mini=k[1]
        mini_name=k[0]
maxi=0
for k in players:
    if k[2]>=maxi:
        maxi=k[2]
        maxi_name=k[0]
count=0
for k in players:
    if k[3]=='':
        count+=1
print('the youngest player is', mini_name)
print('the player with the best score is', maxi_name)
print('Amount of players without e-mail:', count)

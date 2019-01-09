import random
amount = 4
champ1=[random.randint(0,5) for i in range(amount)]
champ2=[random.randint(0,5) for i in range(amount)]
print(champ1, champ2)
print('first championship: {}\nsecond championship:\
 {}\n total: {}'.format(sum(champ1),sum(champ2),sum(champ1+champ2)))

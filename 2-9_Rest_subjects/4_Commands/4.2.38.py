import random
amount = random.randint(28,31)
temp=[random.randint(-15,15) for i in range(amount)]
minustemp=[i for i in temp if i>=0]
plustemp=[i for i in temp if i not in minustemp]
print('negative temperature: {}\npositive temperature:\
 {}'.format(minustemp, plustemp))

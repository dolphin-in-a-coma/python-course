import random
amount = 60
price=[random.randint(2,25) for i in range(amount)]
print(price)
number=1
mini=price[0]
for i in price:
    if i<mini:
        mini=i
        number=1
    elif i==mini:
        number+=1
print('min price: {}, \
amount of cheap books: {}'.format(mini,number))

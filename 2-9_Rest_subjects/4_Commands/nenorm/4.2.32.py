import random
n=1
lst=[]
lst1=[]
print('Enter a list of numbers, to complete \
enter any letter')
c=input('first number: ')
while c.replace('.', '', 1).replace('-', '', 1).isdigit():
    lst.append(float(c))
    c=input('next number: ')
print(not all(lst))

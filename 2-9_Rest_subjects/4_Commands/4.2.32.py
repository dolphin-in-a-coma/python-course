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
for i in lst:
    if i > 0:
        lst1.append(i)
lst2=[i for i in lst if i>0]
for i in lst2:
    n*=i
print(lst, lst1, lst2, sep='\n')
print('arifmetic mean: ', sum(lst1)/len(lst1),
'\ngeometric mean: ', n**(1/len(lst2)))

import random
amount = int(input('amount of workers: '))
salary=[random.randint(100,20000) for i in range(amount)]
print(salary)
mini=salary[0]
maxi=salary[0]
maxin=1
mimin=1
for i in range(amount):
    if salary[i]<mini:
        mini=salary[i]
        minin=i+1
    elif salary[i]>maxi:
        maxi=salary[i]
        maxin=i+1
print('max salary: {}, number of worker: {}\n\
min salary: {}, number of worker: {}'.format(maxi,maxin,mini,minin))

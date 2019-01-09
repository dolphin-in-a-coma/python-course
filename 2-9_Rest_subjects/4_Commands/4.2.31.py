import random
length=int(input('length of lists = '))
l1=[]
for i in range(length):
    l1.append(random.randint(-1000,1000)*2)
l2=[random.randint(-1000,1000)*2 for i in range(length)]
l1_plus=[i for i in l1 if i>0]
l2_minus=[i for i in l1 if i<0]
print('list 1: {}\nlist 2: {}\nsum of positive elements: \
{}\nsum of negative elements: {}'.format(l1,l2,sum(l1_plus),sum(l2_minus)))

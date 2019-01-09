n=int(input('n='))
import random
maxi=-1000
mini=1000
for i in range(n):
    x=random.uniform(-1000,1000)
    print('x{} = {:>2}'.format(i+1,x))
    if x>maxi:
        maxi=x
    if x<mini:
        mini=x
print('\n'+60*'-'+'\n')
print("max: ",maxi,"\nmin: ",mini)

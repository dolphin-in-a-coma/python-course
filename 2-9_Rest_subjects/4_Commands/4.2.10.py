x=int(input('число ='))
count=i=0
while x!=0:
    count+=x%10
    x//=10
    i+=1
print('сумма =', count,'\nколичество цифр =', i)

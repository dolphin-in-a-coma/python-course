count = 0
amount = 1
count = x = int(input('первый член='))
while True:
    if x==0:
        break
    x = int(input('следующий член='))
    amount+=1
    count+=x
print('sum =', count, '\namount =', amount)

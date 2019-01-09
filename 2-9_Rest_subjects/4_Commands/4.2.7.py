count = 0
amount = 1
count = x = int(input('первый член='))
while x != 0:
    x = int(input('следующий член='))
    amount+=1
    count+=x
print('sum =', count, '\namount =', amount)

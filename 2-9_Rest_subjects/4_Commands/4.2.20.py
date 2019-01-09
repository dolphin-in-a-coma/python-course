n=int(input('0<n<=27\nn = '))
print('sum of numeral = {}:'.format(n))
for a in range(100, 1000):
    quant=a%10+(a//10)%10+a//100
    if quant==n:
        print(a)

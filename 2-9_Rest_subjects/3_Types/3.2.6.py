print('вхождение корня ax + b = 0 в отрезок')
a=int(input('a='))
b=int(input('b='))
m=int(input('начало отрезка='))
n=int(input('конец отрезка='))
x=-b/a
print('x =',x, end=' ')
if m<=x<=n:
    print('', end='') #как убрать
else:
    print('не', end=' ')
print('входит в отрезок [{},{}]'.format(m,n))      


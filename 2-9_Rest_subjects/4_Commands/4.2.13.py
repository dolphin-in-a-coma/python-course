a=int(input('a='))
b=int(input('b='))
n=1
if a>b:
    n=-n
summa=sum(range(a,b,n))+b
print('сумма =',summa)
mul=1
for i in range(a,b,n):
    mul*=i
mul*=b
print('произведение =', mul)
print('сред. арифм. =', summa/(len(range(a,b,n))+1))
sum_sq=0
for i in range(a,b,n):
    sum_sq+=i**2
sum_sq+=b**2
print("сумма квадратов =",sum_sq)

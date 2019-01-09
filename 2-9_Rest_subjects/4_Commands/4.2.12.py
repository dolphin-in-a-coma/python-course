a=int(input('a='))
b=int(input('b='))
n=1
if a>b:
    n=-n
for i in range(a,b,n):
    print(i,end=' ')
print(b,'\n')
for i in range(b,a,-n):
    print(i)
print(a)

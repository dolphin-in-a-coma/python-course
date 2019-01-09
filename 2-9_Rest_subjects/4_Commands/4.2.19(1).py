a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b:
    p=range(b,a)
else:
    p=range(a,b)
for i in p:
    if i%c==0:
        print(i)

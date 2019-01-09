n=int(input('n='))
f=1
s=1
while f<n and s<n:
    f=s+f
    s=f+s
if n==f or n==s:
    print('n is Fibonacci number')
else:
    print('n is not of Fibonacci number')

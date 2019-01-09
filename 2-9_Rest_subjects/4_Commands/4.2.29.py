print('primes:')
i=n=0
flag=0
while n!=100:
    i+=1
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        print(i)
        n+=1
        print(n)
    else:
        flag=0
    

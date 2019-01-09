print('x^2+y^2=k^2')
for x in range(1,31):
    for y in range(1,31):
        k=(x**2+y**2)**0.5
        if 1<=k<=30 and k-int(k)<0.0000000001:
            print('x = {:>2}, y = {:>2}, k = {:>2}'.format(x,y,int(k)))

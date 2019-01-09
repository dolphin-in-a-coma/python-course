print('ax^2+bx+c=0')
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a == 0:
    print('а=0')
else:
    d=b**2-4*a*c
    if d<0:
        print(None)
    elif d==0:
        print('x=',-0.5*b/a)
    else:
        print('x1={}\nx2={}'.format((-b-d**0.5)/(2*a),(-b+d**0.5)/(2*a)))


x=float(input("x="))
y=float(input("y="))
if x>=0:
    if y>=0:
        print('1st quarter')
    else:
        print('2nd quarter')
elif y>=0:
    print('4th quarter')
else:
    print('3rd quarter')
    

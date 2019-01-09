amount=15
wast=0
n=float(input('1st number: '))
for i in range(2,16):
    p=float(input('{} number: '.format(i)))
    if n>p:
        if wast==0:
            wast=i
    else:
        n=p
if wast==0:
    print('sequence is increasing')
else:
    print('sequence isn\'t increasing')
    print('position of waste number:', i)

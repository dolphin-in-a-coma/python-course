amount=int(input('amount='))
wast=0
n=float(input('1st student: '))
for i in range(2,amount+1):
    p=float(input('{} student: '.format(i)))
    if n<p:
        wast=i
    else:
        n=p
if wast==0:
    print('list is decreasing')
else:
    print('list isn\'t decreasing')

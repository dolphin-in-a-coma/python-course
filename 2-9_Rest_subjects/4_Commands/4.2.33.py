import random
lst=[]
print('Enter a list of numbers, to complete \
enter any letter')
c=input('first number: ')
while c.replace('.', '', 1).replace('-', '', 1).isdigit():
    lst.append(float(c))
    c=input('next number: ')
flagp=True
flagm=True
flag0=False
for i in lst:
    if i>0:
        flagm=False
    if i<0:
        flagp=False
    if i==0:
        flag0=True
lstp=[]
lstm=[]
for i in lst:
    if i>0:
        lstp.append(True)
        lstm.append(False)
    elif i<0:
        lstp.append(False)
        lstm.append(True)
   
print('Flags Method\nall the elements of negative: {}\n\
all the elements of positive: {}\nthere is zero: {}'.format(flagm, flagp, flag0))
print('Any/All Method\nall the elements of negative: {}\n\
all the elements of positive: {}\nthere is zero: {}'.format(all(lstm), all(lstp), any(lst)))

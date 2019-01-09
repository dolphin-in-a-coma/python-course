total=distance=10
for i in range(2,11):
    distance+=distance/10
    total+=distance
    print(i,'-й день: ', distance,' km', sep='')
print('\nвсего =',total,'km')

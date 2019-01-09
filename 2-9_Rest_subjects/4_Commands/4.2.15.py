amount=int(input('amount='))
total=0
for i in range(amount):
    mass=int(input('mass of {} subject ='.format(i+1)))
    total+=mass
print('total mass =',total)

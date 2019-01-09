amount=int(input('amount='))
total=t_area=0
for i in range(amount):
    area=int(input('{} area ='.format(i+1)))
    product=int(input('{} productivity ='.format(i+1)))
    total+=area*product
    t_area+=area
average=total/t_area
print('total wheat = {}\naverage productivity= {}'.format(total, average))

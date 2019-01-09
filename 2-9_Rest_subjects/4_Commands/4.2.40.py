import random
rows=int(input('Enter amount of rows: '))
seatsinrow=int(input('Enter amount of seats in row: '))
seats = [[random.randint(0, 1) for seat_num in range(seatsinrow)]
for row_num in range(rows)]
print(seats)
row=int(input('Enter the number of row: '))
seat=int(input('Enter the number of seat: '))
no=''
if seats[row-1 ][seat-1]:
    no='not '
print('This seat is {}available'.format(no))

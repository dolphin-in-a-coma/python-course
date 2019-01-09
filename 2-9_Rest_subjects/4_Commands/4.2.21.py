amount=int(input('amount of students = '))
b_height=0
g_height=0
boys=0
girls=0
for i in range(amount):
    t=int(input('height of {} student = '.format(i+1)))
    if t>=0:
        g_height+=t
        girls+=1
    else:
        b_height-=t
        boys+=1
print("average boy's height: ",b_height/boys)
print("average girl's height: ",g_height/girls)

import random
time1=time2=removal1=removal2=0
for i in range(24):
    team=random.randint(1,2)
    minute=random.randint(2,4)
    if minute==3:
        minute=5
    elif minute==4:
        minute=10
    print('{:>2} removal - {} team - {:>2} minute'.format(i+1,team,minute))
    if team==1:
        removal1+=1
        time1+=minute
    else:
        removal2+=1
        time2+=minute
print('\n'+60*'-'+'\n')
print("removals of 1st team: ",removal1,"/ntime of removals:",time1)
print("\nremovals of 2nd team: ",removal2,"/ntime of removals:",time2)

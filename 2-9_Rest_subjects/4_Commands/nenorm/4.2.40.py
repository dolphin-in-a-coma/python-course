import random
groups=8
courses=4
students = [[random.randint(10, 50) for group in range(groups)]
for course in range(courses)]
total=0
for course in students:
    total+=(sum(course))
mean=total/(groups*courses)
print('the average amount of stutends in group is ', mean)

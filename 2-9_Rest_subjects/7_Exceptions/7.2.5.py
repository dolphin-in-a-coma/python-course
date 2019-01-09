# Дан список случайных вещественных чисел от [-10 до 10].
# Удалить из списка все отрицательные числа.

# Логическая ошибка: при удалении элемента из списка цикл пропускает
# cледующий элемент 

import random

n = int(input("Сколько элементов в списке? "))
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)

i=0
while i<len(nums):
    if nums[i] < 0:
        del nums[i]
        i-=1
    i+=1

print(nums)

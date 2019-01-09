# Дан список чисел. Найти минимальную сумму соседних 2-х чисел.
# Синтаксическая ошибка: min - встроенная фунция
# Логическая ошибка: for i in range(len(nums)): индекс выходит за пределы списка

import random

N_MAX = 10
RANGE_MIN = 1
RANGE_MAX = 100
nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)

print(nums)

min1 = RANGE_MAX * 2
for i in range(len(nums) - 1):
    min1 = min(nums[i] + nums[i + 1], min1)
print(min1)

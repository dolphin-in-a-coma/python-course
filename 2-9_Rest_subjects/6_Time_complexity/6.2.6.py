
import random
import time

def get_time(func, data):

    time1 = time.time()
    ret = func(data)
    time2 = time.time()
    return round((time2-time1) * 1000.0, 2)

#сложность - O(N)
#находит максимальный элемент списка через стандартную функцию
def foo1(nums):
    return max(nums)

#сложность - O(NlogN)
#сортирует список по возрастание, возвращает последний
def foo2(nums):
    nums.sort()
    return nums[-1]

res = [["i", "1 (мс.)", "2 (мс.)"]]
for i in (100, 1000, 10000, 100000):
    data = [random.randint(0, 50000) for j in range(i)]
    res.append([i,
                get_time(foo1, data),
                get_time(foo2, data),])

format_str = "{:>10}" * len(res[0])
for r in res:
    print(format_str.format(*r))

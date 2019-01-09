import random

#функция сортирует по возрастанию
#сложность = O(N^2)

def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

a = random.sample(range(100), 10)
foo(a)

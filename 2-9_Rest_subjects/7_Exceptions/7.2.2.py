#Вывести список простых чисел на отрезке [`a`, `b`].
#Логическая ошибка: if c == 2, не позволяет включить 1, должно находится
#во внешнем цикле
#Логическая ошибка: range(a, b), b не входит в диапазон
#Логическая ошибка: c=0, требуется обнуление c на каждом шагу 
#итерации for i in range(a, b+1)

a, b = [int(x) for x in input().split()]

res = []
for i in range(a, b+1):
    c=0
    for j in range(i):
        if i % (j + 1) == 0:
            c += 1
    if c <= 2:
        res.append(i)

print(res)

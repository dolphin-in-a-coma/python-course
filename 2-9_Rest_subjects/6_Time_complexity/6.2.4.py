#функция возвращает список, содержащий простые числа от
#1 до введенного включительно
#сложность = O(N^2)

def foo(n):
    # n - число
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1

        if divisors == 0:
            res.append(i)

    return res

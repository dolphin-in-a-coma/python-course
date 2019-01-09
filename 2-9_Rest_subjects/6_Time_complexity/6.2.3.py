#функция возвращает сумму цифр
#сложность = O(N)

def foo(s):
    # s - строка
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

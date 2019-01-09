#функция переводит int в str
#сложность = O(N)

def foo(i):
    # i - число
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result

print(foo(int(input())))

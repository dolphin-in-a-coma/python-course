# Дано положительное целое число `n`.
# Напишите программу, которая выводит на экран сумму цифр этого числа,
# меньших 5. Если в числе нет цифр, меньших 5, требуется на экран вывести 0.

# Логическая ошибка: digit = n // 10, // вместо %
# Логическая ошибка: if digit < 7, 7 вместо 5
# Логическая ошибка: c = c + 1, 1 вместо digit
# Логическая ошибка: print(digit), digit вместо c

n = int(input("Введите число "))
c = 0
while n > 0:
    digit = n % 10
    if digit < 5:
        c = c + digit
    n //= 10
print(c)

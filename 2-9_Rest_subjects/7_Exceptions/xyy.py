def fact(x):
    """Вернуть факториал 'x'.

    Не передавайте числа больше 15 во избежание переполнения памяти.
    """
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(int(input())))

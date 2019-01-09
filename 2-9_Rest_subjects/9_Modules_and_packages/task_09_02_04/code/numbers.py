"""Module for working with numbers.

   -Great Common Divisor
   -Least Common Multiple
   -Is Prime
   -Inverse
   -Root
"""


def gcd(first, second):
    """Вернуть НОД для целых чисел 'first' и 'second'.

    Исключения:
      - ValueError: first или second равны 0.
      - TypeError: first или second - любой тип кроме int.

    Пример: gcd(54, 24) == 6.
    """
    if not (first and second):
        raise ValueError('Arguments mustn\'t equal zero!')
    if not (isinstance(first, int) and isinstance(second, int)):
        raise TypeError('Arguments must be int!')

    answer = 1
    for i in range(1, min((abs(first), abs(second))) + 1):
        if first % i == 0 and second % i == 0:
            answer = i
    return answer


def lcm(first, second):
    """Вернуть НОК для чисел 'first' и 'second'.

    Исключения:
      - ValueError: first или second равны 0.
      - TypeError: first или second - любой тип кроме int.

    Пример: lcm(4, 6) == 12
    """
    if not (first and second):
        raise ValueError('Arguments mustn\'t equal zero!')
    if not (isinstance(first, int) and isinstance(second, int)):
        raise TypeError('Arguments must be int!')

    maxn = max(abs(first), abs(second))
    minn = min(abs(first), abs(second))
    for i in range(1, minn + 1):
        if (i * maxn) % minn == 0:
            return i * maxn

    return maxn * minn


def is_prime(number):
    """Вернуть True, если 'number' - простое число, иначе False.

    Исключения:
      - TypeError: number - любой тип кроме int.
      - ValueError: number - не натуральное число.

    Пример: is_prime(7) == True
    """
    if number <= 0:
        raise ValueError('Number must be natural!')
    if not isinstance(number, int):
        raise TypeError('Number must be int!')

    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return (count == 2)


def inverse(number):
    """Вернуть число, обратное 'number' (1 / number).

    Исключения:
      - ZeroDivisionError: number - 0.
      - TypeError: number - любой тип кроме int, float.

    Пример: inverse(2) == 0.5
    """
    if not number:
        raise ZeroDivisionError('Number mustn\'t equal zero!')
    if not isinstance(number, (int, float)):
        raise TypeError('Number must be int or float!')

    return 1 / number


def root(number, power=2):
    """Вернуть корень 'power' степени из 'number'.

    Исключения:
      - ValueError: power - меньше единицы.
      - TypeError: number - любой тип кроме int, float.
      - TypeError: power - любой тип кроме int, float.

    Пример: root(9) == 3.0
    """
    if power < 1:
        raise ValueError('Power must equal 1 or greater!')
    if not isinstance(number, (int, float)):
        raise TypeError('Number must be int or float!')
    if not isinstance(power, (int, float)):
        raise TypeError('Power must be int or float!')

    return number**(1 / power)

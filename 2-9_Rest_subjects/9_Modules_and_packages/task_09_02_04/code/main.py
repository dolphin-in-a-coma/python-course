import numbers
import random

if __name__ == "__main__":
    ...

    try:
        first = random.randrange(-100, 200)
        second = random.randrange(20)
        print('first:', numbers.first)
        print('second:', numbers.second)
        print('gcd:', numbers.gcd(first, second))
        print('lcm:', numbers.lcm(first, second))
        print(
            'is prime:\n\tfirst: {}\n\tsecond: {}'.format(
                numbers.is_prime(first),
                numbers.is_prime(second)))
        print('inverse:\n\tfirst: {:.4}\n\tsecond: {:.4}'.format(
            numbers.inverse(first), numbers.inverse(second)))
        print('root:', round(numbers.root(first, second), 4))

    except Exception as err:
        print('Error occured during execution:', err)
        print('Type:', type(err))

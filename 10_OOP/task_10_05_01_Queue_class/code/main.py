# Программирование на языке высокого уровня (Python).
# Задание task_10_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

from queue import Queue

if __name__ == "__main__":
    print('Инициализация трех экземпляров класса Queue:')
    q1 = Queue()
    lst = list(range(12))
    q2 = Queue(*lst)
    q3 = Queue.from_string('1, "abc", {"a" : 1}')
    print(q1, q2, q3, sep = '\n', end = '\n\n')
    print('Сохрание q3 в формате json и загрузка данных из json в q1: ')
    q3.save('Queue.json')
    q1.load('Queue.json')
    print(q1, end = '\n\n')
    print('Метод pop() над q1: ')
    print(q1.pop())
    print(q1.pop())
    print(q1, end = '\n\n')
    print('Метод push() над q1:')
    q1.push('new')
    print(q1, end = '\n\n')
    print('Длина q1:')
    print(len(q1), end = '\n\n')
    print('Сложение q1 и q2:')
    print(q1 + q2, end = '\n\n')
    print('Умножение q1 на 4:')
    print(q1 * 4, end = '\n\n')

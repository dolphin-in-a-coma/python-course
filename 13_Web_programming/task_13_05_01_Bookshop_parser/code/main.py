# Программирование на языке высокого уровня (Python).
# Задание task_13_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

# url1: https://www.books.ru/books/kritika-chistogo-razuma-3818000/
# url2: https://www.books.ru/books/konstitutsiya-rossiiskoi-federatsii-4186537/

from book_parser import WebBookParser
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        bp = WebBookParser(sys.argv[1], sys.argv[2])
    else:
        args = input('Введите url с книгой и путь итогового файлов, разделяя запятыми: ').split(',')
        for i in args:
            i.strip()
        bp = WebBookParser(*args)
    bp.get_info()
    print('Файл готов.')

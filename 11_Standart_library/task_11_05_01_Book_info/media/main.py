# Программирование на языке высокого уровня (Python).
# Задание task_11_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com


from book_parser import BookParser
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        bp = BookParser(sys.argv[1], sys.argv[2])
    else:
        args = input('Введите имя исходного и итогового файлов, разделяя запятыми: ').split(',')
        for i in args:
            i.strip()
        bp = BookParser(*args)
    bp.get_info()
    print('Файл готов.')

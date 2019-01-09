# Программирование на языке высокого уровня (Python).
# Задание task_11_05_02. Вариант 3
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

from game import PlainGame
import os.path
import sys

if __name__ == "__main__":
    log_file = os.path.join(
    os.path.dirname(os.path.realpath(sys.argv[0])),'log_file.txt')
    pg = PlainGame(log_file)
    pg.play()

# Программирование на языке высокого уровня (Python).
# Задание task_11_05_03. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

#info.json
from backup_manager import Backuper
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        arg = input('Введите имя json файла с настройками: ')
    bu = Backuper(arg)
    bu.backup()
# проверить, если я буду запускать модуль из другой папки могу ли я использовать отн путь

import sys
import os
import datetime
from print_c import print_c

# Лог-файл
# Имя лог-файла задано в коде - "log.txt" в папке приложения
app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
log_filename = os.path.join(app_path, "log.txt")

agency_name = 'Ur Ma'


def log(message):
    """Вывести на экран 'message' с указанием текущего времени
    формате 0001-01-01 00:00:00 (год, месяц, число, часы, минуты, секунды):
      - на экран;
      - в лог-файл (дописать в конец файла).
    """
    text = datetime.datetime.now().replace(microsecond = 0).isoformat(sep = ' ') + ' | {}\n'.format(message)
    print_c(text)
    filename = 'log.txt'
    with open(filename, 'a') as fl:
        fl.write(text + '\n')

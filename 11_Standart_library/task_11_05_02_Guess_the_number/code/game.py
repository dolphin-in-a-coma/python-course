# Программирование на языке высокого уровня (Python).
# Задание task_11_05_02. Вариант 3
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

import re
import datetime

class PlainGame:
    ''' self._current - (int)
        self._from - (int)
        self._to - (int)
        self._log_file - (str)
    '''
    
    def __init__(self, log_file):
        self._current = None
        self._from = None
        self._to = None
        self._log_file = log_file
        
    def play(self):
        t1 = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        print('Добро пожаловать в игру "Угадай число"!\n'\
        'Время начала игры:', t1 + '\n')
        print('Правила довольно просты: Вы загадываете любое число,'\
        ' я отгадываю.\n'\
        'Итак, начнем. Загадывайте. Как загадаете, нажмите Enter.')
        input()
        self._get_range()
        print('\nТеперь я попытаюсь угадать Ваше число. Если я сделаю это,\n'\
        'введите "+" или "да", в противном случае введите что-либо другое.')
        
        for i in range(self._from, self._to + 1):
            self._next()
            if self._get_answer():
                break

        t2 = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        attempts = self._current - self._from + 1
        self._log(t1, t2, attempts)
        print('Игра закончена. Время окончания: {}\n'\
        'Количество попыток: {}'.format(t2, attempts))
    
    def _get_range(self):
        args = input('Отлично. Теперь через пробел'\
        ' введите границы интервала,\n'\
        'в котором находится Ваше число: ').split()
        self._from, self._to = (int(i) for i in args)
    
    def _get_answer(self):
        ''' Return (bool)
        '''
        ans = input('Вы загадали число {}? - '.format(self._current)).upper()
        if ans in ('ДА', '+'):
            return True
        return False
    
    def _next(self):
        if self._current is None:
            self._current = self._from
        else:
            self._current +=1
    
    def _check_log(self):
        ''' Return number of last game.
        '''
        try:
            count = r'(\d+)' + r'Игра №'[::-1]
            with open(self._log_file) as fl:
                text = fl.read()[::-1]
            return int(re.search(count, text).group(1)[::-1])
        except Exception as err:
            return 0
    
    def _log(self, t1, t2, attempts):
        ''' t1 - (str) start time (str)
            t2 - (str) end time
            attempts - (int) 
        '''
        number = self._check_log()
        number += 1
        text = 'Игра №{}\n'\
        '   Начало игры: {}\n'\
        '   Конец игры: {}\n'\
        '   Количество попыток: {}\n\n'.format(number, t1, t2, attempts)
        
        with open(self._log_file, 'a') as fl:
            fl.write(text)


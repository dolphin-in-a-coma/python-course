# Программирование на языке высокого уровня (Python).
# Задание task_11_05_03. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

# в json разные слэши

import re
import shutil
import json
import datetime
import os

class Backuper:
    ''' self._json_file - (str) путь файла с json структурой
        self._info - десериализованная структура из self._json_file
    '''
    def __init__(self, json_file):
        self._json_file = json_file
        self._info = None
        
    def __str__(self):
        return 'Backuper v 0.1.0.1'
    
    def backup(self):
        ''' Запускает копирывание.
        '''
        t1 = datetime.datetime.now()
        errs = []
        count = 0
        
        self._get_info()
        self._log('Копирование файлов.\n'
        'Время начала: {}\n'
        'Файлы: '.format(t1))
        try:
            for i in self._info['projects']:
                project = self._info['projects'][i]
                for folder in project['folders']:
                    os.makedirs(folder['dest'],exist_ok = True)
                    for fl in os.scandir(folder['src']):
                        try:
                            fl = fl.name
                            if not (self._check_regex
                            (project['options']['template'],fl) and
                            self._confirm(project['options']['confirm'], fl)):
                                continue
                    
                            self._copy(fl, folder['src'], folder['dest'])
                            count+=1
                            self._log('\t' + fl)
                        except Exception as err:
                            errs.append('{1}, {0}'.format(str(err), type(err)))
        except Exception as err:
            errs.append('{1}, {0}'.format(str(err), type(err)))
        t2 = datetime.datetime.now()
        td = (t2 - t1).total_seconds()
        self._log('Всего файлов скопированно: {}\n'
        'Время завершения: {}\n'
        'Затраченное время: {}'.format(count, t2, td))
        if errs:
            self._log('Во время работы возникли ошибки:\n\t' + '\n\t'.join(errs))
                    
    def _get_info(self):
        ''' Получает структуру из self._json_file
        '''
        with open(self._json_file) as f:
            self._info = json.loads(f.read())

    def _log(self, msg):
        ''' Выводит на экран и записывает в файл для логирования.
        '''
        with open(self._info['log_filename'], 'a') as f:
            print(msg, file = f)
        print(msg)
    
    @staticmethod
    def _check_regex(template, filename):
        ''' template - (str) регулярное выражение или (bool) False
            filename - (str) имя файла
            Возвращает True, если filename соответствует template, или 
            template отсутсвует.
        '''
        # print(template)
        # print(filename)
        return bool(not template or re.search(template, filename) and
        re.search(template, filename).group(0) == filename)
    
    @staticmethod
    def _confirm(confirm_it, filename):
        ''' confirm_it - (bool) нужно ли подтверждение
            Возвращает True, если confirm_it == False, или дан
            положительный ответ.
        '''
        if confirm_it:
            ans = input('Вы хотите скопировать {}?\n'
                        '"+" или "да" для подтверждения: '.format(filename))
            if ans.strip().lower() not in ('+', 'да'):
                return False
        return True
        
    @staticmethod
    def _copy(filename, src, dest):
        ''' filename - (str) имя файла
            src - (str) путь исходной директории
            dest - (str) путь итоговой директории
            Совершает копирование файла или папки.
            Если папка существует, вызывает FileExistsError.
        '''
        src_filename = os.path.join(src, filename)
        dest_filename = os.path.join(dest, filename)
        if os.path.isfile(src_filename):
            shutil.copy2(src_filename, dest_filename)
        else:
            shutil.copytree(src_filename, dest_filename)
            

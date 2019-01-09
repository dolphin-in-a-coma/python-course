# Программирование на языке высокого уровня (Python).
# Задание task_11_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com


import re
import json

class BookParser:
    ''' self._html_file - (str) имя html файла
        self._text_file - (str) имя итогового файла
        self._info - (dict) структура из self._create_info()
    '''
    def __init__(self, html_file, text_file):
        self._html_file = html_file
        self._text_file = text_file
        self._info = []
    
    def __str__(self):
        return 'BookParser v. 0.0.1'
    
    def _create_info(self):
        ''' Сохраняет в (dict) self._info информацию о книге.
        '''
        title = r'var product_title = "([\w:\. ]+)"'
        author = r'<td class="book-info">\s+<p class="author">\s+([\w\., ]*[\w.])\s+<\/p>'
        # разделять и по точке с запятой (нет)
        price = r'<meta itemprop="price" content="(\d+)">'
        isbn = r'<td class="label">ISBN:<\/td>\s+<td>([\d-]+)<\/td>'
        publishing = r'<td class="label">Издательство:<\/td>\s+<td><a href=".+" title=".+">([\w -]+)<\/a><\/td>'
        pages = r'<td class="label">Объём:<\/td>\s+<td>(\d+) страниц<\/td>'
        # верхнее выражение возможно нужно подправить
        year = r'<td class="label">Дата выхода:<\/td>\s+<td>\D+(\d+)<\/td>'
        
        with open(self._html_file, 'rb') as fl:
            text = fl.read().decode('utf-8')
        
        self._info = dict(title = re.search(title, text).group(1),
        author = re.search(author, text).group(1),
        price = re.search(price, text).group(1),
        isbn = re.search(isbn, text).group(1),
        publishing = re.search(publishing, text).group(1),
        pages = re.search(pages, text).group(1),
        year = re.search(year, text).group(1))
        
        
    def _save_text(self):
        ''' Сохраняет self._info как json в self._txt_file.
        '''
        json_text = json.dumps(self._info, ensure_ascii=False, indent=4)
        with open(self._text_file, 'w') as fl:
            fl.write(json_text)
            
    def get_info(self):
        ''' Получает информацие о книге в self._info и сохраняет как json в self._txt_file.
        '''
        self._create_info()
        self._save_text()

from queue import Queue
import json

class QueueCollection():
    ''' класс-контейнер для Queue()
    '''
    
    def __init__(self, *data):
        ''' self._data - (list) список объектов Queue().
        '''
        self._data = []
        if data:
            for i in data:
                if not isinstance(i, type(Queue())):
                    raise TypeError('Аргументы должны принадлежать классу Queue()')
                self._data.append(i)
        # можно ли вообще обратиться к аргс, если здесь ничего нет
    
    def __str__(self):
        ''' Возвращает строку вида: "QueueCollection: (...)."
        '''
        res = 'QueueCollection: ({})'
        elements = ''
        for i in self._data:
            elements += ', ' + str(i) if elements else str (i)
            # проверить команду сверху
            # посмотреть как работает join с none и списком объектов queue - не работает
        return res.format(elements)
        
    def __getitem__(self, key):
        ''' key - индекс или срезовые индексы.
        
            Возвращает срез или элемент по индексу.
        
        '''
        # if not (isinstance(key, int) and key < len(self.data) and -key <= len(self.data)):
        #    raise IndexError
        # можно было не писать верхнее
        # вопрос про минус перед переменной 
        
        if isinstance(self._data[key], type(Queue())):
            return self._data[key]
        return QueueCollection(*self._data[key])
    
    '''def __getitem__(self, slice(a, b)):
        return self._data[a:b] '''  
    
    def add(self, value):
        ''' value - (Queue()).
        
            Добавляет новый элемент в контейнер.
        '''
        if not isinstance(value, type(Queue())):
            raise TypeError('Элемент должен принадлежать классу {}'.format(type(Queue)))
        self._data.append(value)
    
    def remove(self, index):
        ''' index - (int) номер элемента.
        
            Удаляет элемент по номеру index.
        '''
        self._data.pop(index)
    
    def save(self, filename):
        '''filename - (str) имя файла
        
        Сериализирует объект в формат json и сохраняет в filename.
        '''
        as_dict = dict(_data = [])
        for i in self._data:
            as_dict['_data'].append({'_list':i._list})
        with open(filename, 'w') as fl:
            fl.write(json.dumps(as_dict))
    
    def load(self, filename):
        ''' filename - (str) имя файла
        
        Десериализирует объект из filename из формата json.
        Возвращает объект класса Queue().
        ''' 
        with open(filename) as fl:
            as_dict = json.loads(fl.read())
        if not (isinstance(as_dict, dict) and len(as_dict) == 1 and '_data' in as_dict):
            raise TypeError('json не содержит объект {}'.format(type(Queue())))
        # проверку наверное нужно изменить 
        data = []
        for i in as_dict['_data']:
            data.append(Queue(*i['_list']))
        self._data = data

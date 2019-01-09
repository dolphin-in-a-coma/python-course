import json

class Queue:
    def __init__(self, *tpl):
        ''' self._list - (list).'''
        self._list = list(tpl)
        
    def __str__(self):
        ''' Возвращает строку вида 'Queue: (...)'.'''
        return 'Queue: {}'.format(tuple(self._list))
    
    def __len__(self):
        ''' Возвращает длину объекта.'''
        return len(self._list)

    def __add__(self, other):
        # почему не работает __concat__?
        ''' other - объект класса Queue().
            
            Возвращает новый объект, добавляя элементы other к self.
        '''
        if not isinstance(other, self.__class__):
            raise TypeError("Невозможно добавить {} к {}".format(type(other), self.__class__))
        return Queue(*(self._list + other._list))
    
    def __mul__ (self, other):
        ''' other - int.
        
            Возвращает новый объект, повторяя элементы из self other раз.
        '''
        if not isinstance(other, int):
            raise TypeError('Нвозможно умножить {} на {}'.format(self.__class__, type(other)))
        return Queue(*self._list * other)
        
    def push(self, item):
        '''Добавляет новый элемент item в конец очереди.'''
        self._list.append(item)
    
    def pop(self):
        '''Возвращает первый элемент, удаляя его из очереди.'''
        return self._list.pop(0)
        
    def remove(self):
        '''Очищает очередь.'''
        self._list = []
    
    def reverse(self):
        '''Меняет направление очереди.'''
        self._list = self._list[::-1]
    
    @classmethod
    def from_string(cls, str_value):
        ''' str_value - (str) элементы через запятую
        
            Возвращает объект класса Queue(), состоящий из элементов
            из str_value
        '''
        str_like_json = '[{}]'.format(str_value)
        lst = json.loads(str_like_json)
        return Queue(*lst)
    
    def save(self, filename):
        ''' filename - (str) имя файла
        
        Сериализирует объект в формат json и сохраняет в filename.
        '''
        res = {'_list' : self._list}
        with open(filename, 'w') as fl:
            fl.write(json.dumps(res))

    def load(self, filename):
        ''' filename - (str) имя файла
        
        Десериализирует объект из filename из формата json.
        Записывает его.
        ''' 
        with open(filename, 'r') as fl:
            res = json.loads(fl.read())
        if not (isinstance(res, dict) and len(res) == 1
                and isinstance(res['_list'], list)):
                raise TypeError('json-объект не содержит {}'.format(self.__class__))
        self._list = res['_list']

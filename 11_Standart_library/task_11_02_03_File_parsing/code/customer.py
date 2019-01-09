import re
import datetime


class Customer:
    """Класс Customer представляет клиента.

    Атрибуты экземпляра класса:
      - self.info: словарь-информация о клиенте; содержит следующие ключи:
        - f (str): фамилия клиента;
        - i (str): имя клиента;
        - o (str): отчество клиента;
        - birthday (datetime.date): дата рождения;
        - polis_type (str): тип полиса;
        - polis_price (int): цена оформленного полиса.
    """

    REGEX = r'^(?P<f>[а-яё]+)\s+(?P<i>[а-яё]+)\s+(?P<o>[а-яё]+)\s+'\
        '(?P<birthday>\d?\d[\.\/\-]\d?\d[\.\/\-]\d?\d?\d{2})\s+'\
        '(?P<polis_type>недвижимость|транспорт|здоровье|путешествия)\s+'\
        '(?P<polis_price>\d+)$'
    DATE_FORMAT = '%d/%m/%Y'

    def __init__(self, info):
        """Инициализация класса.

        Аргументы:
          - info (dict): словарь-информация о клиенте (формата 'self.info')

        Необходимые проверки:
          - info - словарь и содержит необходимые ключи;
          - значения в словаре имеют нужный тип.

        Исключения:
          - ValueError - если не все проверки успешны.

        Действия:
          - установить self.info;
          - Ф, И, О и тип полиса должны быть с большой буквы.
        """
        if not (isinstance(info, dict) and len(info) == 6 and
                isinstance(info.get('f', None), str) and
                isinstance(info.get('i', None), str) and
                isinstance(info.get('o', None), str) and
                isinstance(info.get('birthday', None), datetime.date) and
                isinstance(info.get('polis_type', None), str) and
                isinstance(info.get('polis_price', None), int)):
            raise ValueError('Из данного словаря нельзя создать объект')
        self.info = info.copy()
        for i in ['f', 'i', 'o', 'polis_type']:
            self.info[i] = info[i].title()

    def __str__(self):
        """Вернуть строковое представление клиента.

        Формат:
          'Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.'.

        Для вывода суммы с разделителем тысяч используйте заполнитель {:,}.
        """
        return '{0[f]} {0[i]} {0[o]} {1} {0[polis_type]} {0[polis_price]:,}'\
               ' руб.'.format(
                              self.info,
                              self.info['birthday'].strftime(self.DATE_FORMAT))

    @classmethod
    def from_string(cls, str_value):
        """Создать и вернуть экземпляр класса Customer из строки 'str_value'.

        1. Используя регулярное выражение, проверить, что 'str_value' содержит
           информацию о клиенте:
              - ФИО клиента в произвольном регистре; в качестве разделителя
                может быть использован пробел или знак табуляции;
              - Дата рождения:
                    - день и месяц могут быть указаны с наличием/отсутствием
                      ведущего 0;
                    - год может содержать 2 или 4 цифры;
                    - в качестве разделителя может быть использован
                      '.', '/' или '-'.
              - Тип полиса: "Транспорт", "Недвижимость",
                            "Путешествия" или "Здоровье";
              - Сумма: целое число.

              Пример: 'Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.'

           Неплохим вариантом будет использовать именованные аргументы,
           совпадающие с ключами в 'self.info', таким образом, их будет просто
           получить через 'match.groupdict()'.

           Возбудить ValueError, если не удается получить информацию из строки.

        2. При обнаружении информации, сформировать словарь найденных данных:
           - откорректировать год до 4-х знаков;
           - все числовые значения преобразовать в соответствующие типы.

        3. Создать экземпляр класса и вернуть в качестве результата.
        """
        a = re.search(Customer.REGEX, str_value.strip(),
                      re.UNICODE | re.IGNORECASE | re.MULTILINE)
        if a:
            dct = a.groupdict()
            dct['polis_price'] = int(dct['polis_price'])
            dct['birthday'] =\
                datetime.date(int('19' + dct['birthday'][-2:]),
                              int(dct['birthday'][3:5].strip('-/.')),
                              int(dct['birthday'][0:2].strip('-/.')))
            return Customer(dct)
        else:
            raise ValueError('Невалидная строка.')

    def __getattr__(self, key):
        """Вернуть значение атрибута 'key'.

        Благодаря специальному методу '__getattr__' обращение к
        характеристике клиента, например, фамилии будет выгляеть
        как
           Customer.f,
        вместо
           Customer.info['f']
        т.е. нет необходимости объявлять отдельные методы/свойства для
        "красивого" доступа к значениям 'self.info'.
        """
        if key in self.info:
            return self.info[key]
        raise AttributeError(key)

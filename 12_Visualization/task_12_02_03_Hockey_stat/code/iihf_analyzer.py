import csv
import datetime
import calendar
import locale
import matplotlib.pyplot as plt
import numpy as np


class IihfAnalyzer:
    """Класс IihfAnalyzer выполняет:
      - формирование итогового списка партий с подсчетом голосов;
      - построение круговой диаграммы суммарного количества голосов.

    Поля:
      - self._data: список словарей вида:

        [
            {'cohort': 1976, 'position': 'Защитник', 'country': 'RUS',
             'birth': datetime.datetime(1976, 5, 18, 0, 0),
             'bmi': 24.5434623813002, 'year': 2001,
             'club': 'anaheim mighty ducks', 'age': 24.952772073922,
             'side': 'L', 'height': 185.0, 'name': 'tverdovsky oleg',
             'no': 10, 'weight': 84.0},
            ...
        ]

      - self.fields (tuple): данные о хоккеистах (по возрастанию):
          ('age', 'birth', 'bmi', 'club', 'cohort', 'country', 'height',
           'name', 'no', 'position', 'side', 'weight', 'year')

      - self.years (tuple): годы проведения ЧМ (по возрастанию):
          (2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
           2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016)

      - self.countries (tuple): страны-участники ЧМ (по возрастанию):
          ('AUT', 'BLR', 'CAN', 'CZE', 'DEN', 'FIN',
           'FRA', 'GER', 'HUN', 'ITA', 'JPN', 'KAZ', 'LAT', 'NOR', 'POL',
           'RUS', 'SLO', 'SUI', 'SVK', 'SWE', 'UKR', 'USA')

    Методы: см. отдельно.
    """

    PLAYER_POSITION_NAME = {
        "G": "Вратарь", "D": "Защитник", "F": "Нападающий"
    }

    def __init__(self):
        """Инициализация класса.

        Действия:
          - инициализировать 'self._data'.
          - инициализировать 'self.fields'.
          - инициализировать 'self.years'.
          - инициализировать 'self.countries'.
        """
        self._data=[]
        self.fields=()
        self.years=()
        self.countries=()

    def __str__(self):
        """Вернуть строку - анализируемые данные.

        Формат:

        Набор данных (6292):
         - поля: age, birth, bmi, club, cohort, country, height, name,
           no, position, side, weight, year;
         - годы: (2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
           2010, 2011, 2012, 2013, 2014, 2015, 2016);
         - страны-участники: ('AUT', 'BLR', 'CAN', 'CZE', 'DEN', 'FIN',
           'FRA', 'GER', 'HUN', 'ITA', 'JPN', 'KAZ', 'LAT', 'NOR', 'POL',
           'RUS', 'SLO', 'SUI', 'SVK', 'SWE', 'UKR', 'USA').
        """
        res = 'Набор данных ({0}):'.format(len(self._data))
        res+='\n - поля: '+', '.join(self.fields)+';'
        res+='\n - годы: {};'.format(self.years)
        res+='\n - страны-участники: {}.'.format(self.countries)

        return res

    def load(self, filename):
        """Загрузить файл 'filename' с результатами выборов.

        Параметры:
          - filename (str): имя файла.

        По результатам загрузки:

        1) 'self._data' должен содержать писок словарей вида:

        [
            {'cohort': 1976, 'position': 'Защитник', 'country': 'RUS',
             'birth': datetime.datetime(1976, 5, 18, 0, 0),
             'bmi': 24.5434623813002, 'year': 2001,
             'club': 'anaheim mighty ducks', 'age': 24.952772073922,
             'side': 'L', 'height': 185.0, 'name': 'tverdovsky oleg',
             'no': 10, 'weight': 84.0},
            ...
        ]

        2) 'self.fields', 'self.years', 'self.countries' должны быть
            заполнены на основании 'self._data'.

        Особенности:
            - функция не обрабатывает возникающие исключения;
            - нестроковые данные (числа, даты и др.) должны быть
              преобразованы в соответствующие типы;
            - позиция игрока должна быть заменена на соответствующий
              элемент IihfAnalyzer.PLAYER_POSITION_NAME.
        """
        with open(filename, encoding='utf-8') as fh:
            data = list(csv.DictReader(fh))
        self.fields=tuple(sorted(data[0].keys()))
        self._data=data
        
        self.countries=[]
        self.years=[]
        for n, i in enumerate(data):
            if i['country'] not in self.countries:
                self.countries.append(i['country'])
            if int(i['year']) not in self.years:
                self.years.append(int(i['year']))
            for j in ['bmi', 'weight', 'height', 'age']:
                self._data[n][j]=float(i[j])
            for j in ['no', 'cohort', 'year']:
                self._data[n][j]=int(i[j])
            self._data[n]['birth']=datetime.datetime(int(i['birth'][:4]),
                                                    int(i['birth'][5:7]),
                                                    int(i['birth'][-2:]))
            self._data[n]['position']=IihfAnalyzer.PLAYER_POSITION_NAME[i['position']]
        self.countries=tuple(sorted(self.countries))
        self.years=tuple(sorted(self.years))
            

    def _get_player_id(self, player):
        """Вернуть кортеж, однозначно определяющий игрока.

        Считается, что однозначно игрока характеризует
        имя, страна, дата рождения и позиция.

        Параметры:
          - player (dict): информация об игроке:

              {'cohort': 1976, 'position': 'Защитник', 'country': 'RUS',
                 'birth': datetime.datetime(1976, 5, 18, 0, 0),
                 'bmi': 24.5434623813002, 'year': 2001,
                 'club': 'anaheim mighty ducks', 'age': 24.952772073922,
                 'side': 'L', 'height': 185.0, 'name': 'tverdovsky oleg',
                 'no': 10, 'weight': 84.0}

        Результат:
          - кортеж: ('tverdovsky oleg',
                     datetime.datetime(1976, 5, 18, 0, 0),
                     'RUS',
                     'Защитник').
        """
        return (player['name'], player['birth'],
                player['country'], player['position'])

    def _get_players_without_dublicates(self, data):
        """Вернуть копию 'data' без дубликатов.

        Дубликатом считается игрок с одинаковым значением
        self._get_player_id().

        Параметры:
          - data (list): список игроков формата 'self._data'.

        Результат:
          - data (list): список словарей вида:

            {'birth': datetime.datetime(1976, 5, 18, 0, 0),
             'name': 'tverdovsky oleg',
             'country': 'RUS',
             'position': 'Защитник'}
        """
        res=[]
        for i in data:
            uniq=self._get_player_id(i)
            if uniq not in res:
                res.append(uniq)
        for i in range(len(res)):
            res[i] = {'name':res[i][0], 'birth':res[i][1],
                      'country':res[i][2], 'position':res[i][3]}
        return res

    def get_wc_participation_stats(self):
        """Вернуть распределение хоккеистов по количеству участий в ЧМ.

        Результат: словарь вида

            {
              ('jagr jaromir', datetime.datetime(1972, 2, 15, 0, 0),
               'CZE', 'Нападающий'): 8,
              ...
            }
              , где
            - ключ: кортеж - id игрока (self._get_player_id());
            - значение: количество участий в ЧМ.

        Если 'self._data' не содержит данных, возбудить AssertionError.
        """
        assert self._data, 'Нет данных!'
        
        res={}
        for i in self._data:
            uniq=self._get_player_id(i)
            if res.get(uniq, False):
                res[uniq]+=1
            else:
                res[uniq]=1
        return res

    def get_trend_data(self):
        """Вернуть наборы данных 'год выступления - роста игрока'
        для каждой позиции (вратарь, защитник, нападающий).

        Результат: список вида

            {'Защитник': {
              'x': [2001, 2001, 2001, 2001],
              'y': [185.0, 188.0, 182.0, 178.0]
             },
             'Вратарь': ...
            }, где:
            - ключ 'x': год выступления хоккеиста;
            - ключ 'y': рост хоккеиста.

        Если 'self._data' не содержит данных, возбудить AssertionError.
        """
        assert self._data, 'Нет данных!'
        
        res={}
        for i in self.PLAYER_POSITION_NAME.values():
            res[i]={'x':[],'y':[]}
            for player in self._data:
                if player['position']==i:
                    res[i]['x'].append(player['year'])
                    res[i]['y'].append(player['height'])
        return res

    def get_birthday_month_stats(self):
        """Вернуть распределение хоккеистов по месяцам
        рождения по всему набору данных, исключая одних и
        тех же игроков, выступающих в разные годы.

        Результат: словарь вида

            {1: 269, 2: 264, 3: 284, 4: 259, 5: 224, 6: 210,
             7: 255, 8: 189, 9: 193, 10: 167, 11: 172, 12: 149}
            , где
            - ключ: номер месяца;
            - значение: количество родившихся игроков.

        Если 'self._data' не содержит данных, возбудить AssertionError.
        """
        assert self._data, 'Нет данных!'
        
        data=self._get_players_without_dublicates(self._data)
        res={i:0 for i in range(1,13)}
        for i in data:
            res[i['birth'].month]+=1
        return res

    def get_position_stats(self):
        """Вернуть распределение позиций (вратарь, защитник, нападающий)
        между хоккеистами по всему набору данных, исключая одних и
        тех же игроков, выступающих в разные годы.

        Результат: список вида

            {'Вратарь': 47, 'Нападающий': 225, 'Защитник': 122}, где
            - ключ: позиция;
            - значение: количество игроков.

        Если 'self._data' не содержит данных, возбудить AssertionError.
        """
        assert self._data, 'Нет данных!'
        
        data=self._get_players_without_dublicates(self._data)
        
        res={i:0 for i in self.PLAYER_POSITION_NAME.values()}
        for i in data:
            res[i['position']]+=1
        return res
        

    def _make_plot(self):
        """Генерирует изображение, не отображая его.

        Изображение должно включать несколько диаграмм по горизонтали,
        количество которых равно длине 'self._data'.

        Параметры:
          - country(str): страна из 'self.countries'.

        Результат:
          - fig: matplotlib.figure.Figure.

        Особенности:
          - если 'self._data' не содержит данных, возбудить AssertionError.
        """
        assert len(self._data) > 0, "Нет данных для анализа"

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=2,
                                                     figsize=(12, 6))

        title = "Хоккейная статистика ЧМ: " + str(self.years)
        fig.canvas.set_window_title(title)
        fig.suptitle(title)

        self._stats1(self.get_wc_participation_stats(), ax1)
        self._stats2(self.get_trend_data(), ax2)
        self._stats3(self.get_birthday_month_stats(), ax3)
        self._stats4(self.get_position_stats(), ax4)

        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.85,
                            wspace=0.2, hspace=0.45)

        return fig

    def _stats1(self, data, ax):
        """Отобразить распределение хоккеистов по количеству участий в ЧМ.

        Гистограмма.

        Параметры:
          - data (dict): структура из метода
                         'self.get_wc_participation_stats()';
          - ax (Axes): координатная плоскость для рисования.

        Гистограмма должна быть нормирована (параметр normed=True).
        """
        ax.set_title('Рапределение хоккеистов по количеству участий в ЧМ')
        ax.set_xlabel('Количество ЧМ')
        ax.set_ylabel('Доля')
        lst = list(data.values())
        bins = list(range(1,max(lst)+1))
        labels = bins
        ax.hist(lst, color='r', edgecolor = 'black', bins = bins) 

        # Подписи посередине прямоугольника
        ax.set_xticks([x + 0.5 for x in bins])
        ax.set_xticklabels(labels)

    def _stats2(self, data, ax):
        """Отобразить тренды изменения роста на протяжении всех ЧМ
        для каждой позиции (вратарь, защитник, нападающий).

        График.

        Параметры:
          - data (dict): структура из метода 'self.get_trend_data()';
          - ax (Axes): координатная плоскость для рисования.

        Для формирования линии тренда (линейная аппроксимация) используйте
        следующий код:
            x_trend = np.polyfit(x, y, 1)
            y_trend = np.poly1d(x_trend)
        где
            x, y - исходные наборы значений лет и роста соответственно;
            x_trend, y_trend - наборы значений тренда, которые можно
                               нарисовать с помощью ax.plot().
        """
        ax.set_title('Тренды изменения роста игрока для каждой позиции')
        ax.set_xlabel('Год ЧМ')
        ax.set_ylabel('Рост (см.)')
        
        x_trend = np.polyfit(data['Вратарь']['x'],data['Вратарь']['y'], 1)
        y_trend = np.poly1d(x_trend)
        ax.plot(data['Вратарь']['x'], y_trend(data['Вратарь']['x']))
        
        print(x_trend)
        print(y_trend)
        
                
        '''newdata={}
        for pos in self.PLAYER_POSITION_NAME.values():
            newdata['pos']['']
            for i,year in enumerate(data[pos]['x']):
                newdata['']'''
                        
        #print(data)
        
        #x_trend, y_trend = [], []
        
        '''positions = list(self.PLAYER_POSITION_NAME.values())
        for pos in positions:
            x_trend.append(np.polyfit(data[pos]['x'],data[pos]['y'],1))
            y_trend.append(np.poly1d(x_trend[-1]))'''
        
        '''ax.set_xlim(2001,2016)
        ax.set_ylim(170,190)'''
        '''ax.plot(x_trend[1], y_trend[1])
        ax.plot(x_trend[2], y_trend[2])'''
        
        '''lst = list(data.values())
        bins = list(range(1,max(lst)+1))
        labels = bins
        #lst1 = [x/sum(lst) for x in lst]
        ax.hist(lst, color='r', normed=True, edgecolor = 'black', bins = bins) '''

    def _stats3(self, data, ax):
        """Отобразить распределение хоккеистов по месяцам
        рождения по всему набору данных, исключая одних и
        тех же игроков, выступающих в разные годы.

        Столбчатая диаграмма (вертикальная).

        Параметры:
          - data (dict): структура из метода
                         'self.get_birthday_month_stats()';
          - ax (Axes): координатная плоскость для рисования.

        Русские аббревиатуры месяцев можно отобразить, переключив локаль
        (locale.setlocale()).
        """
        ax.set_title('Распределение хоккеистов по месяцам рождения')
        ax.set_ylabel('Чел.')
        
        locale.setlocale(locale.LC_ALL, 'Russian')
        tick_label = [datetime.date(2000,x,1).strftime('%b') for x in range(1,13)]
        # какой-то бред
        ax.bar(range(1,13),[data[i] for i in range(1,13)], tick_label = tick_label)

    def _stats4(self, data, ax):
        """Отобразить распределение позиций (вратарь, защитник, нападающий)
        между хоккеистами по всему набору данных, исключая одних и
        тех же игроков, выступающих в разные годы.

        Круговая диаграмма.

        Параметры:
          - data (dict): структура из метода 'self.get_position_stats()';
          - ax (Axes): координатная плоскость для рисования.
        """
        ax.set_title('Распределение позиций между хоккеистами')
        
        newdata = sorted(data.items(), key = lambda x: 1/x[-1])
        # x[-1] не может же быть равен нулю, да?
        ax.pie(x = [i[-1] for i in newdata],
        autopct = lambda x: '{:.1f}%'.format(x),
        labels = [i[0] for i in newdata])
        ax.set_aspect('equal')

    def show_plot(self):
        """Создать изображение и показать его на экране."""
        self._make_plot()
        plt.show()
    
    @staticmethod
    def _make_tuple(field, key, data):
        field=[]
        for i in data:
            if i[key] not in field:
                field.append(i[key])
        field=tuple(field)
        print(field)

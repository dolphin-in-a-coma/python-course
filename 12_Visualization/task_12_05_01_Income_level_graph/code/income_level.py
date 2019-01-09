# Программирование на языке высокого уровня (Python).
# Задание task_12_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

import csv
import matplotlib
import matplotlib.pyplot as plt

class AverageIncome:
    ''' 
        self._csffile - (str) путь к csv-файлу
        self._data - (list) структура из self._read_data()
    '''
    def __init__(self, csvfile):
        self._csvfile = csvfile
        self._read_data()
        
    def _read_data(self):
        ''' 
            читает csv-файл,
            возвращает (list)  
        '''
        with open(self._csvfile, 'r', encoding="utf-8-sig") as fl:
            self._data = list(csv.DictReader(fl, delimiter = ';'))
            
    def _get_average_income(self):
        ''' 
            определяет среднюю зарплату по округам
            возвращает (dict)
        '''
        counties = {}
        for i in self._data:
            if i['Федеральный округ'] in counties:
                counties[i['Федеральный округ']].append(int(i['Денежные доходы в расчете на душу населения, руб.//месяц']))
            else:
                counties[i['Федеральный округ']] = [int(i['Денежные доходы в расчете на душу населения, руб.//месяц'])]
        return {key:sum(counties[key])/len(counties[key]) for key in counties.keys()}
        
    def _get_county_income(self, county = 'Дальневосточный федеральный округ'):
        ''' 
            определяет среднюю зарплату по областям в указаном округе
            county - (str) округ для анализа
            возвращает (dict)
        '''
        regions = {}
        for i in self._data:
            if i['Федеральный округ'] == county:
                regions[i['Субъект РФ']] = i['Денежные доходы в расчете на душу населения, руб.//месяц']
        return regions
        
    def _make_plot(self):
        ''' 
            составляет графики 
        '''
        assert self._data, 'Нет данных!'

        title = 'Средний доход по округам и областям РФ.'
        
        fig, (ax1, ax2) = plt.subplots(ncols = 2)
        fig.canvas.set_window_title('Уровень денежных доходов населения РФ')
        fig.suptitle(title)
        
        income_dict = self._get_average_income()
        labels = sorted(income_dict.keys(),key = lambda a: income_dict[a], reverse = True)
        values = [income_dict[x] for x in labels]
        
        ax1.pie(values, autopct = lambda x: int(x*sum(values)*0.01))
        ax1.set_aspect('equal')
        ax1.set_ylim(-0.6,2.1)
        ax1.set_xlim(-0.6,2.1)
        ax1.legend(labels,loc='upper right')
        ax1.set_title('Средний доход по округам.')

        income_dict = self._get_county_income()
        labels = sorted(income_dict.keys(),key = lambda a: income_dict[a], reverse = True)
        values = [income_dict[x] for x in labels]
        try:
            labels[labels.index('Республика Саха (Якутия)')]='Якутия'
            labels[labels.index('Еврейская автономный область')] = 'Еврейская АО'
            labels[labels.index('Чукотский автономный округ')] = 'Чукотский АО'
        except Exception:
            pass
        
        ax2.barh(range(1,1+len(values)), values, tick_label = labels, color = '#DE92D3')
        ax2.set_aspect(10000)
        ax2.set_title('Средний доход по областям.')
    
    def show_plot(self):
        ''' 
            рисует графики
        '''
        self._make_plot()
        plt.show()    

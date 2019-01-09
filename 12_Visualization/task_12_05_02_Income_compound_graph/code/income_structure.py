# Программирование на языке высокого уровня (Python).
# Задание task_12_05_02. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com


import csv
import matplotlib
import matplotlib.pyplot as plt

class IncomeStructure():
    ''' 
        self._csffile - (str) путь к csv-файлу
        self._data - (list) структура из self._read_data()
    '''
    def __init__(self,csvfile):
        self._csvfile = csvfile
        self._read_data()
    
    def _read_data(self):
        ''' 
            читает csv-файл,
            возвращает (list)  
        '''
        with open(self._csvfile, encoding = 'utf-8-sig') as fl:
            self._data = list(csv.DictReader(fl, delimiter = ';'))
    
    def _get_income_structure(self):
        ''' 
            определяет структуру по округам
            возвращает (dict)
        '''
        structure = {}
        for i in self._data:
            lst = [i['Доходы от предпринимательской деятельности'], i['Оплата труда'], i['Социальные выплаты'], i['Доходы от собственности'],i['Другие доходы (включая скрытую зарплату)']]
            lst = [float(k.replace(',','.')) for k in lst]
            if i['Федеральный округ РФ'] in structure:
                structure[i['Федеральный округ РФ']].append(lst)
            else:
                structure[i['Федеральный округ РФ']] = [lst]
        return {key:
                    [sum(i[j] for i in structure[key]) / len(structure[key]) for j in range(5)]
                for key in sorted(structure.keys(), key = lambda a: structure[a])}
        
    def _get_county_structure(self, county = 'Дальневосточный федеральный округ'):
        ''' 
            определяет структуру доходов по областям в указаном округе
            county - (str) округ для анализа
            возвращает (dict)
        '''
        structure = {}
        for i in self._data:
            if i['Федеральный округ РФ'] == county:
                lst = [i['Доходы от предпринимательской деятельности'], i['Оплата труда'], i['Социальные выплаты'], i['Доходы от собственности'],i['Другие доходы (включая скрытую зарплату)']]
                lst = [float(j.replace(',','.')) for j in lst]
                structure[i['Субъект РФ']] = lst
        return structure
                
                
                
    def _make_plot(self):
        ''' 
            составляет графики 
        '''
        def make_ax(ax, structure, title):
            keys = structure.keys()
            for n, i in enumerate(keys):
                bottom = [sum(structure[i][:k]) for k in range(5)]
                ax.barh([n]*5, structure[i], left = bottom, color = color)
            #kostyl
            ax.barh(range(len(structure)), [0]*len(structure), tick_label = keys)
            #ax.set_xlim(0,100)
            ax.set_aspect(2.5)
            ax.set_title(title)
        
        labels = ['Доходы от предпринимательской деятельности','Оплата труда','Социальные выплаты','Доходы от собственности','Другие доходы (включая скрытую зарплату)']
        color = ['#DF8CA0','#BB8CDF','#8CC8DF','#8CDFB1','#CBDF8C']
        title = 'Структура доходов России'
        ax1_title = 'Структура доходов по федеральным округам'
        ax3_title = 'Структура доходов в ДВФО'
        
        fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3)
        fig.canvas.set_window_title(title)
        
        ax2.pie([1]*5,colors = color)
        ax2.set_aspect('equal')
        ax2.set_xlim(-10000,10000)
        ax2.legend(labels, loc = 'center')
        
        make_ax(ax1, self._get_income_structure(), ax1_title)  
        make_ax(ax3, self._get_county_structure(), ax3_title)
                
    def show_plot(self):
        ''' 
            рисует графики
        '''
        self._make_plot()
        plt.show()

# Программирование на языке высокого уровня (Python).
# Задание task_12_05_03. Вариант 6
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

import csv
import json
import matplotlib
import matplotlib.pyplot as plt

class GDPAnalizer():
    def __init__(self, options, data):
        self._read_data_and_options(options, data)
    def _read_data_and_options(self, options, data):
        with open(options) as fl:
            self._options = json.loads(fl.read())
        with open(data, encoding = 'utf-8-sig') as fl:
            self._data = list(csv.DictReader(fl, delimiter = ','))
    
    def _get_gdp_dinamic(self, ax):
        period = range(self._options['plot']['period'][0],self._options['plot']['period'][-1]+1)
        counries = self._options['plot']['countries']
        n = 0
        
        for i in sorted(self._data, key = lambda a: len(a[str(period[-1])]) and float(a[str(period[-1])]), reverse = True):
            if i['Country Name'] in counries:
                n+=1
                gdp = []
                label = ''
                for j in period:
                    gdp.append(i[str(j)])
                gdp[-1]
                ax.plot(period, gdp, label = i['Country Name'])
        ax.legend(loc = 'upper left')
        ax.set_xlim(period[0]-10, period[-1])
        ax.set_title('Динамика ВВП')
        ax.set_xlabel('Год')
        ax.set_ylabel('ВВП, трлн. $')
        
    def _get_hist(self, ax, bins = 10):
        x = [float(i[str(self._last_year())]) for i in self._data if i[str(self._last_year())] and i['Country Name'] != 'High income' and i['Country Name'] != 'North America']
        print(x)
        n, bins_array, patches = ax.hist(x, bins = bins, color = '#DE92D3', edgecolor = 'black', weights = x)
        print(max(x))
        ax.set_xlim(0, max(x))
        labels = ''
        for i in range(bins):
            if n[i]:
                labels+=('№{0}. От ${2:.0f} до ${3:.0f} млрд., Сумма: ${1:.0f} млрд.\n'.format(i+1, n[i]/10**9, bins_array[i]/10**9, bins_array[i+1]/10**9))
        print(labels)
        ax.legend([labels.strip()], loc = 'best')
        ax.set_title('Распределение ВВП')
        ax.set_xlabel('ВВП, трлн. $')
        ax.set_ylabel('Сумма ВВП по группам, трлн. $')
        
    def _get_pie(self, ax):
        lst=[[],[]]
        for i in sorted(self._data, key = lambda a: len(a[str(self._last_year())]) and float(a[str(self._last_year())])):
            if i['Country Name'] in self._options['pie']['countries'] and i[str(self._last_year())]:
                lst[0].append(i['Country Name'])
                lst[1].append(i[str(self._last_year())])
        ax.pie(lst[1], autopct = lambda a: (a>4 and '{:.1f}%'.format(a)) or '')
        ax.legend(lst[0], loc = 'upper right', bbox_to_anchor=(1.6, 1.3))
        ax.set_aspect('equal')
        ax.set_xlim(-1,2.5)
        ax.set_title('Structure of {} GDP.'.format(self._options['pie']['name']))
                
                
    def show_plot(self):
        fig, ((ax1,ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)
        fig.canvas.set_window_title('GDP')
        ax3.remove()
        self._get_gdp_dinamic(ax1)
        self._get_hist(ax4, 10)
        self._get_pie(ax2)
        plt.show()
    
    def _last_year(self):
        years = sorted([int(i) for i in self._data[0].keys() if i.isdigit()], reverse = True)
        for i in years:
            for j in self._data:
                if j[str(i)]:
                    return i

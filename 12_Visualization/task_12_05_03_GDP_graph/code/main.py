# Программирование на языке высокого уровня (Python).
# Задание task_12_05_03. Вариант 6
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

#options.json
#world_bank_gdp_data_2017-02-01.csv

from gdp_analyzer import GDPAnalizer

if __name__ == "__main__":
    options = 'options.json'
    data = 'world_bank_gdp_data_2017-02-01.csv'
    gdpa = GDPAnalizer(options, data)
    gdpa.show_plot()

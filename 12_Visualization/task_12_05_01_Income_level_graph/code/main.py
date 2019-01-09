# Программирование на языке высокого уровня (Python).
# Задание task_12_05_01. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

#data_2017-12-27.csv
from income_level import AverageIncome

if __name__ == "__main__":
    ai = AverageIncome('data_2017-12-27.csv')
    ai._read_data()
    #print(ai._get_average_income())
    #print(ai._get_county_income())
    ai.show_plot()
    

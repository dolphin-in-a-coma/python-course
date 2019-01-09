# Программирование на языке высокого уровня (Python).
# Задание task_12_05_02. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

#data_2017-12-27

from income_structure import IncomeStructure

if __name__ == "__main__":
    i_s = IncomeStructure('data_2017-12-27.CSV')
    i_s.show_plot()

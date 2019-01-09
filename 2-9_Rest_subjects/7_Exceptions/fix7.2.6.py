#  При вводе unemployed и employed могут быть введены не корректные
#  данные или отрицательные числа
#  В функции get_unemployment_rate() может произойти деление на ноль

def get_unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы в долях 1.

       Расчет по формуле: УБ = Б / (З + Б).
	
	В фунцкцию могут быть посланы отрицательные, нулевые либо 
	аргументы неподходщих типов.
	
		"""
    assert unemployed>=0 and employed>=0, "Аргументы не могут быть\
отрицательными!"
    return unemployed / (unemployed + employed)


try:
    print("== Расчет уровня безработицы. Версия 0.1. ==")
    unemployed = int(input("Введите кол-во безработных (чел.): "))
    employed = int(input("Введите кол-во занятых (чел.): "))
    unemployment_rate = get_unemployment_rate(unemployed, employed)
    print("Уровень безработицы = {:.1%}".format(unemployment_rate))

except ValueError:
    print("Аргументы должны быть целыми числами!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except Exception as err:
    print("Произошла ошибка!")
    print("Тип:", type(err))
    print("Описание:", err)

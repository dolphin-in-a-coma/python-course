# Отрицательная степень или >997, вызывающая бесконечную рекурсию
# Некорректные аргуметы

def power(x, y=2):
    """Вернуть x^y."""
    assert 0<=y<=997,'Степень должна быть неотрецательной и меньше 998!' 
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
try:
	print("Я умею возводить 'x' в степень 'y'!")
	x = int(input("x="))
	y = int(input("y="))
	print(power(x, y))
except ValueError:
	print('Аргументы должны быть целыми числами!')
except AssertionError as err:
	print(err)
except Exception as err:
	print("Произошла ошибка!")
	print("Тип:", type(err))
	print("Описание:", err)

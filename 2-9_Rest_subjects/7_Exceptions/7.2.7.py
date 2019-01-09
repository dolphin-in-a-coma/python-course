# Протабулируйте заданную функцию f() на отрезке [-k; k] c шагом h,
# округлив ответ до 2-х знаков после запятой.

#Деление на ноль в функции
#Шаг может быть равен нулю, тогда цикл будет бесконечен
#Граница и шаг могут оказаться разных знаков, и цикл будет бесконечен


def f(x): 
	try:
		return x**0.5 / (x + 2) - 3
	except ZeroDivisionError:
		print("На ноль делить нельзя!")
		raise
	except Exception as err:
		print("Произошла ошибка!")
		print("Тип:", type(err))
		print("Описание:", err)
		raise
try: 
	k = int(input("Введите границу интервала [-k; k]: "))
	h = float(input("Введите шаг табуляции: "))

	assert h!=0, 'Шаг не должен быть равен нулю!'
	assert k/h>0, 'Граница и шаг должны быть одного знака!'

	x = -k
	print("{:>5} {:>5}".format("x", "f(x)"))
	while x <= k:
		print("{:5.2f} {:5.2f}".format(x, f(x)))
		x += h
		
except ValueError:
	print(
	"Граница должна быть целой! Аргументы должны быть числами!")
except AssertionError as err:
	print(err)
except Exception as err:
	print("Произошла ошибка!")
	print("Тип:", type(err))
	print("Описание:", err)

# Дан список ФИО. Найти наиболее часто встречаемое отчество.

# Отсутсвие отчества
# Некорректное количество человек, <=0, с плавающей точкой или не число

try:
	n = int(input("Введите кол-во человек: "))

	assert n>0, 'Введите натуральное число!'
	
	fio_count = {}
	for i in range(n):
		fio = input("Введите ФИО через пробел: ").split()

		fio_count[fio[2]] = fio_count.get(fio[2], 0) + 1

	print(sorted(fio_count.items(), key=lambda item: item[1])[-1][0])

except IndexError:
	print('ФИО должны состоять из трех слов через пробел!')
except ValueError:
	print('Введите натуральное число!')
except AssertionError as err:
	print(err)
except Exception as err:
	print("Произошла ошибка!")
	print("Тип:", type(err))
	print("Описание:", err)

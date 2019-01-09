# В программе хранится словарь вступительных экзаменов вида Предмет=Баллы.
# Узнать, проходит ли абитуриент на специальность, если нужно сдать
# все перечисленные экзамены с не меньшим кол-вом баллов.

# Вводимые баллы могут быть меньше 0 или больше 100, оказаться
# десятичными дробями или оказаться не числом
# Название экзамена может отсутствовать в словаре
# Не все экзамены могут быть сданы
# Введенная строка может также иметь неверный формат(отсутсвие | )

#Имена переменных, написанные кириллицей - нежелательны
 
try:
	необходимые_экзамены = {
		"Информатика": 80,
		"Математика": 85,
		"Русский язык": 75
	}

	print("""Для определения возможности поступления, необходима информация о Вас.

Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
	""")

	сданные_экзамены = {}


	while True:
		ввод = input("").strip()
		if ввод == "":
			break

		ввод = [x.strip() for x in ввод.split("|")]
		сданные_экзамены[ввод[0]] = int(ввод[1])
		assert int(ввод[1])>=0 and int(ввод[1])<=100,\
		'Баллы должны быть натуральным числом, не больше 100'
	assert len(сданные_экзамены)==3,\
	'Введены не все обязательные экзамены'
	
	print(сданные_экзамены)

	ok = True
	for сданный_экзамен, баллы in сданные_экзамены.items():
		if необходимые_экзамены[сданный_экзамен] > баллы:
			ok = False
			break

except ValueError:
	print('Баллы должны быть натуральными числами!')
except IndexError:
	print('Используйте |')
except KeyError:
	print('Вводите наименования из:', необходимые_экзамены, sep='\n')
except AssertionError as err:
	print(err)
except Exception as err:
	print("Произошла ошибка!")
	print("Тип:", type(err))
	print("Описание:", err)
else:
	print("Вы можете к нам поступить!" if ok else "Увы...")
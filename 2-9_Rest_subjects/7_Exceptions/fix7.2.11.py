
# Неположительное или другое некорректное количество баллов
# Отсутствие необходимого количества баллов на счету
# Отсутствие аккаунтов в словаре

def make_payment(accounts, account1, account2, value):
	"""Выполнить перевод 'value' баллов со счета 'account1' на 'account2'.

	Нельзя снимать со счета больше баллов, чем есть.
	"""

	# Ориентируясь на примеры лекций (в частности, 7.1.8 (в)),
	# реализуйте работу функции в виде транзакции
	# (транзакция может быть выполнена либо целиком и успешно, либо не выполнена вообще)
	# см. подробнее: https://ru.wikipedia.org/wiki/Транзакция_(информатика)
	assert accounts[account1]>=value, 'Недостаточно средств!'
	assert value>0, 'Некорректная сумма!'
	accounts[account2]
	accounts[account1] -= value
	accounts[account2] += value

try:
	accounts = {"Василий Иванов": 100, "Екатерина Белых": 1500}
	make_payment(accounts, "Екатерина Белых", "Василий Иванов", 250)
	print(accounts)
except TypeError:
	print('Баллы могут быть только числами!')
except AssertionError as err:
	print(err)
except KeyError as err:
	print('В словаре отсутствует',err)
except Exception as err:
	print("Произошла ошибка!")
	print("Тип:", type(err))
	print("Описание:", err)

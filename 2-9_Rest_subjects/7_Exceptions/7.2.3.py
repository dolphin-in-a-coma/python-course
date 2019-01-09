# Дана информация о проданных билетах на самолет хранится в таблице (билет продан/нет).
# Указать первый ряд, в котором имеется больше всего свободных мест и их количество.

# Логическая ошибка: 'if available_seats_count >= max:', сохраняет 
# последний, а не первый ряд
# Логическая ошибка(притянутая): 'max_row = row_index+1', порядок рядов
# начинается с нуля
# Синтаксическая ошибка: 'max = 0', max - встроенная функция
import random

random.seed(50)

ROWS_MAX = 10
SEATS_MAX = 5

seats = [[random.randint(0, 1) for seat in range(SEATS_MAX)]
                               for row in range(ROWS_MAX)]

for seat in seats:
    print(seat)

max1 = 0
max_row = 0
for row_index, row in enumerate(seats):
    available_seats_count = row.count(0)  # 0 - пусто
    if available_seats_count > max1:
        max_row = row_index+1
        max1 = available_seats_count

print("Ряд: {}, мест: {}".format(max_row, max1))

# Программирование на языке высокого уровня (Python).
# Задание task_10_05_03. Вариант 3
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

from transport import Transport
from transport import WaterTransport
from transport import Vehicle
from transport import Car
from transport import TransportError
import time

if __name__ == "__main__":
    try:
        print('Создать экземпляр Transport.')
        t = Transport('green', 50, 5, 5)
        print(t, end = '\n\n')
        print('Состояние объекта\n'\
        '(находится в движении, сколько м. проехал с момента старта):',
        t.check_condition(), sep ='\n', end = '\n\n')
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
        print('Сесть в объект и поехать, разгоняясь до скорости 40 м/с.')
        t.get_in()
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
        t.go(40)
        print('Состояние:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(2)
        print('Состояние через 2 секунды:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(3)
        print('Состояние через 5 секунд:', t.check_condition(), sep ='\n', end = '\n\n')
        t.stop()
        print('Состояние после остановки:', t.check_condition(), sep ='\n', end = '\n\n')
        print('Количество пасажиров:', t.passengers, sep ='\n', end = '\n\n')
        print('Добавить пасажира.')
        t.add_passenger()
        print('Количество пасажиров:', t.passengers, sep ='\n', end = '\n\n')
        print('Удалить пасажира и выйти из транспорта.')
        t.remove_passenger()
        t.get_out()
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
        
        print('Создать экземпляр WaterTransport.')
        t = WaterTransport('fair wood', 60, 7, 5, 1000)
        print(t, end = '\n\n')
        print('Состояние плота:',
        t.check_condition(), sep ='\n', end = '\n\n')
        print('Сесть в плот и поехать, разгоняясь до скорости 30 м/с, '
              'учитывая обратное течение 10м/c.')
        t.get_in()
        t.go(40, 10)
        print('Состояние:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(2)
        print('Состояние через 2 секунды:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(3)
        print('Состояние через 5 секунд:', t.check_condition(), sep ='\n', end = '\n\n')
        t.stop()
        print('Состояние после остановки:', t.check_condition(), sep ='\n', end = '\n\n')
        print('Вес груза:', t.cargo_weight, sep ='\n', end = '\n\n')
        print('Добавить 300 кг груза.')
        t.add_cargo(300)
        print('Вес груза:', t.cargo_weight, sep ='\n', end = '\n\n')
        print('Покинуть плот.')
        t.get_out()
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
        
        print('Создать экземпляр Vehicle.')
        t = Vehicle(2, 'chromic', 10, 4, 5)
        print(t, end = '\n\n')
        print('Состояние транспорта:',
        t.check_condition(), sep ='\n', end = '\n\n')
        print('Транспорт открыт:', t.opened, sep ='\n', end = '\n\n')
        t.open()
        print('Открыть.','Транспорт открыт:', t.opened, sep ='\n', end = '\n\n')
        print('Сесть и поехать, разгоняясь до скорости 6 м/с.')
        t.get_in()
        t.go(6)
        print('Состояние:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(2)
        print('Состояние через 2 секунды:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(3)
        print('Состояние через 5 секунд:', t.check_condition(), sep ='\n', end = '\n\n')
        t.stop()
        print('Состояние после остановки:', t.check_condition(), sep ='\n', end = '\n\n')
        print('Покинуть транспорт и закрыть.')
        t.get_out()
        t.close()
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
        
        print('Создать экземпляр Car.')
        t = Car(170, 32, 4, 'black', 100, 30, 2)
        print(t, end = '\n\n')
        print('Состояние автомобиля\n'\
        '(едет, сколько проехал, топливо):',
        t.check_condition(), sep ='\n', end = '\n\n')
        t.tank_up(10)
        print('Заправить 10 л.\n'\
              'Состояние после заправки:', 
              t.check_condition(), sep ='\n', end = '\n\n')
        print('Машина открыта:', t.opened, sep ='\n', end = '\n\n')
        t.open()
        print('Открыть.','Машина открыта:', t.opened, sep ='\n', end = '\n\n')
        print('Сесть и поехать, разгоняясь до скорости 100 м/с.')
        t.get_in()
        t.go(100)
        print('Состояние:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(2)
        print('Состояние через 2 секунды:', t.check_condition(), sep ='\n', end = '\n\n')
        time.sleep(3)
        print('Состояние через 5 секунд:', 
        'Вынужденная становка из-за выхода топлива.',
        t.check_condition(), sep ='\n', end = '\n\n')
        print('Состояние после остановки:', t.check_condition(), sep ='\n', end = '\n\n')
        print('Покинуть транспорт и закрыть.')
        t.get_out()
        t.close()
        print('Водитель внутри:', t.driver_inside, sep ='\n', end = '\n\n')
    except TransportError as err:
        print(err)
        


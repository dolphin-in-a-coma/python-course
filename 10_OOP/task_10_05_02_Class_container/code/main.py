# Программирование на языке высокого уровня (Python).
# Задание task_10_05_02. Вариант 8
#
# Выполнил: Рудаков Е. А.
# Группа: ЗЕБЗ-01-16
# E-mail: eugenartemovich@gmail.com

from queue import Queue
from queuecollection import QueueCollection

if __name__ == "__main__":
    print('Инициализация 3-х очередей:')
    q1 = Queue(1)        
    q2 = Queue(1,2,3)    
    q3 = Queue(5,4)    
    print(q1,q2,q3)
    print('\nСоздание контейнера, содержащего эти очереди:')
    qc = QueueCollection(q1,q2,q3)
    print(qc)
    print('\nДобавление нового элемента:')
    qc.add(Queue('a','b'))
    print(qc)
    print('\nУдаление первого элемента:')
    qc.remove(0)
    print(qc)
    print('\nСериализация и сохранение в формате json, затем создание нового объекта и загрузка данных из файла:')
    qc.save('QueueCollection.json')
    new_qc = QueueCollection()
    new_qc.load('QueueCollection.json')
    print(new_qc)
    print('\nПолучение элемента по индексу [-1]:')
    print(new_qc[-1])
    print('\nПолучение среза [::-1]:')
    print(new_qc[::-1])

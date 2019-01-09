from customer import Customer
import statistics
import datetime


class CustomerList:
    """Класс CustomerList представляет список клиентов.

    Атрибуты экземпляра класса:
        - self.customers (list из Customer): список клиентов;
        - self.filename (str): имя файла, из которого были получены клиенты;
        - self.errors (list из str): список строк с ошибками чтения файла.
    """

    def __init__(self):
        """Инициализация класса.

        Создать:
          - 'self.customers', 'self.errors', 'self.filename'.
        """
        self.customers = []
        self.filename = ''
        self.errors = []

    def __str__(self):
        """Вернуть строковое представление класса.

        Возвращает строку со списком клиентов в алфавитном порядке.
        Для печати клиента необходимо использовать его __str__-метод.

        Формат:

        Список клиентов (3):
        1. Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.
        2. Лягушкина Екатерина Олеговна 17/04/1958 Здоровье 15,000 руб.
        3. Смирнова Елена Юрьевна 15/12/1966 Здоровье 15,000 руб.
        """
        res = ''
        for i, customer in enumerate(self.customers):
            res += '\n{}. '.format(i + 1) + str(customer)
        return ('Список клиентов ({}):'.format(len(self.customers)) + res)

    def open(self, filename):
        """Открыть файл 'filename' со списком клиентов.

        Аргументы:
            - filename (str): имя файла.

        1. Очистить списки клиентов и ошибок.
           Сохранить имя файла в 'self.filename'.
        2. Построчно прочитать файл "filename".
        3. Для каждой строки:
           - создать Customer.from_string() из строки;
           - добавить в 'self.customers';
           - при возникновении ошибки занести строку в 'self.errors' и
             перейти к следующей.
        4. Проверить, что прочитан хотя бы 1 клиент (assert).
        5. Отсортировать список 'self.customers' по Ф, И, О (по возрастанию).
        """
        self.customers, self.errors = [], []
        self.filename = filename
        with open(filename, encoding='utf-8') as fh:
            lines = fh.readlines()
        for line in lines:
            try:
                self.customers.append(Customer.from_string(line))
            except Exception as err:
                print(err)
                self.errors.append(line)
        assert self.customers, 'Отсутствуют валидные строки.'
        self.customers.sort(key=lambda a: a.o)
        self.customers.sort(key=lambda a: a.i)
        self.customers.sort(key=lambda a: a.f)

    def total_price(self):
        """Вернуть общую сумму контрактов."""
        return sum(customer.polis_price for customer in self.customers)

    def price_stats(self):
        """Вернуть статистические показатели (среднее, мода и медиана)
        по сумме продаж (кортеж).

        Если мода не может быть вычислена (StatisticsError) -
        вернуть вместо нее строку "не доступно".
        """
        prices = [customer.polis_price for customer in self.customers]
        try:
            mode = (statistics.mode(prices))
        except Exception:
            mode = 'не доступно'
        prices = [customer.polis_price for customer in self.customers]
        return (statistics.mean(prices), mode,
                statistics.median(prices))

    def age_stats(self):
        """Вернуть статистические показатели (среднее и медиана)
        по возврасту клиентов (кортеж).

        Возраст - полное количество лет.
        """
        bdays = [customer.birthday for customer in self.customers]
        ages = [(datetime.date.today() - bday).total_seconds() //
                (60 * 60 * 24 * 365.2425) for bday in bdays]
        return (statistics.mean(ages),
                statistics.median(ages))

    def most_popular_polis_type(self):
        """Вернуть наиболее популярный тип полиса
        (по количеству контрактов).

        Результат: кортеж (Тип полиса, Количество контрактов),
                   например, ("Здоровье", 7).

        Подсказка: удобным способом может быть использование функции
                   sorted() с настраиваемым параметром key.
        """
# что имеется ввиду под удобным способом?
        res = {}
        for i in self.customers:
            if res.get(i.polis_type, False):
                res[i.polis_type] += 1
            else:
                res[i.polis_type] = 1
        return (sorted(res.items(), key=lambda x: x[1]))[-1]

    def most_profitable_polis_type(self):
        """Вернуть наиболее прибыльный тип полиса
        (по количеству контрактов).

        Результат: кортеж (Тип полиса, Сумма всех полисов данного типа),
                   например, ("Здоровье", 105000).

        Подсказка: удобным способом может быть использование функции
                   sorted() с настраиваемым параметром key.
        """
        res = {}
        for i in self.customers:
            if res.get(i.polis_type, False):
                res[i.polis_type] += i.polis_price
            else:
                res[i.polis_type] = i.polis_price
        return (sorted(res.items(), key=lambda x: x[1]))[-1]

    def print_report(self):
        """Напечатать отчет.

        Выводит на экран сводку по запрошенным показателям.

        Формат:

        "
Сумма контрактов = 305,000 руб.

Статистика продаж:
  - Цена: 30,500 руб. (среднее), 15,000 руб. (мода), 15,000.0 руб. (медиана)
  - Возраст: 51.6 л. (среднее), 53.5 л. (медиана)
  - Самый популярный тип страхового полиса: Здоровье (7)
  - Самый прибыльный тип страхового полиса: Здоровье (105,000 руб.)
        "

        Сформируйте строку 'report', которую в конце выведите на экран.
        """
        summ = sum(x.polis_price for x in self.customers)

        report = 'Сумма контрактов = {:,} руб.\n\n'\
            'Статистика продаж:\n'\
            '  - Цена: {:,} руб. (среднее), {:,} руб. (мода), {:,} руб.'\
            ' (медиана)\n'\
            '  - Возраст: {:.1f} л. (среднее), {:.1f} л. (медиана)\n'\
            '  - Самый популярный тип страхового полиса: {} ({})\n'\
            '  - Самый прибыльный тип страхового полиса: {} ({:,} руб.)'\
            ''.format(summ, *self.price_stats(), *self.age_stats(),
                      *self.most_popular_polis_type(),
                      *self.most_profitable_polis_type())

        print(report)

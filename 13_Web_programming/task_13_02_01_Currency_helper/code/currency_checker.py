import os.path
import re
import datetime
import time
import smtplib
from email.mime.text import MIMEText
import requests


NO_DATA = "Нет данных"


EMAIL = "***"
PASSWORD = "***"

class CurrencyChecker:
    """Класс CurrencyChecker реализует валютный помощник.

    Поля:
        Данные ИТ-аккаунта (прописаны в коде)
        - self.it_email: e-mail ИТ-отдела;
        - self.it_email_password: пароль от e-mail ИТ-отдела;
        - self.it_email_smtp_server: SMTP-сервер для e-mail ИТ-отдела;
        - self.it_email_smtp_port: SMTP-порт для e-mail сервера ИТ-отдела;
        Данные руководителя
        - self.ceo_name: ФИО руководителя;
        - self.ceo_email: e-mail руководителя.
        Прочее
        - self.log_filename: имя файла для логгирования;
        - self.msg: письмо для отправки (email.mime.text).

    Методы:
      - self._log(): вывод события на экран и в лог-файл;
      - self.run(): бесконечный цикл работы - получение данных и их отправка;
      - self.get_info(): получение котировок с сайта;
      - self._create_message(): формирование текста сообщения для отправки.
    """

    def __init__(self, ceo_name, ceo_email):
        """Конструктор класса."""
        # Данные руководителя
        self.ceo_name = ceo_name
        self.ceo_email = ceo_email

        # Данные ИТ-аккаунта
        self.it_email = EMAIL
        self.it_email_password = PASSWORD
        self.it_email_smtp_server = 'smtp.gmail.com'
        self.it_email_smtp_port = 587

        # Лог-файл
        # Имя лог-файла задано в коде - "log.txt" в папке приложения
        self.log_filename = os.path.realpath('log.txt')
        self.msg = MIMEText

    def __str__(self):
        """Вернуть информацию о классе."""
        return "CurrencyChecker v 0.1"

    def _log(self, message):
        """Вывести на экран 'message' с указанием текущего времени
        формате 0001-01-01 00:00:00 (год, месяц, число, часы, минуты, секунды):
          - на экран;
          - в лог-файл (дописать в конец файла).
        """
        form = '%Y-%m-%d %X'
        currenttime = datetime.datetime.today()
        message = '\n' + currenttime.strftime(form) + ' | ' + message
        print(message)
        with open(self.log_filename, mode='a') as f:
            f.write('\n' + message)

    def run(self, timeout, currencies):
        """Каждые 'timeout секунд':
        - запросить информацию о курсах;
        - отправить их на почту.
        """
        while True:
            try:
                info = self.get_info(currencies)
                self._log("Данные получены: " + str(sorted(info.items())))
                text = self._create_message(info)
                self.send_mail(text)
                self._log("Письмо успешно отправлено!")
            except Exception as err:
                self._log("Произошла ошибка: " + str(err))
            finally:
                time.sleep(timeout)

    @staticmethod
    def get_info(currencies):
        """Вернуть курсы валют.

        Источник: http://www.finanz.ru/valyuty/v-realnom-vremeni-rub.

        Параметры:
            - currencies: список валют, например: ['USD', 'EUR'].

        Результат:
            - словарь вида {
                              'USD': (20.0, "10:23:00"),
                              'EUR': (30.0, "10:23:00")
                            }
                , где значение (кортеж) содержит:
                  - значение покупки (3-й столбец) (float);
                  - дату получения значения с биржи (последний столбец) (str).

              Если валюта из 'currencies' или какое-либо значение не найдено,
              валюта добавляется в словарь со значением "Не известно".
        """

        def _value_to_float(value):
            """Вернуть 'value' как вещественное число (если возможно)
            или вернуть 'NO_DATA'."""
            try:
                return float(value.replace(',', '.'))
            except ValueError:
                return NO_DATA

        res = {}
        # 1. По умолчанию о каждой валюте ничего не известно
        link = 'http://www.finanz.ru/valyuty/v-realnom-vremeni-rub'
        text = requests.get(link).text
        n = text.find('КУРСЫ ВАЛЮТ И КОТИРОВКИ ВАЛЮТ В РЕАЛЬНОМ ВРЕМЕНИ')
        # это действие для спасения от ошибки неизвестного символа
        text = text[n:]
        for cur in currencies:
            start = text.find('{}/RUB'.format(cur))
            try:
                cost = _value_to_float(re.search(
                        r'data-template="Bid".+data-animation="">(\d+,\d+)'
                        '<\/span> <\/div><\/td>', text[start:start + 1200],
                        re.DOTALL).groups()[0])
                if not isinstance(cost, float):
                    raise AttributeError
                res[cur] = (cost,
                            re.search(r'data-field="BidTimestamp".+data-'
                                      'animation="animationType:none" >'
                                      '(\d+:\d+:\d+)'
                                      '<\/span><\/div><\/td>',
                                      text[start:start + 3000],
                                      re.DOTALL).groups()[0])
            except AttributeError:
                res[cur] = 'Не известно'

        # 2. Поиск информации о валютах
        # . не захватывает переносы строки по умолчанию, поэтому при создании
        # regex-объекта необходимо указать флаг re.DOTALL
        return res

    def _create_message(self, info):
        """Составить и вернуть текст письма.

        Валюты выводятся в алфавитном порядке.

        Параметры:
          - info: словарь из self.get_info().

        Результат:
          - текст письма (str) вида:

            Иван Иванович!

            Обновленные курсы валют:
              - EUR: 60.65 (12:00:05)
              - USD: 50.12 (12:00:05)

            С уважением, ИТ-отдел.
        """

        info_str = ''
        for i in sorted(info.keys()):
            if isinstance(info[i], str):
                info_str += '{0}:  {1}\n'.format(i, info[i])
            else:
                info_str += '{0}: {1[0]:>6.2f} ({1[1]})\n'.format(i, info[i])

        res = """\
{ceo_name}!

Обновленные курсы валют:

{info_str}
С уважением, ИТ-отдел.\
""".format(ceo_name=self.ceo_name, info_str=info_str)

        return res

    def send_mail(self, text):
        """Отправить текст 'text' на почтовый адрес
        'self.ceo_email' для 'self.ceo_name'.
        """

        # 1. Формирование сообщения (MIMEText)
        self.msg = MIMEText(text)
        self.msg["From"] = self.it_email
        self.msg["To"] = self.ceo_email
        self.msg["Subject"] = 'Курс Валют'
        try:
            server = smtplib.SMTP(
                self.it_email_smtp_server,
                self.it_email_smtp_port)
            server.starttls()
            server.login(self.it_email, self.it_email_password)

            server.send_message(self.msg)
        except smtplib.SMTPException as err:
            print("Ошибка при отправке письма:", err)
        finally:
            server.quit()

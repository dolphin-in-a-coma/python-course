import sys
import re
import imaplib
import smtplib
import email
import os.path
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import decode_header

import utils

LOGIN = "****"
PASSWORD = "******"

class Mailer:
    """Класс Mailer отвечает за чтение и отправку почты.

    Поля:
      - self.login (str): логин (email) почтового сервиса;
      - self.password (str): пароль для почтового сервиса;
      - self.imap_server (imaplib.IMAP4_SSL): объект - IMAP-сервер;
      - self.imap_server_url (str): адрес IMAP-сервера;
      - self.imap_port (int): порт IMAP-сервера;
      - self.smtp_server (smtplib.SMTP): объект - SMTP-сервер;
      - self.smtp_server_url (str): адрес SMTP-сервера;
      - self.smtp_port (int): порт SMTP-сервера;
      - self.msg (email.Message): электронное письмо.

    Методы:
      - см. описание методов.
    """

    def __init__(self):
        """Инициализация класса.

        - задать значения:
            - self.login,
            - self.password,
            - self.imap_server_url,
            - self.imap_port,
            - self.smtp_server_url,
            - self.smtp_port,
            - self.msg (None);
        - создать self.imap_server, self.smtp_server и выполнить подключение.
        """
        self.login = LOGIN
        self.password = PASSWORD
        self.imap_server_url = 'imap.gmail.com'
        self.imap_port = '993'
        self.smtp_server_url = 'smtp.gmail.com'
        self.smtp_port = 587

        """Выполнить подключение к IMAP- и SMTP серверам."""
        self.imap_server = imaplib.IMAP4_SSL(self.imap_server_url, self.imap_port)
        self.imap_server.login(self.login, self.password)
        
        self.smtp_server = smtplib.SMTP(self.smtp_server_url, self.smtp_port)
        self.smtp_server.starttls()
        self.smtp_server.login(self.login, self.password)
        
        # Сообщение
        self.msg = None

    def __str__(self):
        """Вернуть информацию о классе."""
        return "Mailer v 0.1"

    def noop(self):
        """Выполнить noop для IMAP- и SMTP-серверов."""
        self.imap_server.noop()
        self.smtp_server.noop()

    def disconnect(self):
        """Отключиться от IMAP- и SMTP-серверов."""
        self.imap_server.logout()
        self.smtp_server.quit()

    @staticmethod
    def _get_request_info(message):
        """Вернуть информацию о запросе клиента.

        Параметры:
          - message (email.Message): письмо.

        Письмо должно соответствовать определенному шаблону:

        * тема: **Просьба прислать актуальные вакансии**;
        * в тексте письма:

           * **Поиск: {}.**
           * **Регион: {}.**
           * **Опыт работы (лет): {}.**
           * **З/п (руб.): {}.**

        Данные о строке поиска и регионе являются обязательными.

        Результат:
          - словарь с ключами (значение = None, если не найдено):
            - "email" (str): e-mail клиента,
            - "datetime" (str): дата сообщения;
            - "subject" (str): тема сообщения;
            - "text" (str): текст сообщения;
            - "title" (str): строка поиска;
            - "area" (str): регион поиска;
            - "experience" (int): опыт работы;
            - "salary" (int): уровень зарплаты;
          - или None, если обязательные данные не найдены.
        """
        
        subject = r'Просьба прислать актуальные вакансии'
        title = r'Поиск ([\w -]+)\.'
        # не забыть двоеточие
        area = r'Регион: ([\w -]+)\.'
        experience = r'Опыт работы \(лет\): (\d+)\.'
        salary = r'З\/п \(руб.\): (\d+)\.'
        email = r'([\w_\.-]+@\w+\.\w+)'
        # 1. Информация о письме
        text, encoding, mime = get_message_info(message)

        info = {}

        # 2. Поиск необходимой информации
        # Проверка темы
        subject_in_text = re.search(subject, do_decode_header(message['Subject']))


        # Проверка строки поиска и региона
        area_in_text = re.search(area, text)
        title_in_text = re.search(title, text)
        
        if not(subject_in_text and area_in_text and title_in_text):
            return None

        # Проверка опыта и уровня з/п
        experience_in_text = re.search(experience, text)
        salary_in_text = re.search(salary, text)
        
        info = {'text' : text,
                'subject' : subject_in_text.string,
                'email' : re.search(email, do_decode_header(message['From'])).group(1),
                'datetime' : message['Date'],
                'area' : area_in_text.group(1),
                'title' : title_in_text.group(1)
                }
                
        if experience_in_text:
            info['experience'] = int(experience_in_text.group(1))
        if salary_in_text:
            info['salary'] = float(salary_in_text.group(1))

        return info

    def check_requests(self):
        """Получить список новых запросов от клиентов."""
        requests = []
        try:
            self.imap_server.select()

            response, messages_nums = self.imap_server.search(None, "(UNSEEN)")
            if response != "OK":
                raise imaplib.IMAP4.error("Не удалось получить список писем.")

            messages_nums = messages_nums[0].split()
            utils.log("Найдено новых писем: {}".format(len(messages_nums)))

            # 2.3. Чтение новых сообщений
            # не все письма читаются 
            for message_num in reversed(messages_nums[-20:]):
                # message_parts = "(RFC822)" - получение письма целиком
                response, data = \
                    self.imap_server.fetch(message_num,
                                           message_parts="(RFC822)")
                if response != "OK":
                    utils.log("Не удалось получить письмо №",
                              int(message_num.decode()))
                    continue

                # Отметить "прочитанность" обратно
                # Она будет отмечена при успешной отпраке письма
                self.imap_server.store(message_num, '-FLAGS', '\Seen')

                # Преобразование сообщения в объект email.Message
                message = email.message_from_bytes(data[0][1])
                info = self._get_request_info(message)
                if info:
                    # print(info)
                    info['id']=message_num
                    requests.append(info)

                

                # Получение информации из письма, используя
                # Mailer._get_request_info()
                # Если возвращается не None, необходимо:
                #  - добавить ключ "id" с номером message_num;
                #  - добавить 'info' в 'requests'.

            return requests
        except imaplib.IMAP4.error as err:
            utils.log("Возникла следующая ошибка:", err)
            raise

    def send_mail(self, info, filename):
        """Отправить файл `filename` на почтовый адрес 'email' из 'info' c
        сопровождающим текстом.

        Параметры:
          - info (словарь _get_request_info()): запрос клиента;
          - filename(str): имя файла.
        """

        # 1. Формирование сообщения
        #    Заголовки "Subject", "From", "To"
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'Подходящие вакансии'
        self.msg['From'] = self.login
        self.msg['To'] = info['email']

        # 1.1. MIMEText и MIMEApplication
        #      Прикрепить 'text' к 'self.msg' как 'text/plain'
        text = "Здравствуйте!\n\n"          \
               "Ответ на Ваш запрос содержится во вложении\n\n"         \
               "С уважением, агентство \"{}\"".format(utils.agency_name)
        self.msg.attach(MIMEText(text, 'plain'))

        # 1.2. MIMEApplication
        #      Прикрепить 'filename' к 'self.msg'
        #filename = os.path.join(os.path.dirname(sys.argv[0]),filename)
        with open(filename, mode = 'rb') as fl:
            pdf_part = MIMEApplication(fl.read(), _subtype = 'pdf')
        pdf_part.add_header('Content-Disposition','attachment',filename=os.path.basename(filename))
        self.msg.attach(pdf_part)

        # 2. Подклюение к серверу и отправка письма
        try:
            # Отправить письмо 'self.msg'
            self.smtp_server.send_message(self.msg)

            # Отметить письмо как прочитанное, чтобы не проверять его повторно
            self.imap_server.select()
            self.imap_server.store(info['id'], 'FLAGS', '\Seen')
        except smtplib.SMTPException as err:
            utils.log("Возникла следующая ошибка:", err)
            raise


def do_decode_header(header):
    """Декодировать заголовок по ключу 'header'.

    Параметры:
      header (str): заголовок вида
                    "=?UTF-8?B?UmU6INCT0LvQtdCxINCf0L7Rh9GC0LA=?=".

    Базовые стандарты RFC 822 и RFC 2822 предусматривают, что
    любой заголовок представляет собой набор ASCII-символов, и до сих пор
    все символы обязательно преобразуются из/в этот формат.

    Python позволяет декодировать заголовки с использованием
    функции decode_header модуля email.header.
    """
    header_parts = decode_header(header)
    # 'decode_header' возвращает список кортежей вида
    # [(b'\xd0\x9f\xd0\xb0\xd0\xb2\xd0\xb5\xd0\xbb
    #     \xd0\x9f\xd0\xb0\xd0\xbd\xd1\x84\xd0\xb8\xd0\xbb
    #     \xd0\xbe\xd0\xb2', 'utf-8'),
    #  (b' <***@gmail.com>', None)]
    # Которые необходимо преобразовать в правильную кодировку

    res = []
    for decoded_string, encoding in header_parts:
        if encoding:
            decoded_string = decoded_string.decode(encoding)
        elif isinstance(decoded_string, bytes):
            decoded_string = decoded_string.decode("ascii")
        res.append(decoded_string)

    # На выходе 'res' содержит заголовок в "привычном", декодированном виде
    return "".join(res)


def get_part_info(part):
    """Получить текст сообщения в правильной кодировке.

    Параметры:
      - part: часть сообщения email.Message.

    Результат:
      - message (str): сообщение;
      - encoding (str): кодировка сообщения;
      - mime (str): MIME-тип.
    """
    encoding = part.get_content_charset()
    # Если кодировку определить не удалось, используется по умолчанию
    if not encoding:
        encoding = sys.stdout.encoding
    mime = part.get_content_type()
    message = part.get_payload(decode=True).decode(encoding,
                                                   errors="ignore").strip()

    return message, encoding, mime


def get_message_info(message):
    """Получить текст сообщения в правильной кодировке.

    Параметры:
      - message: сообщение email.Message.

    Результат:
      - message (str): сообщение или строка "Нет тела сообщения";
      - encoding (str): кодировка сообщения или "-";
      - mime (str): MIME-тип или "-".

    """
    # Алгоритм получения текста письма:
    # - если письмо состоит из нескольких частей
    #   (message.is_multipart()) - необходимо пройти по составным
    #   частям письма: "text/plain" или "text/html"
    # - если нет - текст можно получить напрямую

    message_text, encoding, mime = "Нет тела сообщения", "-", "-"

    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() in ("text/html", "text/plain"):
                message_text, encoding, mime = get_part_info(part)
                break  # Только первое вхождение
    else:
        message_text, encoding, mime = get_part_info(message)

    return message_text, encoding, mime


# ml = Mailer()
'''ml.imap_server.select()
message_nums=ml.imap_server.search(None,'ALL')[-1][0]
x=ml.imap_server.fetch(message_nums.split()[-1],'(RFC822)')
x = email.message_from_bytes(x[-1][0][1])
print(x)
print(ml._get_request_info(x))'''
# print(ml.check_requests())

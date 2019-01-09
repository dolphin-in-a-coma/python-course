import time

from mailer import Mailer
from hh import Hh
from reporter import Reporter
import utils


class JobMonitor:
    """Класс JobMonitor реализует помощник кадрового менеджера.

    Поля:
      - self.mailer (mailer.Mailer);
      - self.hh (hh.Hh);
      - self.reporter (reporter.Reporter).

    Методы:
      - см. описание методов.
    """

    def __init__(self):
        """Инициализация класса.

        Создать атрибуты self.mailer, self.hh, self.reporter.
        """
        self.mailer = Mailer()
        self.hh = Hh()
        self.reporter = Reporter()
        #существуют ли экземпляры класса для верхних классов?

    def __str__(self):
        """Вернуть информацию о классе."""
        return "JobMonitor v 0.1"

    def run(self, timeout):
        """Проверять и отвечать на заявки каждые 'timeout' секунд."""
        sec_old = None
        while True:
            # Если 'sec_old' не установлен или не прошло нужное время,
            # поддерживаем соединение
            sec_new = time.perf_counter()
            if sec_old is None or sec_new - sec_old > timeout:
                utils.log("Проверяю...")

                # 1. Проверка почты и запросов клиентов
                requests = self.mailer.check_requests()
                utils.log("Найдено новых запросов: {}".format(len(requests)))

                # 2. Обработка запросов
                for i, request in enumerate(requests, start=1):
                    utils.log("Обработка запроса №{}: {}".format(i, request))

                    # 2.1. Поиск вакансий
                    print(request['title'],
                    request['area'], request.get('salary', None),
                    request.get('experience', None), sep = '\n')
                    
                    vacancies = self.hh.search(request['title'],
                    'Москва' , request.get('salary', None),
                    request.get('experience', None))
                    utils.log("Найдено вакансий: {}".format(len(vacancies)))
                    for vacancy in vacancies:
                        utils.log(vacancy)

                    # 2.2. Формирование отчета
                    filename = self.reporter.make(request, vacancies)
                    utils.log("Документ \"{}\" сформирован".format(filename))

                    # 2.3. Отправка ответа
                    self.mailer.send_mail(request, filename)
                    utils.log("Письмо отправлено!")

                sec_old = sec_new
            else:
                utils.log("Ожидаю.")
                # "Заморозка" потока на 5 с.
                time.sleep(5)
                self.mailer.noop()

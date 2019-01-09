import requests
import exceptions
import json


class Hh:
    """Класс Parser реализует парсер вакансий с сайта hh.ru."""

    @staticmethod
    def _get_area_id(area):
        """Получить ID региона по его имени.

        Параметры:
          - area (str): регион (например, Москва);

        Результат:
          - ID региона;
          или
          - None, если пришла ошибка в ответе на запрос или регион не найден.

        Переданные параметры необходимо преобразовать в параметры запроса:
          - API-метод:
            https://api.hh.ru/areas;
          - документация:
            https://github.com/hhru/api/blob/master/docs/areas.md.
        """

        def get_area(areas, name):
            """Вернуть ID города 'name' из структуры 'areas'."""
            for item in areas:
                if "name" in item and item["name"] == name:
                    return int(item["id"])
                if "areas" in item and item["areas"]:
                    res = get_area(item["areas"], name)
                    if res:
                        return res

        area = area[0].upper() + area[1:]
        # поднимает лишние буквы, добавить в Mailer проверку на верхние буквы (fixed)
        areas_json = requests.get('https://api.hh.ru/areas').json()
        res = get_area(areas_json, area)
        return res

    @staticmethod
    def _get_experience_id(experience):
        """Получить тип опыта (строку) в зависимости от 'experience' лет.

        На hh.ru опыт делится на 4 категории:
         - "noExperience": нет опыта;
         - "between1And3": от 1 до 3 лет (не включительно);
         - "between3And6": от 3 до 6 лет (не включительно);
         - "moreThan6": больше 6 лет.

        Результат:
          - одна из категорий выше в зависимости от 'experience' лет;
          или
          - ValueError, если 'experience' не является
            целым положительным числом.
        """
        if not (isinstance(experience, int) and experience >=0): 
            raise ValueError('Опыт(experience) должен быть целым'
            ' неотрицательным числом')
        if experience == 0:
            return 'noExperience'
        elif experience < 3:
            return 'between1And3'
        elif experience <6:
            return 'between3And6'
        else:
            return 'moreThan6'
    @staticmethod
    def search(title, area, salary=None, experience=None):
        """Выполнить поиск и вернуть список вакансий.

        Параметры:
          - title (str): наименование вакансии;
          - area (str): регион;
          - salary (int или float): уровень зарплаты;
          - experience (int): количество лет опыта.

        Переданные параметры необходимо преобразовать в параметры запроса:
          - основной API-метод:
            https://api.hh.ru/vacancies;
          - документация:
            https://github.com/hhru/api/blob/master/docs/vacancies.md.

        Поиск включает ряд шагов:
        1. Найти вакансии и получить ID вакансий.
        2. Для каждой найденной ссылки получить информацию по ID.

        Результат:
          - список словарей вакансий.
        """

        url = 'https://api.hh.ru/vacancies/'
        # Только первые 10 результатов
        params = dict(text=title, search_field="name", per_page=10)
        params['area'] = Hh._get_area_id(area)
        if salary:
            params['salary'] = int(salary)
        if experience:
            params['experience'] = Hh._get_experience_id(experience)
        secret = requests.get(url, params = params)
        # print(secret.text)
        vacancies_json = secret.json()
        res = []
        # print(vacancies_json)
        for item in vacancies_json['items']:
            vac = requests.get(url + item['id']).json()
            # возможно это неправильно, что я делаю список json, а не структур питона
            # print(vac)
            res.append(vac)
            

        # Запрос для каждого элемента из vacancies["items"] по 'id'



        return res

'''hhh = Hh()
print(json.dumps(hhh.search('визажист', 'москва', 50000, 5)))'''

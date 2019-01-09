import os.path
import requests
import urllib


class VkError(Exception):
    """Класс-исключение, возбуждаемый в классе Vk."""
    pass


class Vk:
    """Класс для работы с ВК API.

    Поля:
        - self.access_token (str): токен;
        - self.api_url (str): адрес для вызова API.
    """

    def __init__(self, access_token):
        """Инициализация класса.

        Действия:
          - инициализировать 'self.access_token';
          - инициализировать 'self.api_url'.
        """
        self.access_token = access_token
        self.api_url = 'https://api.vk.com/method/'

    def __str__(self):
        """Вернуть информацию о классе."""
        return "Vk v 0.1"

    def _call_method(self, method, **params):
        """Вернуть результаты выполнения метода 'method'
        с параметрами 'params' для ВК API формате json.

        Параметры:
          - method (str): наименование API-функции;
          - params (dict): параметры вызова API-функции;
                           не включают "access_token", который должен
                           быть добавлен к каждому вызову функции.

        Результат:
          - ответ в формате json или исключение;
            для возврата необходимо использовать метод 'self._json()'.
        """
        # Токен добавляется при каждом вызове метода
        r = requests.get(self.api_url + method, params = dict(params, access_token = self.access_token))

        return self._json(r)

    def _json(self, r):
        """Вернуть HTTP-ответ 'r' в формате json.

        Если запрос был выполнен с ошибкой, возбудить исключение VkError.
        """
        r.raise_for_status()
        # кажется это подъем ошибки

        res = r.json()
        if "error" in res and "error_msg" in res["error"]:
            raise VkError("Ошибка выполнения запроса:\n\n"
                          "1. url: {}\n\n2. Ошибка: {}".
                          format(urllib.parse.unquote(r.url),
                                 res["error"]["error_msg"]))

        return res

    def _upload_image(self, owner_id, image_filename):
        """Загрузить изображения из файла 'image_filename' на сервер.

        Для загрузки изображения необходимо вызвать 2 функции
        (https://vk.com/dev/upload_files?f=2. Загрузка фотографий на стену):
          - photos.getWallUploadServer: возвращает адрес сервера для
                                        загрузки фотографии на стену
                                        пользователя или сообщества;
          - photos.saveWallPhoto: сохраняет фотографии после успешной
                                  загрузки на URI, полученный методом
                                  photos.getWallUploadServer.
        """
        # 1. Поиск адреса для загрузки фотографии на стену
        #
        #    Необходимо вызвать API-функцию 'photos.getWallUploadServer'
        #    и получить res["response"]["upload_url"]
        params = {}
        if owner_id <= 0:
            params = {'group_id' : (-1)*owner_id}
        upload_url = self._call_method('photos.getWallUploadServer', **params)["response"]["upload_url"]

        # 2. Загрузка фотографии на полученный адрес, используя POST-запрос,
        #    и получение адреса загруженного изображения
        #
        #    Необходимо получить параметры:
        #    res["server"], res["hash"], res["photo"]
        files = {"photo": open(image_filename, "rb")}
        r = requests.post(upload_url, files=files)
        res = self._json(r)

        # 3. Сохранение загруженного изображение
        #
        #    Необходимо вызвать API-функцию 'photos.saveWallPhoto',
        #    передав параметры 'server', 'hash' и 'photo'
        #    и получить res["response"][0]["id"]
        params = dict(params, server = res['server'], hash = res['hash'], photo = res['photo'])
        print(params)

        res = self._call_method('photos.saveWallPhoto', **params)
        
        image_id = res['response'][0]['id']

        return image_id

    def wall_post(self, owner_id, message,
                  location=None, image_filename=None, link=None):
        """Оставить пост на стене пользователя 'owner_id'.

        Параметры (обязательные):
          - owner_id (int): id пользователя/группы;
          - message (str): сообщение.

        Параметры (необязательные):
          - location (dict): {"lat": ..., "long": ...} (ширина и долгота);
          - image_filename (str): имя файла с рисунком;
          - link (str): произвольная ссылка.

        Результаты (14):
          - post_id (int): операция прошла успешно;
          - VkError в противном случае.

        Для публикации сообщения на стене пользователя или сообщества
        используется функция 'wall.post'.
        """
        # 1. Формирование параметров API-функции
        params = dict(owner_id=owner_id, message=message, attachments="")

        # Для тестов на своей стене используйте параметр "publish_date",
        # который позволяет сделать отложенную публикацию
        
        # params["publish_date"] =  \
        # int((datetime.datetime.now() +
        # datetime.timedelta(days=1)).timestamp())

        # 1.1. Вложения (если не равны None - image_filename, link)
        attachments = []

        if image_filename:
            attachments.append(self._upload_image(owner_id,image_filename))
        if link:
            attachments.append(link)

        params["attachments"] = ",".join(attachments)

        # 1.2. Местоположение (если не равно None - location)
        if location:
            params['lat'] = location['lat']
            params['long'] = location['long']
        
        
        # 2. Вызов функции
        post_id = self._call_method('wall.post', **params)["response"]["post_id"]

        return post_id

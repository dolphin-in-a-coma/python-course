import requests
import matplotlib.pyplot as plt
import time


class VK:
    """
    получает информацию о друзьях во ВКонтакте и
    создает столбчатую диаграмму по количеству друзей по полу
    """

    FIELDS = ("user_id", "first_name", "last_name", "sex")
    SEX = {1: 'Ж', 2: 'М', 0: 'М/Ж'}

    def __init__(self, user_id, token):
        """
            self._user_id - id пользователя
            self._token - токен
            self._data - информация о друзьях ВК
        """
        assert isinstance(user_id, int), \
            "id пользователя должен быть типа 'int'"
        assert isinstance(token, str), \
            "Токен должен быть типа 'str'"
        self._user_id = user_id
        self._token = token
        self._data = []
        self._get_data()

    def __str__(self):
        """
            возвращает строковое представление информации о друзьях
        """
        string = "Список друзей({}):".format(len(self._data))
        string += "\n{0:11}{1:15}{2:15}{3:3}".format(VK.FIELDS[0],
                                                     VK.FIELDS[1],
                                                     VK.FIELDS[2],
                                                     VK.FIELDS[3])
        for i in self._data:
            string += "\n{0:11}{1:15}{2:15}{3:15}". \
                format(str(i[VK.FIELDS[0]]), i[VK.FIELDS[1]],
                       i[VK.FIELDS[2]], self.SEX[i[VK.FIELDS[3]]])
        fio, value = self.most_common_friends()
        string += "\nДруг, с которым больше всего общих знакомых:"
        string += "\n Ф.И.О. - {}\n Кол-во общих друзей - {}".format(fio,
                                                                     value)
        fio, value = self.most_popular_friend()
        string += "\nСамый популярный друг:"
        string += "\n Ф.И.О. - {}\n Кол-во друзей - {}".format(fio, value)
        return string

    def _get_data(self):
        """
        получает данные о друзьях
        """
        data = []
        method_url = 'https://api.vk.com/method/friends.get?'
        dct = dict(access_token=self._token, user_id=self._user_id,
                   fields='sex')
        r = requests.post(method_url, dct)
        result = r.json()
        assert not result.get("error", None), "Произошла ошибка при" \
                                              " выполнении friends.get! " \
                                              "Код ошибки" \
                                              " - {}".format(
            result["error"]["error_code"])
        data = result['response']
        for i in data:
            dct = {}
            for field in i:
                if field in VK.FIELDS:
                    dct[field] = i[field]
            time.sleep(0.1)
            self._data.append(dct)

    def most_common_friends(self):
        """
            возвращает друга с наибольшим количеством общих друзей
        """
        method_url = "https://api.vk.com/method/friends.getMutual?"
        data = []
        for i in self._data:
            try:
                dct = dict(access_token=self._token, target_uid=i["user_id"])
                r = requests.post(method_url, dct)
                result = r.json()
                assert not result.get("error", None), "Произошла ошибка при" \
                                                      " выполнении friends." \
                                                      "getMutual! Код ошибки" \
                                                      " - {}".format(
                    result["error"]["error_code"])
                time.sleep(0.3)
                fio = ' '.join([i['first_name'], i['last_name']])
                data.append((fio, len(result["response"])))
            except AssertionError as err:
                print(err)
        data.sort(key=lambda x: x[1])
        return data[-1]

    def most_popular_friend(self):
        """
            возвращает самого популярного друга
        """
        data = []
        for i in self._data:
            try:
                method_url = 'https://api.vk.com/method/friends.get?'
                dct = dict(access_token=self._token, user_id=i['user_id'])
                r = requests.post(method_url, dct)
                result = r.json()
                assert not result.get("error", None), "Произошла ошибка при" \
                                                      " выполнении " \
                                                      "friends.get! " \
                                                      "Код ошибки" \
                                                      " - {}".format(
                    result["error"]["error_code"])
                time.sleep(0.3)
                fio = ' '.join([i['first_name'], i['last_name']])
                data.append((fio, len(result['response'])))
            except AssertionError as err:
                print(err)
        data.sort(key=lambda x: x[1])
        return data[-1]

    def _make_plot(self):
        """
            генерирует изображение
        """
        assert len(self._data) > 0, "Нет данных для вывода!"

        fig, ax = plt.subplots()
        fig.canvas.set_window_title("Распределение друзей из ВК по полу.")
        ax.set_title("Распределение друзей из ВК по полу.")
        ax.set_xlabel("Количество(чел.)")
        lst = [i["sex"] for i in self._data]
        sexes = {i: lst.count(i) for i in lst}

        tick_label = [self.SEX[i] for i in list(sexes.keys())]
        size = list(sexes.values())
        nums = [x + 1 for x in range(len(size))]
        ax.barh(nums, size, tick_label=tick_label)
        return fig

    def show_plot(self):
        """
            отображет сгенерированное изображение
        """
        self._make_plot()
        plt.show()

import csv
import matplotlib.pyplot as plt


class ElectionAnalyzer:
    """Класс ElectionAnalyzer выполняет:
      - формирование итогового списка партий с подсчетом голосов;
      - построение круговой диаграммы суммарного количества голосов.

    Поля:
      - self._data: двумерный массив данных вида:
             [[1, 'Партия 5', 1, 1, 2, 0.06666666666666667],
              [2, 'Партия 4', 2, 2, 4, 0.13333333333333333],
              [3, 'Партия 3', 3, 3, 6, 0.2]]

    Методы:
      - self.load(): загрузка, определение показателей и сортировка данных;
      - self._make_plot(): формирование изображения;
      - self.show_plot(): отображение изображения.
    """

    def __init__(self):
        """Инициализация класса.

        Действия:
          - инициализировать 'self._data'.
        """
        self._data = []

    def __str__(self):
        """Вернуть строку - анализируемые данные.

        Формат:

        Результаты (14):
        1. ЕДИНАЯ РОССИЯ 55.23%
        ...
        14. Гражданская Сила 0.14%
        """
        res = 'Результаты ({}):'.format(len(self._data)-1)
        for i in self._data:
            if isinstance(i[0], int):
                res += '\n{}. {} {:.2f}%'.format(len(self._data)-i[0],
                                                 i[1], i[-1] * 100)

        return res

    def load(self, filename):
        """Загрузить файл 'filename' с результатами выборов.

        Параметры:
          - filename (str): имя файла.

        По результатам загрузки 'self._data' должен содержать
        двумерный набор данных и файла, включая заголовки.
        Числовые значения должны быть преобразованы в числа.

        Функция не обрабатывает возникающие исключения.
        """
        with open(filename, encoding='utf-8') as fh:
            lines = list(csv.reader(fh))
            nose = lines[0]
            tail = lines[1:]
        lst = [[int(i) if i.isdigit() else i for i in line] for line in tail]

        all_sum = 0
        for i in range(len(lst)):
            summ = sum(lst[i][2:])
            all_sum += summ
            lst[i].append(summ)
        for i in range(len(lst)):
            lst[i].append(lst[i][-1]/all_sum)

        lst.sort(key=lambda x: x[-1], reverse=True)
        for i in range(len(lst)):
            lst[i][0] = len(lst) - i
        self._data = [nose] + lst

    def _make_plot(self):
        """Генерирует изображение, не отображая его.

        Изображение должно включать несколько диаграмм по горизонтали,
        количество которых равно длине 'self._data'.

        Если 'self._data' не содержит данных, возбудить AssertionError.

        Результат:
          - fig: matplotlib.figure.Figure.
        """
        assert self._data, 'Нет данных!'

        title = 'Выборы в государственную думу(2016): Результаты'

        fig, ax = plt.subplots()
        fig.canvas.set_window_title(title)

        values = [i[-1] for i in self._data[1:]]
        labels = [i[1] + ' ({:.2f}%)'.format(i[-1] * 100)
                         for i in self._data[1:]]
        # colors = []
        explode = [0.15 for i in range(len(values))]
        ax.pie(values, explode=explode)
        ax.legend(labels)

        # Смещение оси и легенды
        ax.set_position([0.2, 0.1, 1.5, 0.8])
        plt.legend(labels, bbox_to_anchor=(1., 0.8))
        ax.set_aspect("equal")
        fig.tight_layout()

        return fig

    def show_plot(self):
        """Создать изображение и показать его на экране."""
        self._make_plot()
        plt.show()

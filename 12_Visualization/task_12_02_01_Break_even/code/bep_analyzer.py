import numpy as np
import math
# import matplotlib
import matplotlib.pyplot as plt


class BepAnalyzer:
    """Класс BepAnalyzer выполняет:
      - поиск точки безубыточности;
      - построение графика безубыточности.

    Поля:
      - self._data: список словарей данных. Каждый словарь имеет ключи:
          - "bep_x": точка безубыточности (x);
          - "bep_y": точка безубыточности (y);
          - "fc": постоянные издержки;
          - "ic": себестоимость единицы продукции;
          - "price": цена единицы продукции.

    Методы:
      - self.find_bep(): определение точки безубыточности;
      - self.add_data(): добавление данных для анализа;
      - self.clear_data(): очистка данных для анализа;
      - self._make_plot(): формирование изображения;
      - self.show_plot(): вывод изображения.
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

        Анализируемые данные (2):
        1.
          - bep_x: 600
          - bep_y: 150000
          - fc: 30000
          - ic: 200
          - price: 250
        2.
          - bep_x: 38
          - bep_y: 38000
          - fc: 30000
          - ic: 200
          - price: 1000
        """

        res = 'Анализируемые данные ({}):'.format(len(self._data))
        for i, dct in enumerate(self._data):
            res += '\n{}.'.format(i + 1)
            # print(dct)
            for item in sorted(dct.items(), key=lambda x: x[0]):
                res += '\n  - {}: {}'.format(*item)

        return res

# разве это не должен быть метод класса?
# если нет, тогда зачем аргументы кроме селф?
    def find_bep(self, ic, fc, price):
        """Определить и вернуть значение точки безубыточности.

        Параметры:
          - ic (int или float, > 0): себестоимость единицы продукции;
          - fc (int или float, > 0): постоянные издержки;
          - price (int или float, > ic): цена единицы продукции.

        При несоответствии типов и/или значений возбудить AssertionError.

        Результат:
          - словарь вида: {'bep_x': 150, 'bep_y': 60000}, где:
            - 150: кол-во продукции (целое число);
            - 60000: доход при производстве 150 единиц продукции.
        """
        self._check_args(ic, fc, price)
        bep_x = math.ceil(fc / (price - ic))
        return {'bep_x': bep_x, 'bep_y': bep_x * price}

    def add_data(self, ic, fc, price):
        """Добавить данные для анализа в 'self._data'.

        Параметры:
          - ic (int или float, > 0): себестоимость единицы продукции;
          - fc (int или float, > 0): постоянные издержки;
          - price (int или float, > ic): цена единицы продукции.

        При несоответствии типов и/или значений возбудить AssertionError.
        """
        self._check_args(ic, fc, price)
        dct = {'ic': ic, 'fc': fc, 'price': price}
        dct.update(self.find_bep(**dct))
        self._data.append(dct)

    def clear_data(self):
        """Очистить данные для анализа."""
        self._data = []

    def _make_plot(self):
        """Генерирует изображение, не отображая его.

        Изображение должно включать несколько диаграмм по горизонтали,
        количество которых равно длине 'self._data'.

        Если 'self._data' не содержит данных, возбудить AssertionError.

        Длина оси OX для каждой диаграммы должна быть вдвое больше
        значения точки безубыточности.

        Результат:
          - fig: matplotlib.figure.Figure.
        """
        assert self._data, 'Нет данных!'

        title = 'График безубыточности'

        fig, ax = plt.subplots(ncols=len(self._data))
        fig.canvas.set_window_title(title)

        for i, dct in enumerate(self._data):
            ax[i].set_title(
                title +
                'при цене = {:.2f} руб.'.format(
                    float(
                        dct['price'])))
            ax[i].set_xlabel('Шт.')
            ax[i].set_ylabel('Руб.')

            x = np.arange(2 * dct['bep_x'])
            y = np.arange(2 * dct['bep_y'])
# попробавть без листа, и надо ли прибавить единицу?

            ax[i].plot(x, [dct['fc']] * len(x), 'orange',
                       linewidth=2, label='Постоянные издержки (FC)')
# не уверен насчет квадратных скобок и вообще
            ax[i].plot(
                x,
                x * dct['ic'],
                'green',
                linewidth=2,
                label='Переменные издержки (VC)')
            ax[i].plot(
                x,
                dct['fc'] +
                x *
                dct['ic'],
                'red',
                marker='o',
                label='Валовые издержки (TC)')
            ax[i].plot(
                x,
                x * dct['price'],
                'blue',
                linewidth=2,
                label='Валовый доход (TR)')

            ax[i].plot(x, [dct['bep_y']] * len(x), 'black', linestyle='dashed')
            ax[i].plot([dct['bep_x']] * len(y), y, 'black', linestyle='dashed')

            text = ("Точка\nбезубыточности\n$BEP = \\frac{FC}{PRICE-AVC}$"
                    + "\n({}, {})".format(dct['bep_x'], dct['bep_y']))
            ax[i].annotate(text,
                           xy=(len(x) * 0.5,
                               len(y) * 0.5),
                           xytext=(len(x) * 0.05,
                                   len(y) * 0.8),
                           arrowprops=dict(facecolor="black",
                                           arrowstyle="->"))
# координаты - вовсе не левый верхний угол
            ax[i].legend(loc="upper right")

            ax[i].set_xlim(0, len(x))
            ax[i].set_ylim(0, len(y))
            ax[i].set_aspect(1 / dct['price'])

        return fig

    def show_plot(self):
        """Создать изображение и показать его на экране."""
        self._make_plot()
        plt.show()

    @staticmethod
    def _check_args(ic, fc, price):
        assert (isinstance(ic, (int, float)) and isinstance(fc, (int, float))
                and isinstance(price, (int, float)) and price > ic > 0
                and fc > 0), 'Недопустимые значения!'

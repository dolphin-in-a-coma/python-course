from card import Card
from card_list import CardList
import options


class CardTable:
    """Класс CardTable представляет игорный стол.

    Умеет:
      - хранить карты, лежащие на столе;
      - "отдавать" карту;
      - определять - пуст или нет.

    Атрибуты экземпляра класса:
      - self._card_list (CardList): набор карт на столе.

    Методы экземпляра класса:
      - self.take_card(): берет карту со стола;
      - self.is_empty(): True, если на слоле нет карт.

    Свойства:
      - card_count (int): количество карт на столе.
    """

    def __init__(self, cards_count):
        """Инициализация стола.

        Параметры:
          - cards_count (int): количество карт для игры.

        При инициализации стола происходит генерация набора
        из 'cards_count' карт (номерами от 1 до 'cards_count').
        Если options.debug == True, карты должны быть лицом вверх.
        После генерации их необходимо перемешать -
        используйте self._card_list.shuffle().

        Необходимо удостовериться, что 'cards_count' > 1.
        """
        assert cards_count > 1, 'Количество карт должно быть больше единицы'
        self._card_list = CardList()
        # print(self._card_list._cards)
        self._card_list._cards = [Card(x) for x in range(1, cards_count + 1)]
        # self._card_list._cards=map(Card,list(range(1,cards_count+1)))
# кажется нельзя использовать мап для создания списка объектов класса
        # print(self._card_list._cards)
# используется поле CardList с '_', еще map может не работать с range
        # print(options.debug)
        if options.debug:
            # print('love')
            list(map(lambda x: x.turn_face(), self._card_list._cards))
# почему мап работает только, когда конвертируется в список???
        # print(self._card_list._cards[0].is_face)
# можно ли без lambda?
        self._card_list.shuffle()

    def __str__(self):
        """Вернуть строковое представление карт на столе.

        Формат:

        Карты на столе (3): X X X
        """

        return('Карты на столе ({}): {}'.format(self.card_count,
                                                self._card_list))

    def take_card(self, index):
        """Взять (вернуть) со стола одну карту под номером 'index'.

        Параметры:
          - 'index' - номер карты, начиная с 1.

        Исключения:
          - IndexError: если не 1 <= index <= card_count.
        """
        if not 1 <= index <= self.card_count:
            raise IndexError('Номер карты должен быть в интервале [1;{}]'
                             .format(self.card_count))
        return self._card_list.pop(index - 1)

    def is_empty(self):
        """Вернуть True, если на столе нет карт."""
        return self._card_list.is_empty()

    @property
    def card_count(self):
        """Вернуть количество карт на столе."""
        return len(self._card_list)

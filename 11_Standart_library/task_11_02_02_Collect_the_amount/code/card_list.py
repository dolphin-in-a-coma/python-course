import random
import functools
from card import Card


class CardList:
    """Класс CardList представляет набор карт
    (например, в руке у игрока или на столе).

    Поля экземпляра класса:
      - self._cards (list из Card): карты в наборе.

    Методы экземпляра класса:
      - self.shuffle(): перемешивает карты в наборе;
      - self.append(): добавляет карту в набор;
      - self.remove(): удаляет карту из набора;
      - self.pop(): удаляет и возвращает карту из набора;
      - self.is_empty(): True, если набор пустой;
      - self.sum(): считает сумму значения карт.
    """

    def __init__(self):
        """Инициализация класса."""
        self._cards = []

    def __str__(self):
        """Вернуть строковое представление набора карт.

        Формат: 'карта1 карта2...', например
                '1 2 5', если все карты лежат лицом вверх.

        Для формирования строки используйте functools.reduce().
        """
        return str(functools.reduce(
            lambda res, x: str(res) + ' ' + str(x), self._cards))

    def __len__(self):
        """Размер набора карт."""
        return len(self._cards)

    def shuffle(self):
        """Перемешать набор карт."""
        random.shuffle(self._cards)
# i'm not sure

    def append(self, card):
        """Добавить карту 'card' в набор.

        Необходимо удостовериться, что 'card' -
        экземпляр класса Card (assert).
        """
        assert isinstance(card, Card), 'карта должна принадлежать классу Card'
        self._cards.append(card)

    def pop(self, index):
        """Вытащить (удалить и вернуть) карту
        под индексом 'index' из набора."""
        return self._cards.pop(index)

    def sum(self):
        """Вернуть сумму выбранных карт."""
        return sum(map(lambda x: x.value, self._cards))
# i pray it can work

    def is_empty(self):
        """Вернуть True, если в наборе нет карт."""
        return not bool(len(self))

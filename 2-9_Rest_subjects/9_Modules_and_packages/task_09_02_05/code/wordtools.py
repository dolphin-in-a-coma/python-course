"""Module for working and analysis with text.

    -Cleaning punctuation marks;
    -Tuple of words in the text;
    -Count of words in the text;
    -The longest word in the text;
    -Dictionary of frequency found of words in the text.

    """

rusabc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
engabc = 'abcdefghijklmnopqrstuvwxyz'
abc = rusabc + engabc + (rusabc + engabc).upper()
marks = '.,?!-;:\'"()[]\\/`=+_'


def clean(text):
    """Вернуть строку 'text' без знаков препинания.

    Исключения:
      - TypeError: text - любой тип кроме str.

    Пример: clean("Это, конечно, неправда!?") == "Это конечно неправда"
    """
    if not isinstance(text, str):
        raise TypeError('Text must be str')

    result = ''
    for i in text:
        if i not in marks:
            result += i
    return result


def words(text):
    """Вернуть слова из 'text' в виде кортежа.

    Исключения:
      - TypeError: text - любой тип кроме str.

    Пример: words("Это, конечно, неправда!?") == ('Это', 'конечно', 'неправда')
    """
    if not isinstance(text, str):
        raise TypeError('Text must be str')

    answer = []
    word = ''
    for i in text:
        if i in abc:
            word += i
        elif word:
            answer.append(word)
            word = ''
    if word:
        answer += [word]
    return tuple(answer)


def word_count(text):
    """Вернуть количество слов в 'text'.

    Исключения:
      - TypeError: text - любой тип кроме str.

    Пример: word_count("Это, конечно, неправда!?") == 3
    """
    if not isinstance(text, str):
        raise TypeError('Text must be str')

    return len(words(text))


def longest_word(text):
    """Вернуть самое длинное слово в 'text'.

    Исключения:
      - TypeError: text - любой тип кроме str.

    Пример: longest_word("Это, конечно, неправда!?") == "неправда"
    """
    if not isinstance(text, str):
        raise TypeError('Text must be str')

    if not words(text):
        return ''

    return max(words(text), key=lambda a: len(a))


def char_stats(text):
    """Вернуть словарь-статистику встречаемости букв в 'text'.

    Исключения:
      - TypeError: text - любой тип кроме str.

    Пример: char_stats("папка") == {'а': 2, 'п': 2, 'к': 1}
    """
    if not isinstance(text, str):
        raise TypeError('Text must be str')

    answer = {}
    for i in text.lower():
        if answer.get(i, False):
            answer[i] += 1
        elif i in abc:
            answer[i] = 1
    return answer

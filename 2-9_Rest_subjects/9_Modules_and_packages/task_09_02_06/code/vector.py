"""Module for working with vectors.

    -Creating vector;
    -Checking it's vector or not;
    -Length of vector;
    -Multiplication of vector by a number;
    -Scalar multiplication of two vectors;
    -Angle between two vectors.
    """

import math


def create(x1, y1, x2, y2):
    """Создать и вернуть вектор по точкам.

    Параметры:
        x1, y1: точка - начало вектора
        x2, y2: точка - конец вектора

    Исключения:
      - TypeError: x1, y1, x2, y2 - не int или float.

    Результат:
        {"start": [x1, y1], "end": [x2, y2]}
    """
    if not(isinstance(x1, (int, float)) and isinstance(x2, (int, float))
           and isinstance(y1, (int, float)) and isinstance(y2, (int, float))):
        raise TypeError('Arguments must be a number!')

    return {"start": [x1, y1], "end": [x2, y2]}


def is_vector(vector):
    """Вернуть True, если `vector` -
    структура формата, возвращаемого create(...)."""
    try:
        return len(vector) == 2\
            and (create(*vector['start'], *vector['end'])) == vector

    except Exception:
        return False


def length(vector):
    """Вернуть длину `vector`.

    Исключения:
      - TypeError: `vector` - не вектор.

    Параметры:
        `vector`: структура формата, возвращаемого create(...).
    """
    if not is_vector(vector):
        raise TypeError('Argument must be a vector!')

    return ((vector["start"][0] - vector['end'][0])**2 +
            (vector["start"][1] - vector['end'][1])**2)**0.5


def multiply(vector, num):
    """Вернуть `vector`, умноженный на число `num`.

    Исключения:
      - TypeError: `vector` - не вектор.
    """
    if not is_vector(vector):
        raise TypeError('First argument must be a vector!')
    if not isinstance(num, (int, float)):
        raise TypeError('Second argument must be a number!')

    return create(vector['start'][0] * num, vector['start'][1] * num,
                  vector['end'][0] * num, vector['end'][1] * num)


def scalar_product(vector1, vector2):
    """Вернуть скалярное произведение `vector1` на `vector2`.

    Параметры:
        `vector1`, `vector2`: структура формата, возвращаемого create(...).

    Исключения:
      - TypeError: `vector1` или `vector2` - не вектор.
    """
    if not (is_vector(vector1) and is_vector(vector2)):
        raise TypeError('Arguments must be vectors!')

    return (vector1['end'][0] - vector1['start'][0]) *\
        (vector2['end'][0] - vector2['start'][0]) +\
        (vector1['end'][1] - vector1['start'][1]) *\
        (vector2['end'][1] - vector2['start'][1])


def angle_between(vector1, vector2):
    """Вернуть угол в градусах между `vector1` на `vector2`.

    Исключения:
      - TypeError: `vector1` или `vector2` - не вектор.
    """
    if not (is_vector(vector1) and is_vector(vector2)):
        raise TypeError('Arguments must be vectors!')

    return round((math.acos(scalar_product(vector1, vector2) /
                  length(vector1) / length(vector2))) / math.pi * 180, 4)

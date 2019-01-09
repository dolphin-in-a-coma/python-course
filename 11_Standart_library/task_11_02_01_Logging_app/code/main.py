# ПРОБЛЕМА ВКЛЮЧЕНИЯ!!!!!!!!!
import datetime
import platform
from settings import Settings


def get_last_run_info(settings, launch_dt):
    """Вернуть кортеж вида: (
       Количество запусков программы,
       Количество секунд с последнего запуска,
       Информация о платформе
    ).

    Если программа не была запущена ранее:
      - количество запусков: 0,
      - количество секунд: -1,
      - информации о платформе: пустой кортеж.

    Параметры:
      - settings: настройки - экземпляр класса Settings;
      - launch_dt (datetime.datetime): дата/время запуска программы.
    """
    last_time = settings.get_value('last_run_datetime', False)
    if last_time:
        sek = (launch_dt - last_time).total_seconds()
    else:
        sek = -1

    return (settings.get_value('run_count', 0),
            sek,
            tuple(settings.get_value('last_run_platform_info', ())))


def update_last_run_info(settings, launch_dt):
    """Установить новые значения для настроек:

      - количество запусков программы должно быть увеличено на 1;
      - установлена дата/время последнего запуска (текущая);
      - установлена информация о текущей платформе (platform.uname()).

    Параметры:
      - settings: настройки - экземпляр класса Settings;
      - launch_dt (datetime.datetime): дата/время запуска программы.
    """
    settings.set_value('run_count', settings.get_value('run_count', 0) + 1)
    settings.set_value('last_run_datetime', launch_dt)
    settings.set_value('last_run_platform_info', tuple(platform.uname()))


if __name__ == "__main__":

    launch_dt = datetime.datetime.now()  # Время запуска приложения

    settings = Settings()
    try:
        settings.load()

        run_count, last_run_seconds, last_run_platform_info = \
            get_last_run_info(settings, launch_dt)

        print("Сейчас программа запущена: {}-й раз.".format(run_count + 1))
        if run_count > 0:
            print("С предыдущего запуска прошло {} с.".
                  format(last_run_seconds))
            print("Информация о платформе: {}".format(last_run_platform_info))

        update_last_run_info(settings, launch_dt)
        settings.save()
    except Exception as err:
        print("Во время работы приложения произошла ошибка:", err)

# -------------
# Пример вывода:
#
# Сейчас программа запущена: 1-й раз.

# -------------
# Пример вывода:
#
# Сейчас программа запущена: 3-й раз.
# С предыдущего запуска прошло 12 с.
# Информация о платформе: ('Windows', 'user-pc', '10', '10.0.14393', 'AMD64',
# 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel')

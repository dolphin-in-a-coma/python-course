import sys
import os.path
import requests
import tkinter as Tk
import tkinter.ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from vk import Vk

TITLE = "Автопостинг ВКонтакте"

# Токен должен быть создан с правами wall,photos
TOKEN = "***"

# -------------------
# Начальные настройки
ID = 0
MESSAGE = """\
Программирование на языке высокого уровня.
Курс: http://yuripetrov.pythonanywhere.com/python/

Сообщение оставлено из Python-кода и содержит:
 - изображение;
 - геолокацию;
 - ссылку;
 - хештеги: #Python.

Группа ВК:
 - https://vk.com/python_yup.\
"""
LAT = 55.755814
LONG = 37.617635
IMAGE_FILENAME = "python-snake.jpg"
URL = "https://www.python.org/"
# -------------------


def on_browse_image():
    """Открыть диалог и выбрать файл с изображением."""
    image_filename = askopenfilename(filetypes=(("Изображения",
                                                 "*.png;*.jpg"),))
    if image_filename:
        edt_image_filename.delete(0, Tk.END)
        edt_image_filename.insert(Tk.END, image_filename)


def on_post():
    """Выполнить пост на стене ВКонтакте."""
    access_token = edt_access_token.get().strip()
    vk = Vk(access_token)
    try:
        # Данные из текстовых полей
        owner_id = int(edt_owner_id.get())
        message = edt_message.get(1.0, Tk.END).strip()
        location = {"lat": float(edt_lat.get()),
                    "long": float(edt_long.get())}
        image_filename = edt_image_filename.get().strip()
        link = edt_link.get().strip()

        # Пост
        post_id = vk.wall_post(
            owner_id, message, location, image_filename, link
        )

        messagebox.showinfo(
            TITLE,
            "Пост №{} успешно отправлен на публикацию!".format(post_id)
        )
    except requests.exceptions.ConnectionError as err:
        messagebox.showerror(
            TITLE,
            "Не удается выполнить запрос к ресурсу...\n\n{}".format(err)
        )
    except Exception as err:
        messagebox.showerror(
            TITLE,
            "Во время работы приложения произошла ошибка:\n\n{}".format(err)
        )


if __name__ == "__main__":
    app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    image_filename = os.path.join(app_path, IMAGE_FILENAME)

    # Главное окно приложения
    app = Tk.Tk()
    app.title(TITLE)

    WIDTH = 65

    # ID пользователя
    Tk.Label(text="ID пользователя:").grid(row=0, sticky=Tk.E)

    edt_owner_id = Tk.Entry(app)
    edt_owner_id.grid(row=0, column=1, sticky=Tk.W+Tk.E)
    edt_owner_id.insert(Tk.END, str(ID))

    # Сообщение
    Tk.Label(text="Сообщение:").grid(row=1, sticky=Tk.E)

    edt_message = Tk.Text(app, width=WIDTH, height=13)
    edt_message.grid(row=1, column=1, sticky=Tk.W+Tk.E)
    edt_message.insert(Tk.END, MESSAGE)

    # Местоположение (широта)
    Tk.Label(text="GPS (широта):").grid(row=2, sticky=Tk.E)

    edt_lat = Tk.Entry(app, width=WIDTH)
    edt_lat.grid(row=2, column=1, sticky=Tk.W+Tk.E)
    edt_lat.insert(Tk.END, str(LAT))

    # Местоположение (долгота)
    Tk.Label(text="GPS (долгота):").grid(row=3, sticky=Tk.E)

    edt_long = Tk.Entry(app, width=WIDTH)
    edt_long.grid(row=3, column=1, sticky=Tk.W+Tk.E)
    edt_long.insert(Tk.END, str(LONG))

    # Изображение
    Tk.Label(text="Изображение:").grid(row=4, sticky=Tk.E)

    edt_image_filename = Tk.Entry(app, width=WIDTH)
    edt_image_filename.grid(row=4, column=1, sticky=Tk.W+Tk.E)
    edt_image_filename.insert(Tk.END, image_filename)

    btn_browse = Tk.Button(app, text="...", command=lambda: on_browse_image())
    btn_browse.grid(row=4, column=3)

    # Ссылка
    Tk.Label(text="Ссылка:").grid(row=5, sticky=Tk.E)

    edt_link = Tk.Entry(app, width=WIDTH)
    edt_link.grid(row=5, column=1, sticky=Tk.W+Tk.E)
    edt_link.insert(Tk.END, URL)

    # Линия
    tkinter.ttk.Separator(app, orient=Tk.HORIZONTAL).\
        grid(row=6, columnspan=3, sticky=Tk.W+Tk.E)

    # Токен
    Tk.Label(text="Токен:").grid(row=7, sticky=Tk.E)

    edt_access_token = Tk.Entry(app, width=WIDTH)
    edt_access_token.grid(row=7, column=1, sticky=Tk.W+Tk.E)
    edt_access_token.insert(Tk.END, TOKEN)

    # Кнопка
    btn_post = Tk.Button(app, text="Отправить!", command=lambda: on_post())
    btn_post.grid(row=8, column=0, columnspan=3)

    # Запуск
    app.mainloop()

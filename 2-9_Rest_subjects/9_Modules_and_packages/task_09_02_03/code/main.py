import tkinter as Tk


def set_text(e, text):
    """Установить 'text' в элементе 'e'."""
    e.delete(0, Tk.END)
    e.insert(0, text)


def make_operation(a, b, op):
    """Вернуть результат операции 'op' над 'a' и 'b'."""
    if op == "+":
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '//':
        return a // b
    elif op == '%':
        return a % b
    else:
        return None


def on_click(op):
    try:
        x = float(edt_x.get())
        y = float(edt_y.get())
        set_text(edt_result, "{}".format(make_operation(x, y, op)))
    except Exception as err:
        print(err)  # Текст ошибки выводится в терминал
        set_text(edt_result, "Не могу выполнить операцию!")


if __name__ == "__main__":
    # Главное окно приложения
    app = Tk.Tk()
    app.title("Мини-калькулятор")
    Tk.Label(text="Введите 2 числа и нажмите кнопку:"). \
        pack(side=Tk.TOP, padx=10, pady=10)

    # 1-е текстовое поле
    edt_x = Tk.Entry(app, width=20)
    edt_x.pack(side=Tk.TOP, padx=10, pady=10)

    # 2-е текстовое поле
    edt_y = Tk.Entry(app, width=20)
    edt_y.pack(side=Tk.TOP, padx=10, pady=10)

    # Область для кнопок
    buttons_frame = Tk.Frame(height=2, bd=2, relief=Tk.SUNKEN)
    buttons_frame.pack(padx=10, pady=10)

    # Кнопка
    Tk.Button(buttons_frame, text="+", command=lambda: on_click("+")). \
        pack(side=Tk.LEFT)

    # -
    Tk.Button(buttons_frame, text="-", command=lambda: on_click("-")). \
        pack(side=Tk.LEFT)
    # *
    Tk.Button(buttons_frame, text="*", command=lambda: on_click("*")). \
        pack(side=Tk.LEFT)
    # /
    Tk.Button(buttons_frame, text="/", command=lambda: on_click("/")). \
        pack(side=Tk.LEFT)
    # //
    Tk.Button(buttons_frame, text="//", command=lambda: on_click("//")). \
        pack(side=Tk.LEFT)
    # %
    Tk.Button(buttons_frame, text="%", command=lambda: on_click("%")). \
        pack(side=Tk.LEFT)

    # Результат - текстовое поле
    edt_result = Tk.Entry(app, width=50)
    edt_result.pack(side=Tk.TOP, padx=10, pady=10)

    # Запуск
    app.mainloop()

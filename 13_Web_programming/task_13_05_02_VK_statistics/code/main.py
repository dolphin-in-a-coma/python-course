from vk import VK

try:
    user = int(input("Введите id: "))
    token = input("Введите токен: ")
    vk = VK(user, token)
    print(vk)
    vk.show_plot()
except Exception as err:
    print("Во время работы произошла ошибка: ", err)

from mailer import Mailer
import getpass

mail = input('Введите ваш почтовый адрес: ')
password = getpass.getpass('Введите пароль от почтового ящика: ')
mail = Mailer(mail, password)
mail.run()

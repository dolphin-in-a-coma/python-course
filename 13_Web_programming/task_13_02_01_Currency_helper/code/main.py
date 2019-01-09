from currency_checker import CurrencyChecker

if __name__ == "__main__":
    # Данные руководителя
    ceo_name = 'JJ'
    ceo_email = 'eugenartemovich@gmail.com'

    checker = CurrencyChecker(ceo_name, ceo_email)
    checker.run(timeout=30, currencies=["USD", "EUR", "AAA"])

# -------------
# Пример вывода:
#
# 2017-03-22 14:27:42 | Произошла ошибка:
#                       HTTPConnectionPool(host='www.finanz.ru', port=80)...
#
# 2017-03-22 14:06:22 | Данные получены: [('EUR', (62.6697, '12:00:00')),
#                                         ('USD', (58.0517, '12:00:00'))]
# 2017-03-22 14:06:24 | Письмо успешно отправлено!
#
# 2017-03-22 14:38:17 | Данные получены:
#                       [('AAA', ('Нет данных', 'Нет данных')),
#                        ('EUR', (62.6213, '12:35:00')),
#                        ('USD', (58.0336, '12:35:00'))]
# 2017-03-22 14:38:19 | Письмо успешно отправлено!
#
# -------------
# Пример письма:
#
# Никанор Петрович!
#
# Обновленные курсы валют:
#
#   - EUR: 62.6697 (12:00:00)
#   - USD: 58.0517 (12:00:00)
#
# С уважением, ИТ-отдел.
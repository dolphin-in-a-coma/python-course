from currency_checker import CurrencyChecker
ceo_name = 'JJ'
ceo_email = 'vegansneacker@gmail.com'

checker = CurrencyChecker(ceo_name, ceo_email)
cur = ['CNY', 'EUR', 'БИЧ']
cur.append('USD')

print(checker._create_message(checker.get_info(tuple(cur))))
print(checker.run(1, cur))
# checker.send_mail(checker._create_message(checker.get_info(tuple(cur))))

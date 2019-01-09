import random
month=random.randint(1,12)
year=random.randint(1900,2000)
year_td=random.randint(2001,2100)
month_td=random.randint(1,12)
print('месяц/год рожд.: {}/{}\nгод/месяц сегодня:{}/{}'.format(month, year, month_td, year_td))
old=year_td-year
if month_td<month:
    old-=1
print(old)    

import random
m=random.randint(1,24*60)
h=m//60
m_past_h=m%60
print('Всего минут:{:>14}\nВсего часов:{:>14}\nМинут в последнем часу:{:>3}'
.format(m,h,m_past_h))

team=input('твоя команда: ')
print(team + ' - чемпион')
i=len(team)
print(i*'-')
team=team.lower()
print(team)
print('длина = ', i)
print('буква "п" в названии:', 'п' in team)
print('"а" встречается в названии {} раз'.format(team.count('а')))

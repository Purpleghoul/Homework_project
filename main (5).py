boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys)!=len(girls):
  print('Кто-то может остаться без пары.')
else:
  print('Идеальные пары:')
  for x, y in zip(boys, girls):
    print(f'{x} и {y}')
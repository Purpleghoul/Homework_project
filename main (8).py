queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


search={}
percent= int(100/len(queries))
for items in queries:
  lenght=len(items.split())
  search[lenght]=search.get(lenght,0)+1
for key,val in search.items():
      print('Количество слов:', key, val*percent, '%')

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
myset= set()
for numbers in list(ids.values()):
  for elem in numbers:
    myset.add(elem)
res=list(myset)
print(res)

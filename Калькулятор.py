basic_stake = 7
region =input("Клиент с Дальнего Востока?").lower()
if region == "да":
  basic_stake = 2
  print ("Ипотечная ставка: ",basic_stake,"процента")
else:
  child_count =int(input("Введите количество детей: "))
  if child_count > 3:
    basic_stake-= 1
  salary = input("Есть ли у клиента зарплатный проект? ").lower()
  if salary=="да":
    basic_stake-= 0.5
  insurance = input("Есть ли у клиента страхование? ").lower()
  if insurance=="да":
    basic_stake-=1.5
  print ("Ипотечная ставка: ", basic_stake," процентов")
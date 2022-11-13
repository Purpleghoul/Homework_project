month=input("Введите месяц: ").lower()
date=int(input("Введите число: "))
if (month == "март" and 21<= date <=31) or (month == "апрель" and 1<= date <=19):
  print("Вывод:")
  print("Овен")
elif (month == "апрель" and 20<= date <=30) or (month == "май" and 1<= date <=20):
  print("Вывод:")
  print("Телец")
elif (month == "май" and 21<= date <=31) or (month == "июнь" and 1<= date <=21):
  print("Вывод:")
  print("Близнецы")
elif (month == "июнь" and 22<= date <=30) or (month == "июль" and 1<= date <=22):
  print("Вывод:")
  print("Рак")
elif (month == "июль" and 23<= date <=31) or (month == "август" and 1<= date <=22):
  print("Вывод:")
  print("Лев")
elif (month == "август" and 23<= date <=31) or (month == "сентябрь" and 1<= date <=22):
  print("Вывод:")
  print("Дева")
elif (month == "сентябрь" and 23<= date <=30) or (month == "октябрь" and 1<= date <=23):
  print("Вывод:")
  print("Весы")
elif (month == "октябрь" and 24<= date <=31) or (month == "ноябрь" and 1<= date <=22):
  print("Вывод:")
  print("Скорпион")
elif (month == "ноябрь" and 23<= date <=30) or (month == "декабрь" and 1<= date <=21):
  print("Вывод:")
  print("Стрелец")
elif (month == "декабрь" and 22<= date <=31) or (month == "январь" and 1<= date <=20):
  print("Вывод:")
  print("Козерог")
elif (month == "январь" and 21<= date <=31) or (month == "февраль" and 1<= date <=19):
  print("Вывод:")
  print("Водолей")
elif (month == "февраль" and 19<= date <=28) or (month == "март" and 1<= date <=20):
  print("Вывод:")
  print("Водолей")
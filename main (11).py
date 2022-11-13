documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}

def people(documents):
  doc_num_people=input('Введите номер документа: ')
  for logs in documents:
    if doc_num_people in logs.values():
      result_people=logs["name"]
      return result_people


def shelf(directories):
  doc_num_shelf=input('Введите номер документа: ')
  for key, numbers in directories.items():
    if doc_num_shelf in numbers:
      return key
  else:
      return "Такого номера не существует."


def type():
    type = []
    for type_doc in documents:
        type.append(type_doc["type"])
    return type

def number():
    number = []
    for number_doc in documents:
        number.append(number_doc["number"])
    return number

def name():
    name = []
    for name_doc in documents:
         name.append(name_doc["name"])
    return name

def items_list(type, number, name):
    for item in range(len(type)):
        print(type[item], number[item], name[item])


def new_log(documents):
  new_docs={}
  doc_type= input('Введите тип документа: ')
  new_docs["type"]=doc_type
  doc_num= input('Введите номер документа: ')
  new_docs["number"]=doc_num
  doc_name= input('Введите ФИО: ')
  new_docs["name"]=doc_name
  documents.append(new_docs)
  shelf_num=input('Введите номер полки: ')
  for shelf_number, shelf_items in directories.items():
    if shelf_num in shelf_number:
      shelf_items.append(doc_num)
      return documents,directories
  else:
      return 'Такой полки не существует.'

def delete(documents):
  del_num= input('Введите номер документа: ')
  docs=[]
  for del_voc in documents:
    if del_voc.get('number') != del_num:
      docs.append(del_voc)
  for del_val_shelf in directories.values():
    if del_num in del_val_shelf:
      del_val_shelf.remove(del_num)
      return docs,directories
  else:
      return 'Такого документа не существует.'

def move(directories):
  plus_num= input('Введите номер документа: ')
  src_list=[]
  dest_list=[]
  for shelf_num,shelf_val in directories.items():
    if plus_num in shelf_val:
      src_list = directories[shelf_num]
      src_list.remove(plus_num)
    else:
      return 'Такого документа не существует.'
    try:
      plus_key = input('Введите номер полки: ')
      if plus_num not in dest_list:
        dest_list = directories[plus_key]
        dest_list.append(plus_num)
    except:
      return 'Такой полки не существует.'
    return directories

def add_shelf(directories):
  new_shelf= input('Введите номер новой полки: ')
  if new_shelf in directories.keys():
    return 'Полка с таким номером уже создана.'
  else:
    directories[new_shelf]=[]
  return directories

def main(documents,directories):
  while True:
    user_input = input('Введите команду: ')
    if user_input == 'p':
      """Функция выводит имя человека по номеру документа."""
      print(people(documents))
    elif user_input == 's':
      """Функция выводит номер полки по номеру документа."""
      print(shelf(directories))
    elif user_input == 'l':
      """Функция выводит список всех документов."""
      items_list(type(), number(), name())
    elif user_input == 'a':
      """Функция добавляет новую запись в список и помещает ее на указанную полку."""
      print(new_log(documents))
    elif user_input == 'd':
      """Функция удаляет запись из списка и номер документа из списка полок."""
      print(delete(documents))
    elif user_input == 'm':
      """Функция переносит номер документа с одной полки на другую."""
      print(move(directories))
    elif user_input == 'as':
      """Функция создает новую полку."""
      print(add_shelf(directories))
    elif user_input == 'q':
      print('До свидания!')
      break
      
main(documents,directories)



  

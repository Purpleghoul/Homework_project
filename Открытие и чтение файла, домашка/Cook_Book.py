from pprint import pprint

file_path = "Cookbook.txt"
def make_cook_book(file_path):
    new_cook_book = {}
    with open("Cookbook.txt", encoding='UTF-8') as file:
        for recipe_name in file:
            recipe_name = recipe_name.strip()
            ingredients_amount = int(file.readline())
            ingredients_list = []
            for items in range(ingredients_amount):
                ingr = file.readline().split(' | ')
                ingredients = {'ingredient_name': ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
                ingredients_list.append(ingredients)
            new_cook_book[recipe_name] = ingredients_list
            file.readline()
        return new_cook_book
pprint(make_cook_book(file_path), width=70)

def get_shop_list_by_dishes(dishes: list, file_path: str, person_count=1):
    new_cook_book=make_cook_book(file_path)
    ingr_book={}
    for dishes_list in new_cook_book:
        for ingr_list in new_cook_book.get(dishes_list, []):
            if ingr_list['ingredient_name'] in ingr_book:
                ingr_book[ingr_list['ingredient_name']]['quantity'] += ingr_list['quantity'] * person_count
            else:
                ingr_book[ingr_list['ingredient_name']] = {'quantity': ingr_list['quantity'] * person_count, 'measure': ingr_list['measure']}
    return ingr_book
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], ..., 3))

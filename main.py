def get_cook_book(recipes_file='recipes.txt'):
    with open(recipes_file, 'r', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            dish, _, *ingredients = txt.split('\n')
            list_ = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ingredient.split(' | '))
                list_.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = list_
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_ingredient = dict(ingredient)
            new_ingredient['quantity'] *= person_count
            if new_ingredient['ingredient_name'] not in shop_list:
                shop_list[new_ingredient['ingredient_name']] = new_ingredient
            else:
                shop_list[new_ingredient['ingredient_name']]['quantity'] += new_ingredient['quantity']
    return shop_list


cook_book = get_cook_book()
print(cook_book)
print()
shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
print(shop_list)

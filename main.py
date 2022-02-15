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


cook_book = get_cook_book()
print(cook_book)

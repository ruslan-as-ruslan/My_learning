def print_products(*args):
    x = 0
    for i in args:
        if type(i) is str and i:
            x += 1
            print(f"{x}) {i}")
    if not i: print('Нет продуктов')



print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# products = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# 'название': ['компьютер', 'принтер', 'сканер'],
# 'цена': [20000, 6000, 2000],
# 'количество': [5, 2, 7],
# 'ед': ['шт.']
# }
keys = ['название', 'цена', 'количество', 'eд']

products = []
index = 1

while True:
    answer = input('Добавить новый элемент?')
    if answer.lower() == 'нет':
        break
    element = {}
    for key in keys:
        value = input(f'Введите {key}:')
        element[key] = value
    products.append((index, element))
    index += 1

print(products)

analytics = {}

for _, item in products:
    for key in keys:
        if key not in analytics.keys():
            analytics.setdefault(key, set())
        analytics[key].add(item[key])

print(analytics)

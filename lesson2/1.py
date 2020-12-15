# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = list()

new_list.append('first_element')
new_list.append(34)
new_list.append(True)
new_list.append(3.14)

for item in new_list:
    print(type(item))

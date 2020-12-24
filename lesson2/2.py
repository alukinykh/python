# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list()

for item in range(1, 10):
    my_list.append(input('Введите элемент списка: '))

for key, val in enumerate(my_list):
    if (key + 1) < len(my_list) and not (key % 2):
        my_list[key], my_list[key + 1] = my_list[key + 1], my_list[key]

print(my_list)

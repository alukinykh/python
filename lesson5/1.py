# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('result_1.txt', 'w') as f_obj:
    while True:
        line = input('Введите данные: ')
        if not line:
            break
        f_obj.write(f'{line}\n')

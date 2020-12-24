# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('task_5.txt', 'w') as out_f:
    for i in range(10):
        out_f.write(f'{randint(1, 100)} ')

with open('task_5.txt') as f_obj:
    list_numbers = f_obj.read().split()
    sum_numbers = 0
    for number in list_numbers:
        sum_numbers += int(number)
    print(sum_numbers)

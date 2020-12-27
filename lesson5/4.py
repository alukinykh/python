# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре'
}

with open('task_4.txt') as f_obj:
    result = []
    for line in f_obj:
        key, sign, val = line.split()
        result.append(f'{rus[int(val)]} {sign} {val}\n')

    with open('result_4.txt', 'w') as out_f:
        out_f.writelines(result)


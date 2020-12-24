# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('task_3.txt') as f_obj:
    employees = f_obj.readlines()
    average = 0
    for line in employees:
        person = line.split()
        average += float(person[1])
        if float(person[1]) < 20000:
            print(person[0])
    print(f'Средний доход сотрудников: {average / len(employees):.2f}')

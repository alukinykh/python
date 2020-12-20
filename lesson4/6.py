# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle


def generate_numbers(start):
    for el in count(start):
        if el > 15:
            break
        else:
            yield el


def repeat_list(current_list):
    iteration = 0
    for el in cycle(current_list):
        if iteration > 10:
            break
        iteration += 1
        yield el


print([el for el in generate_numbers(5)])

print([el for el in repeat_list([1, 2, 3, 4, 5, 6])])

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(number1, number2):
    if not number2:
        return 'На ноль делить нельзя.'
    return number1 / number2


number_1 = int(input('Введите число 1: '))

number_2 = int(input('Введите число 2: '))

result = division(number_1, number_2)

print(result)

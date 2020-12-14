profit = int(input('Введите значение выручки: '))
expense = int(input('Введите значение издержек: '))

if profit > expense:
    profitability = profit / expense
    print('Ваш финансовый результат - прибыль')
    print(f'Ваша рентабельность {profitability:.2f}')
    employees = int(input('Введите количество сотрудников: '))
    profit_on_person = profit / employees
    print(f'Прибыль фирмы в расчете на одного сотрудника {profit_on_person:.2f}')
else:
    print('Ваш финансовый результат - убыток')


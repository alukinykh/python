years = 15

name = input('Введите имя ')
surname = input('Введите фамилию ')
age = int(input('Введите возраст '))

print(name, surname, f'{age} лет')
print(f'Через {years} лет вам будет {age + years}')

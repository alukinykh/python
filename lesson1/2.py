seconds = int(input('Введите время в секундах '))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')

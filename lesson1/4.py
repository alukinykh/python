number = str(input('Введите целое положительное число '))

number_list = list(number)

biggest_number = 0

while len(number_list):
    current_number = int(number_list.pop())
    if biggest_number < current_number:
        biggest_number = current_number

print(biggest_number)
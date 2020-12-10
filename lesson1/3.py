number = input('Введите число чтобы найти сумму n + nn + nnn: ')

iteration = int(number)
sum_number = 0

while iteration:
    sum_number += int(number * iteration)
    iteration -= 1

print(sum_number)

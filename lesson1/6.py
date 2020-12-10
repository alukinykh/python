def get_day(a, b):
    day = 1
    while a < b:
        a = a + a * 0.1
        day += 1
    return day


print(get_day(1, 4))

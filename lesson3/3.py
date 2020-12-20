# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    m_list = list(args)
    m_list.sort(reverse=True)
    res = 0
    for val in m_list[0:2]:
        res += val
    return res


my_func(10, 6, 7)

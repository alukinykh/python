# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transform_to_int(cls, date):
        day, month, year = date.split('-')
        cls.day = int(day)
        cls.month = int(month)
        cls.year = int(year)

    @staticmethod
    def validate_date(date):
        day, month, year = date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return 0 < day < 31 and 0 < month < 13 and year > 0


dt = Date('12-04-2020')
dt.transform_to_int('14-04-2020')
Date.validate_date('10-10-1994')

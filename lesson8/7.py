# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        return f"({self.real} + {self.imaginary}i)"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)


complex1 = ComplexNumber(1, 2)
complex2 = ComplexNumber(2, 3)
print(f"{complex1} + {complex2} = {complex1 + complex2}")
print(f"{complex2} + {complex1} = {complex2 + complex1}")
print(f"{complex1} * {complex2} = {complex1 * complex2}")
print(f"{complex2} * {complex1} = {complex2 * complex1}")
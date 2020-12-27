# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(speed=55, name='Nissan', color='grey', is_police=False)

town_car.go()
town_car.turn("лево")
town_car.stop()
town_car.show_speed()
town_car.speed = 70
town_car.show_speed()
print(f"Town car is police: {town_car.is_police}")

police_car = PoliceCar(100, "white", "bmw")
print(f"Police car is police: {police_car.is_police}")

work_car = WorkCar(30, "yellow", "Matiz")
work_car.show_speed()
work_car.speed = 70
work_car.show_speed()

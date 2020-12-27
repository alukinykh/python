# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.initial_color_list = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        color_list = list(self.initial_color_list)
        index = color_list.index(self.__color)
        current_list = color_list[index::] + color_list[:index:]
        print(current_list)
        while True:
            for val in current_list:
                self.__color = val
                print(self.__color)
                sleep(self.initial_color_list[val])


a = TrafficLight('red')

a.running()

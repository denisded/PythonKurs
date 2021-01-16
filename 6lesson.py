"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
    (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов,
    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    def running(self, __color):
        if __color == "red":
            b1 = 0
        elif __color == "yellow":
            b1 = 1
        else:
            b1 = 2
        lista1 = ["red", "yellow", "green"]
        d1 = 0
        while d1 < 5:  # просто чтобы цикл был не бесконечный
            if b1 == 1:
                c1 = 0
            else:
                c1 = 5
            print(lista1[b1])
            sleep(2 + c1)
            if b1 == 2:
                b1 = 0
            else:
                b1 += 1
            d1 += 1


aclass = TrafficLight()
aclass.running(input("Enter color "))

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
    толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
    Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def massa(self, _length, _width):
        return print(f"Масса асфальта: {_length * _width * 25 * 5 / 1000} тонн")


Road().massa(int(input("Введите длину дороги ")), int(input("Введите ширину дороги ")))

"""
3. Реализовать базовый класс Worker (работник), 
    в котором определить атрибуты: name, surname, position (должность), income (доход). 
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
    например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
    и дохода с учетом премии (get_total_income). 
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
    проверить значения атрибутов, вызвать методы экземпляров).
"""
from functools import reduce


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, _income={"wage": wage, "bonus": bonus})

    def get_full_name(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}")

    def get_total_income(self):
        print(f"Доход {self.position}a равен {reduce(lambda a, b: a / 100 * b + a, self._income.values())}\n")


a3 = Position("Иванов", "Иван", "Директор", 1000, 100)
a31 = Position("Петров", "Гена", "Программист", 500, 200)
a3.get_full_name()
a3.get_total_income()
a31.get_full_name()
a31.get_total_income()

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
    Для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. 
    Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} начал движение")

    def stop(self):
        print(f"{self.color} {self.name} прекратил движение")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернул на{direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} едет со скоростью {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} и это превышение разрешенной скорости")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} и это превышение разрешенной скорости")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(60, "Серый", "Тавота")
car_2 = SportCar(120, "Красный", "Порш")
car_3 = WorkCar(50, "Серый", "Хундай")
car_4 = PoliceCar(90, "Синий", "Форд")
car_1.go()
car_2.go()
car_3.go()
car_4.go()
car_2.stop()
car_4.stop()
car_1.turn("лево")
car_3.turn("право")
car_1.show_speed()
car_3.show_speed()

"""
    5. Реализовать класс Stationery (канцелярская принадлежность).
        Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
        Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
        В каждом из классов реализовать переопределение метода draw.
        Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
        что выведет описанный метод для каждого экземпляра.
    """


class Stationery:
    def __init__(self, title): self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title): super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


class Pencil(Stationery):
    def __init__(self, title): super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


class Handle(Stationery):
    def __init__(self, title): super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


Pen("ручка").draw()
Pencil("карандаш").draw()
Handle("маркер").draw()

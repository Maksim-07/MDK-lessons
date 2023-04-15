'''
Создайте класс Car, реализуйте в нем 5 атрибутов :

цвет,
марку,
кузов (сидан sedan, грузовик truck),
скорость,
тип коробки передач;
и 6 методов:

start - заставляет начинать движение
stop - останавливает машину
turn - поворачивает машину в какую-либо сторону, и выводит сообщение:" Машина повернула налево"
speed_up - ускоряет автомобиль
speed_down - замедляет автомобиль
beep - сигналит
Создайте два экземпляра класса truck и car. Продемонстрируйте работу всех методов
'''
import random


class Car:
    def __init__(self, color, brand, body, transmission, speed=0):
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print('START ENGINE')

    def stop(self):
        print('STOP ENGINE')

    def turn(self):
        print(f"Транспорт повернул {random.choice(['налево', 'направо'])}")

    def speed_up(self, speed=10):
        self.speed += speed
        print(f"Скорость увеличилась: {self.speed} км/ч")

    def speed_down(self, speed=10):
        if self.speed - speed <= 0:
            print('Транспорт остановился')
        else:
            self.speed -= speed
            print(f"Скорость уменьшилась: {self.speed} км/ч")

    def beep(self):
        print('Бип-бип!!')


car = Car(color='black', brand='Audi', body='sedan', transmission='auto')
car.start()
car.turn()
car.speed_up(100)
car.speed_down(50)
car.beep()
car.stop()
print()
truck = Car(color='red', brand='Volvo', body='truck', transmission='auto')
truck.start()
truck.beep()
truck.turn()
truck.speed_up(90)
truck.speed_down(90)
truck.stop()

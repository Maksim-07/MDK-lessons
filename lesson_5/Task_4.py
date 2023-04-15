'''
Добавьте ограничение скорости в класс Car из предыдущего задания: для грузовика(truck) 60 км/ч,
а для легкового(car) - 80 км/ч. При превышении пусть на экран выводится предупреждение:
"Скорость превышена! Разрешенная скорость 60 км/ч"
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
        match self.body:
            case 'sedan':
                speed_limit = 80
                self.speed += speed
                if self.speed > speed_limit:
                    print(f'Скорость превышена! Разрешенная скорость {speed_limit} км/ч')
                else:
                    print(f"Скорость увеличилась: {self.speed} км/ч")
            case 'truck':
                speed_limit = 60
                self.speed += speed
                if self.speed > speed_limit:
                    print(f'Скорость превышена! Разрешенная скорость {speed_limit} км/ч')
                else:
                    print(f"Скорость увеличилась: {self.speed} км/ч")

    def speed_down(self, speed=10):
        if self.speed - speed <= 0:
            print('Транспорт остановился')
        else:
            self.speed -= speed
            print(f"Скорость уменьшилась: {self.speed} км/ч")

    def beep(self):
        print('Бип-бип!!')

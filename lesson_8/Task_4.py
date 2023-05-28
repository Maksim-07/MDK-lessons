"""
Реализуйте класс Truck (грузовик). Грузовик может перевозить посылки - Box из предыдущего задания
Импортиуйте модуль task_3_box из предыдущего задания.
Создайте класс Truck (грузовик), который будет иметь несколько атрибутов, присущих грузовику.
Реализуйте атрибут capacity (емкость), в котором будет реализовано хранилище посылок (Box): [box1, box2 ...]
Переопределите методы __str__, __add__, __sub__ для реализации отображения грузовика, загрузки и выгрузки посылок.
Продемонстрируйте работу класса Truck.
"""
from Task_3 import Box


class Truck:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__boxes = []

    def __str__(self):
        return f"Ёмкость хранилища грузовика {self.__capacity}. Посылки в кузове: {self.__boxes}."

    def __add__(self, other):
        if len(self.__boxes) < self.__capacity:
            self.__boxes.append(other)
            return "Погрузка завершена."
        else:
            return "Кузов грузовика заполнен."

    def __sub__(self, other):
        if len(self.__boxes) <= 0:
            return "Выгружать нечего."
        else:
            self.__boxes.pop(other)
            return "Посылка выгружена."

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто V/6.5+0.5
для костюма 2H+0.3 Проверить работу этих методов на реальных данных.
Выполнить общий подсчет расхода ткани, который пойдет на пошив всех костюмов и всех пальто соответственно. Реализовать
абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloth):
    reserved = 0  # Считает количество ткани для пальто

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        self.reserved = self.size / 6.5 + 0.5
        return self.reserved


class Suit(Cloth):
    reserved = 0  # Считает количество ткани для костюмов

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        self.reserved = 2 * self.height + 0.3
        return self.reserved

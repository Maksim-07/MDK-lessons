'''
Создайте родительский класс Animal, у которого есть 3 атрибута:

color - цвет
name - кличка
age - возраст
и абстрактный метод:
say - издать звук.

Создайте два класса потомка - Cat и Dog, в которых будет переопределен метод say: для класса Cat - Meow!, для Dog - Woof!
'''
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Cat(Animal):

    def say(self):
        print('Meow!')


class Dog(Animal):

    def say(self):
        print('Woof!')

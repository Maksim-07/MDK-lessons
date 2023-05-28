'''
А) Реализовать класс Stationery (канцелярия):

определить в нём атрибут title (название) и абстрактный метод draw (отрисовка);
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в классу Pen добавьте атрибут color = 'blue';
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение,
например: "Ручка пишет";
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
Б)
Добавьте в класс Stationary метод класса set_color, который присваивает атрибут класса Stationary color;
Вызовете метод set_color и установите color='yellow';
Вызовете атрибуты color у классов Pen, Pencil, Handle. Что вы наблюдаете?
'''
from abc import ABC, abstractmethod


class Stationery(ABC):

    def __init__(self, title, color):
        self.title = title
        self.color = color

    @abstractmethod
    def draw(self):
        print('draw')

    def set_color(self, color):
        self.color = color


class Pen(Stationery):
    color = 'blue'

    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):

    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):

    def draw(self):
        print('Маркер выделяет')


pen = Pen(title='Montegrappa', color='')
pen.draw()
pen.set_color(color='yellow')
print(pen.color)

pencil = Pencil(title='Каляка-Маляка', color='')
pencil.draw()
pencil.set_color(color='yellow')
print(pencil.color)

handle = Handle(title='El Casco', color='')
handle.draw()
handle.set_color(color='yellow')
print(handle.color)

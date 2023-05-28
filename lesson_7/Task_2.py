'''
Реализовать класс Queue

Определить атрибут inside, который будет хранить в себе имена людей в очереди.

Переопределить метод __str__, чтобы преобразовать его к виду: Name1=>Name2=>...=>Name3

Реализовать методы:

add - который добавляет имя в очередь
take_out убирает первого человека из списка
Переопределить методы __add__ , __sub__, __iadd__, __isub__ чтобы они соответствовали методам add и take_out
'''


class Queue:

    def __init__(self):
        self.inside = []

    def __str__(self):
        return f" {'=>'.join(self.inside)} "

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)

    def __add__(self, other):
        self.inside.append(other)

    def __sub__(self, other):
        self.inside.pop(0)

    def __iadd__(self, other):
        self.inside.append(other)
        return self

    def __isub__(self, other):
        self.inside.pop(0)
        return self

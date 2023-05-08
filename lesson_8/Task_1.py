"""
Создайте класс Person с приватными атрибутами name, age, surname. Реализуйте методы name, age, surname, которые будут
давать доступ к аналогичным приватным атрибутам. Создайте сеттер, который будет давать возможность поменять атрибут age.
"""


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

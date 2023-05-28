'''
Создайте базовый класс Father, у которого есть два атрибута: name (имя) и surname (фамилия); и дочерний класс Child,
у которого будут унаследованы те же атрибуты и дополнительно атрибут patronim (отчество). Создайте один экземпляр класса Child.
'''


class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Child(Father):
    def __init__(self, name, surname, patronymic):
        super().__init__(name=name, surname=surname)
        self.patronymic = patronymic


child = Child(name='Анна', surname='Перловкина', patronymic='Леонидовна')
print(child.name)  # Анна
print(child.surname)  # Перловкина
print(child.patronymic)  # Леонидовна

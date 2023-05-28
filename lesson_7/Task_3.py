'''
a) Создайте класс Matrix
который должен принимать данные (список списков) для формирования матрицы.
b) Следующий шаг
реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
c) Далеее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''


class Matrix:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for i in self.lst:
            for j in i:
                print(j, end=' ')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.lst)):
            for i_2 in range(len(other.lst[i])):
                self.lst[i][i_2] = self.lst[i][i_2] + other.lst[i][i_2]
        return Matrix.__str__(self)

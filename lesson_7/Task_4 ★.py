'''
Реализуйте класс Deque
Переопределите метод __str__
Реализуйте методы, которые позволят вставлять элементы слева, справа, и в центр массива и аналогично удалять.
'''


class Deque:

    def __init__(self):
        self.list_deque = []

    def __str__(self):
        return f"{self.list_deque}"

    def insert_left(self, element):
        self.list_deque.insert(0, element)

    def insert_right(self, element):
        self.list_deque.append(element)

    def insert_centre(self, element):
        index_centre = len(self.list_deque) / 2
        self.list_deque.insert(int(index_centre), element)

    def pop_left(self):
        try:
            self.list_deque.pop(0)
        except IndexError as ex:
            print(ex)

    def pop_right(self):
        try:
            self.list_deque.pop()
        except IndexError as ex:
            print(ex)

    def pop_centre(self):
        index_centre = len(self.list_deque) / 2
        self.list_deque.pop(int(index_centre))

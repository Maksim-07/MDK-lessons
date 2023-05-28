'''
Создайте класс Good, который будет вычислять значения стоимости товаров. В качестве атрибутов пусть будут:

в качестве методов:
calc - вычисляющий стоимость товара.

Выведите их стоимость
'''


class Good():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calc(self):
        cost = self.weight * self.price
        print(f"[+] The cost of {self.weight} kg of {self.name}s: {cost} [+]")


apple = Good(name='apple', price=100, weight=1.5)
pear = Good(name='pear', price=120, weight=0.8)

apple.calc()
pear.calc()

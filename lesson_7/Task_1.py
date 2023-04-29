'''
Создайте класс Battery, у которой будет определен атрибут capacity = [ ] (емкость), max_charge = 5 (максимальный заряд)
по умолчанию, и методы:

charge - заряжает батарею

discharge - разряжает батарею.

Переопределите метод __str__, чтобы при вызове экземпляра он представлялся в виде: [)))))] - максимально заряженная батарея.
'''


class Battery:
    capacity = []
    max_charge = 5

    def charge(self):
        self.capacity.append(')')

    def discharge(self):
        try:
            self.capacity.pop(-1)
            print(self.capacity)
        except IndexError:
            print('Заряд полностью разрядился.')

    def __str__(self):
        return '[)))))] - максимально заряженная батарея.'

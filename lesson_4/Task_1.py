'''
Создайте функцию-генератор countdown, которая выводит числа от 10 до 0.
а) Опустошите генератор с помощью цикла
б) Опустошите генератор с помощью next()
'''


def countdown():
    for m in range(10, -1, -1):
        yield m


y = countdown()
activity = True
try:
    while activity:
        print(next(y))
except StopIteration:
    activity = False

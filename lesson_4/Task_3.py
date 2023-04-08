'''
Напишите функцию-генератор, которая выводит 10 чисел Фибоначчи. Выведите числа в виде списка (list).
'''


def fibonacci(num):
    num_1, num_2 = 0, 1
    for _ in range(num):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


print(list(fibonacci(10)))

'''
Напишите функцию итератор, которая будет перебирать список чисел Фибоначчи из предыдущего задания.
Опустошите итератор двумя способами.
'''


def fibonacci(num):
    fib = []
    num_1, num_2 = 0, 1
    for _ in range(num):
        fib.append(num_1)
        num_1, num_2 = num_2, num_1 + num_2
    return iter(fib)


# Первый способ.
y = fibonacci(10)
for m in y:
    print(m)

# Второй способ.
for i in fibonacci(10):
    print(i)

'''
Создайте функцию Fibonacci, которая генерирует список чисел Фибоначчи меньше 100.
а) решите эту задачу с помощью цикла while
б) решите эту задачу с помощью рекурсии
'''


def fibonacci(num):
    num_1, num_2 = 0, 1
    while num_1 < num:
        print(num_1, end=' ')
        num_1, num_2 = num_2, num_1 + num_2


def fibonacci_recur(num):
    if num <= 1:
        return num
    return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)


fibonacci(100)
print()
for i in range(12):
    print(fibonacci_recur(i), end=' ')

'''
Создайте функцию factorial, которая принимает число и вычисляет факториал этого числа.
Факториал 5: 5! = 1 * 2 * 3 * 4 * 5
а) решите эту задачу с помощью цикла while
б) решите эту задачу с помощью рекурсии
'''


def factorial(num):
    summa = 1
    for i in range(1, num + 1):
        summa *= i
    return summa


def factorial_recur(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recur(num - 1)


print(factorial(5))
print(factorial_recur(5))

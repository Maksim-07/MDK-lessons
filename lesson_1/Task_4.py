'''
Создайте функцию count, которая выводит числа от 0 до 10. Решите эту задачу с помощью:
а) цикла while
б) с помощью рекурсии
'''


def count_while():
    num = 0
    while num <= 10:
        print(num, end=' ')
        num += 1


def count_recur(zero, num=None):
    print(zero, end=' ')
    if zero == num:
        return
    else:
        count_recur(zero + 1, num=num)


count_while()  # using the while loop
print('')
count_recur(zero=0, num=10)  # using recursion

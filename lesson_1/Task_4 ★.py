'''
Создайте функцию count, которая выводит количество четных и нечетных чисел от 0 до 10. Решите эту задачу с помощью:
а) цикла while
б) с помощью рекурсии
'''


def count_while(number):
    num = 0
    len_even, len_odd = 0, 0
    while num <= number:
        len_even += 1 if num % 2 == 0 else 0
        len_odd += 1 if num % 2 != 0 else 0
        print(num, end=' ')
        num += 1
    print(
        f'\nКоличество четных чисел: {len_even}'
        f'\nКоличество нечетных чисел: {len_odd}'
    )


len_even, len_odd = 0, 0


def count_recur(zero, num=None):
    print(zero, end=' ')
    global len_even
    global len_odd

    len_even += 1 if zero % 2 == 0 else 0
    len_odd += 1 if zero % 2 != 0 else 0

    if zero == num:
        print(
            f'\nКоличество четных чисел: {len_even}'
            f'\nКоличество нечетных чисел: {len_odd}'
        )
        return
    else:
        count_recur(zero + 1, num=num)


count_while(10)  # using the while loop
print('')
count_recur(zero=0, num=10)  # using recursion

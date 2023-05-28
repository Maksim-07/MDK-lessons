'''
Создайте функцию countdown, которая принимает список рандомных чисел от 0 до 10, а возвращает каждый элемент этого
списка в порядке обратного отсчета, а после 0 - слово " Пуск!".
'''

from random import sample


def countdown(rand_list):
    rand_list = sorted(rand_list, reverse=True)
    for m in rand_list:
        print(m, end=' ')
    print('Пуск!')


lst = sample(range(0, 10), 10)
countdown(rand_list=lst)

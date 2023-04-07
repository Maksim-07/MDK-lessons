'''
Напишите функцию-генератор, которая выдает буквы английского алфавита от a до z. Опустошите генератор любым способом
'''

letters = 'abcdefghijklmnopqrstuvwxyz'


def func():
    for m in letters:
        yield m


y = func()
for letter in range(len(letters)):
    print(next(y))

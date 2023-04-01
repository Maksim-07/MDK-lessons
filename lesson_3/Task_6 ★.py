'''
Создать функцию alphabet, которая:
а) выводит буквы английского алфавита и их порядковый номер.
б) выводит словарь {порядковый номер : буква }
'''

import string

alph = string.ascii_uppercase
dict_alph = {}


def alphabet():
    for num, b in enumerate(alph, 1):
        dict_alph[num] = b
        print(f"{b} - {num}")
    return dict_alph


print(alphabet())

'''
Создайте функцию cesar, которая возвращает зашифрованную строку шифром Цезаря со сдвигом на 3.
Саму строку запросите у пользователя.
'''


def cesar(string):
    str = ''
    for m in string:
        if m.isalpha():
            num = ord(m)
            str += chr(num + 3)
        else:
            str += m
    return str


str = 'Привет, мир!'
print(cesar(string=str))

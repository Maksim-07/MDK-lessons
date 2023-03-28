'''
Пусть дан список имен пользователлей s. Создайте функцию, которая: а) Преобразует имена так, чтобы имена начинались с
заглавной буквы. б) Удаляет недопустимые символы (пробелы, цифры и спецсимволы)

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
'''


def correct(words):
    result = ''
    for word in words:
        name = [val for val in word if val.isalpha()]
        result += "".join(name).capitalize() + ' '
    return result


s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
print(correct(words=s))

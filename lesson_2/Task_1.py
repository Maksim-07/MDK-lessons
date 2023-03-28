'''
Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел по возрастанию и возвращает его.
Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
'''


def tpl_sort(tpl):
    for m in tpl:
        if type(m) == int:
            continue
        else:
            return tpl
    return sorted(tpl)


tpl = (1, 3, 54, 23, 532, 6, 'd')
print(tpl_sort(tpl=tpl))

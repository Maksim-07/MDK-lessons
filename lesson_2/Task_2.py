'''
Функция slicer() на вход принимает кортеж и случайный элемент. Требуется вернуть новый кортеж, начинающийся с первого
появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой
кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
'''


def slicer(tpl, random_element):
    if tpl.count(random_element) == 1:
        return tpl[tpl.index(random_element):]
    elif tpl.count(random_element) > 1:
        first_ind = tpl.index(random_element)
        second_ind = tpl.index(random_element, first_ind + 1)
        return tpl[first_ind:second_ind + 1]
    else:
        return tuple()


tpl = (1, 3, 54, 23, 532, 3, 6, 'd')
print(slicer(tpl=tpl, random_element=3))

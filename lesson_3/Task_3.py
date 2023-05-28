'''
Создайте функцию honest, которая принимает произвольный список, а возвращает список, состоящий только из четных
элементов. Список от 0 до 20 создайте любым способом.
'''


def honest(lst):
    return [m for m in lst if m % 2 == 0]


lst = [num for num in range(20)]
print(honest(lst=lst))

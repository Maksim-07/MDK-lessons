'''
Создайте словарь, в котором ключом будет являться число от 1 до 23, а значением - буквы английского алфавита.
Решите эту задачу с помощью генератора словаря
'''

letters = 'abcdefghijklmnopqrstuvwxyz'
letters_correct = letters[:23]

dict = {key: value for key, value in enumerate(letters_correct, 1)}
print(dict)

'''
Пусть дана функция, которая спрашивает имя пользователя.
Создайте декоратор hello, который дополнительно будет выводить приветствие: "Привет, <имя>!"
'''


def decorator(func_to_decorate):
    def wrapper():
        print(f"Привет, {func_to_decorate}!")
    return wrapper


def get_name():
    name = input('Введите имя: ')
    return name


my_function_decorated = decorator(get_name())
my_function_decorated()

'''
Создайте функцию calculate, которая принимает у пользователя два числа и операцию, а выдает результат операции.
Обязательно: воспользуйтесь функциями exec или eval
'''


def calculate(exp):
    lst = exp.split()
    print(eval(f"{lst[0]}{lst[1]}{lst[2]}"))
    exec(f"print({lst[0]}{lst[1]}{lst[2]})")


exp = input('Введите выражение через пробел: ')
calculate(exp=exp)

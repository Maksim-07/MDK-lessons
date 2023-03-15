'''
Создайте функцию calculator, которая принимает у пользователя два числа и операцию(+, -, /, *), а возвращает результат.
Предусмотрите предупреждение об ошибке при делении на 0.
'''


def calculator(num_1, num_2, operation):
    match operation:
        case '+':
            return num_1 + num_2
        case '-':
            return num_1 - num_2
        case '/':
            try:
                return num_1 / num_2
            except ZeroDivisionError:
                return 'Нельзя делить на 0!'
        case '*':
            return num_1 * num_2


n_1 = int(input('Введите первое число: '))
operation = input('Введите операцию (+, -, /, *): ')
n_2 = int(input('Введите второе число: '))

print(calculator(num_1=n_1, num_2=n_2, operation=operation))

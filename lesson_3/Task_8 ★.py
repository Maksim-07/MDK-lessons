'''
Предположим, что объявлена функция, которая подставляет в шаблон значения переменной field:

def render_input(field):
  return f'<input id="id_{field}" name="{field}">'
username = render_input('username')
print(username)

Создайте декоратор, который обернет строку в теги
<p> ... </p>
'''


def decorator(func):
    def wrapper():
        print(f"</p>{func}</p>")

    return wrapper


def render_input(field):
    return f'<input id="id_{field}" name="{field}">'


username = render_input('username')
# print(username)
my_function_decorated = decorator(username)
my_function_decorated()

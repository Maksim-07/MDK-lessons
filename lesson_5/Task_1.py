'''
Создайте класс cat и добавьте 3 атрибута (имя, окрас, возраст) и 3 метода класса (мяукнуть, мурлыкать и еще один на ваше усмотрение).
Создайте 1 экземпляр класса и продемонстрируйте его атрибуты и методы.
'''


class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print("Мр-р-ряу!")

    def purr(self):
        print("Мур-р-р-р...")

    def sleep(self):
        print(f"{self.name} спит 💤")


lulu = Cat(name='Lulu', color='Chocolate', age=8)
lulu.meow()
lulu.purr()
lulu.sleep()
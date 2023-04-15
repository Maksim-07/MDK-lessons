'''
Создайте класс светофор (trafficlight). Реализуйте в нем метод, который будет переключать цвета (red, green, yellow)
по определенному времени: red = 1 сек, green 2 сек, yellow = 0.5 сек.
'''
from time import sleep


class Trafficlight:
    red_wait = 1
    yellow_wait = 0.5
    green_wait = 2

    def signal(self):
        sleep(self.red_wait)
        print('Red')

        sleep(self.yellow_wait)
        print('Yellow')

        sleep(self.green_wait)
        print('Green')

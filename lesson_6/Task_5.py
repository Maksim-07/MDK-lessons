''' Создайте класс Clock со статичным методом Say_time, который будет выводить на экран текущее время. '''

from time import time, localtime


class Clock:

    @staticmethod
    def say_time():
        current_time = localtime(time())
        print(f'{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}')


Clock.say_time()

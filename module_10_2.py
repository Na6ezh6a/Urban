# Задача "За честь и отвагу!".
import threading
from time import sleep, time
class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0
    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            sleep(1)
            self.days += 1
            self.enemies = max(self.enemies - self.power, 0)
            print(f'{self.name} сражается {self.days}..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
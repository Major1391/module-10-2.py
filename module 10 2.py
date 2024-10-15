from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemies = 100
        day = 0
        while enemies > 0:
            sleep(1)
            day += 1
            enemies -= self.power
            print(f'{self.kname} сражается {day} сутки, осталось {enemies} воинов.')
            if enemies < 0:
                enemies = 0
        print(f"{self.kname} одержал победу спустя {day} дней(дня)!")


def main():
    knight1 = Knight('Sir Lancelot', 10)
    knight2 = Knight("Sir Galahad", 20)
    knight1.start()
    knight2.start()
    knight1.join()
    knight2.join()
    print('Битвы окончены.')


if __name__ == '__main__':
    main()

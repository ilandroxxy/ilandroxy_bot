# region Домашка: ************************************************************



# endregion Домашка: ************************************************************


# region Урок: ************************************************************

'''
class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'black'

    def __init__(self, b, ms):  # декоратор
        self.brand = b
        self.max_speed = ms

    def upgrade(self):
        self.max_speed += 25


class Truck(Car):
    kol_pr = 2
    max_mass = 20

    def AddGruz(self, k, mas):
        self.kol_pr = k
        self.max_mass = mas

obj = Truck('Nissan', 120)
obj.AddGruz(10, 20)

print(obj.brand)
print(obj.max_speed)
print(obj.color)
print(obj.kol_pr)
print(obj.max_mass)
'''


'''
class apple(object):
    type_device = ''
    color = ''
    model = ''
    service_life = 0

    def __init__(self, dev, col, mod, lif):
        self.type_device = dev
        self.color = col
        self.model = mod
        self.service_life = lif

    def upgrade(self, dev, col, mod, lif):
        self.type_device = dev
        self.color = col
        self.model = mod
        self.service_life = lif

class iphone(apple):
    size = 0
    storage = 0
    processor = ''
    price = 0

    def descriptions_iphone(self, siz, stor, proc, pri):
        self.size = siz
        self.storage = stor
        self.processor = proc
        self.price = pri

    def HowDoshiksInIphone(self, n):
        doshik = int(input('Введите цену доширака: '))
        print(n / doshik)


class macbook(apple):
    pass

class airpods(apple):
    pass

iphone_Sasha = apple('phone', 'white', '8+', 1)
print(iphone_Sasha.color)

iphone_Sasha.upgrade('Phone', 'SilverEdition', '8plus', 2)
print(iphone_Sasha.color)

iphone_Ilya = iphone('Phone', 'green', '13 Pro Max', 1)
iphone_Ilya.descriptions_iphone(6.8, 128, 'A15 Bionic', 90000)
print(iphone_Ilya.storage)

iphone_Ilya.HowDoshiksInIphone(iphone_Ilya.price)
'''



# endregion Урок: ************************************************************



# todo: на следующем уроке: Оформляем портфолио для первого нашего бота, отвечаем на вопросы по курсы или решаем задачки

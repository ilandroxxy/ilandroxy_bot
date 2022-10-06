# Типы данных

# x = 4  # переменнаая - это способ доступа к данным (4) по имени (x)


# Типы данных переменных
'''
a = 4  # int (integer) - целочисленные значения
print(type(a))
print(a * 5, type(a * 5))

b = 4.0  # float (число с плавающей точкой) - любые дроби
print(7 / 2, type(7 / 2))

c = '4'  # str (string) - строковый тип данных, хранит в себе буквы, символы, цифры, слова ...
print(c, c * 5, type(c))  # строковая цифра не равно число
# Примечание 1: не важно какие кавычик использовать, можно и двойные

s1 = 'hello '
s2 = 'Aleksandr'
print(s1 + s2)  # конкатенация строк - склеивание



d1 = True  # bool  (boolean) - Булева алгебра или математическая логика
d2 = False
print(4 < 10)  # используются для вывода логических операций

h1 = 'hello '  # пробел тоже символ! эти строки не равны
h2 = 'hello'
print(h1 == h2)


M = [2, 2.0, '2', True, 2+3, 7/2, '4' * 5, 4 == 10]
for x in M:
    print(x, type(x))
'''


# Типы данных коллекций
'''

M = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "один", 2: "два", 3: "три"}]
for x in M:
    print(x, type(x))
'''

# Конвертации типов данных
'''
x = 5
print(x, type(x))

x = str(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = int(x)
print(x, type(x))
# Из int и float можно спокойно переводить в другие типы данных
# А из str можно переводить, только если строка состоит из одних лишь цифр

M = [1, 2, 3]
print(M, type(M))

M = tuple(M)
print(M, type(M))

M = set(M)
print(M, type(M))

M = list(M)
print(M, type(M))
'''



# Ввод данных с клавиатуры
'''
import random

# print('Hello', input('Введите имя: '))  # функция input() - это ввод строки с клавиатуры

a = random.randint(1, 100)
b = random.randint(1, 100)

print(f'Решите пример: {a} + {b} = ')
x = int(input())

if x == a + b:
    print('Правильно')
else:
    print('Неправильно ')
    
# x = float(input()) - для float значений с клавиатуры
'''



# Вывод функции print() в консоль
'''

weather = 'облачно'
temperature = 24
# Привет, сегодня облачно, а температура 24
print('Привет, сегодня', weather, ", а температура", temperature)
print('Привет, сегодня ' + weather + ", а температура " + str(temperature))
print("Привет, сегодня {}, а температура {}".format(weather, temperature))
print("Привет, сегодня %s, а температура %d"%(weather, temperature)) # %s - ввод строки, %d - ввод int, %f - ввод float
print(f"Привет, сегодня {weather}, а температура {temperature}")
'''


# Базовая арифметика
'''
a = 7
b = 2

print(f'{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}')
print()
print(f'Возведите число {a} в степень {b}: {a} ** {b} = {a**b}')
print(f'Квадратный корень числа 16 = {16 ** (1/2)}')
print(f'Кубический корень числа 27 = {27 ** (1/3)}')
print()
print(f'Обычное вещественное деление: {a} / {b} = {a/b}\n'
      f'Целочисленное деление (без округлений): {a} // {b} = {a//b}\n'
      f'Остаток от деления (в виде обыкновенной дроби): {a} % {b} = {a%b}')
'''


# Библиотека math в Python


import math
print(math.pow(4, 2))

x = math.gcd(24, 12)
print(x)

f = math.factorial(5)
print(f)

'''
import math as m
print(m.pow(4, 2))
'''

'''
from math import pow, sqrt
print(pow(4, 2))
print(sqrt(16))
'''

'''
from math import *
print(pow(4, 2))
'''
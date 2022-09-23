
# Типа данных переменных
'''
x = 5  # переменная - это способ взаимодействовать с данными по имени (искать)

a = 4  # int (integer) - целочисленные

b = 4.0  # float (число с плавающей точкой) - дроби

c = '4'  # str (string) строка или строчный тип данных: символы, буквы, цифры, слова, ...
s1 = 'Slava'
s2 = 'Slava '
print(s1 == s2)  # False - пробел тоже символ
print(s2 + s1)  # конкатинация строк (склеивание)


d1 = True  # bool (boolean) - логический тип данных, от Булева Алгебра (Математическая логика)
d2 = False
print(1 < 10)  # True
'''

# Типа данных коллекций
'''
M = [1, 2.0, '3', True, 3+4, 7/2, '3'*5, 1 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for i in M:
    print(i, '  <---->   ', type(i))
'''


# Перевод в разные типы данных
'''
x = 4
print(x, type(x))

x = str(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = int(x)
print(x, type(x))

# Из int и float легко переводить в другие типы данных
# Из str можно переводить, только если в строке одни лишь цифры
print()

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
s = input('s: ')
print(s * 4)
print()

x = int(input('x: '))
print(x * 4)
print()

M = [int(i) for i in input('Введите числа через пробел: ').split()]
print(M)
'''




# Консольные выводы
'''
weather = 'облачно'
temperature = 24
# Привет, сегодня облачно, но жарко, температура 24
print('Привет, сегодня', weather, ', но жарко, температура', temperature)
print('Привет, сегодня ' + weather + ', но жарко, температура ' + str(temperature))
print('Привет, сегодня {}, но жарко, температура {}'.format(weather, temperature))
print(f'Привет, сегодня {weather}, но жарко, температура {temperature}') # f-строки
print()


import random
type = '26'
s = 'https://inf-ege.sdamgia.ru/problem?id='
x = random.randint(0, 33)
M = [46984, 28132, 33528, 40742, 28141, 39255, 33771, 27884, 38960, 27888, 28140, 27886, 35915, 36881, 27423, 29674,
    36000, 35484, 36039, 28139, 27883, 41001, 47023, 27881, 27882, 33198, 27887, 27880, 33105, 28138, 33496, 37161, 45260, 27885]
print(f"Кол-во заданий ({type}): {len(M)}")
task = M[x]
link = f'Задача {task} ({type}):\n{s}{task}'
print(link)
'''


# Базовую арифметику
'''
a = 7
b = 2
print(f'a + b = {a + b}\na - b = {a - b}\na * b = {a * b}')
print()
print(f'Вовзведение a в степень b: a ** b = {a ** b}')
print(f'Квадратынй корень числа 16 = {16 ** (1/2)}')
print(f'Кубический корень числа 27 = {27 ** (1/3)}')
print()
print(f'a = {a}, b = {b}\nВещественное деление: a / b = {a / b}\n'
      f'Целая часть (без округления): a // b = {a // b}\n'
      f'Остаток от деления (взятый от обыкновенное дроби): a % b = {a % b}')
print()
'''

# import math # просто подключили библиотеку math
# x = math.pow(4, 2)

# from math import pow, factorial  # импортировали только два метода из библиотеки math
# x = pow(4, 2)

# from math import *  # импортировали все методы из библиотеки math
# x = pow(4, 2)

import math as m  # сократили имя вызова библиотеки
x = m.pow(4, 2)

print(x)

print(m.sqrt(16))
print(m.gcd(12, 24))
print(m.lcm(12, 24))
print(m.factorial(5))




# Задача №1
'''
x = int(input('x: '))
summ = 0
x1 = x // 100
x2 = (x // 10) % 10
x3 = x % 10
summ = x1 + x2 + x3
print(f'x1 = {x1}\nx2 = {x2}\nx3 = {x3}\nsumm = {summ}')
'''

# Задача №2
'''
x = int(input('x: '))
summ = 0
while x > 0:
    # print(x)
    summ += x % 10
    x //= 10  # x = x // 10
print(f'summ = {summ}')
'''

# Задача №3
'''
M = [int(i) for i in input('x: ')]
print(M)
print(sum(M))
'''
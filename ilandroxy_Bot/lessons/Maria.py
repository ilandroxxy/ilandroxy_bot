# Типы данных
'''
x = 5  # переменная нужна для доступа к данным (5) по имени (x)

a = 4  # int (integer) - целочисленные данные
b = 4.0  # float (число с плавающей точкой)
c = '4'  # str (string)
d1 = True  # bool (boolean)
d2 = False

M = [1, 2.0, '3', True, 3+4, 7/2, '3'*4, 1 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for i in M:
    print(i, '  <---->  ', type(i))
'''


# Можно менять типы данных
'''
x = '4'
print(x * 4)

x = int(x)
print(x * 4)

x = float(x)
print(x * 4)

x = str(x)
print(f'x = {x},  x * 4 = {x * 4}')

# Из int и float переводим свободно в любой тип данных
# Из str мы можем переводить в другие, только цифры: ValueError: invalid literal for int() with base 10: '4igj'
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

# Ввод с клавиатуры
'''
x = input('x: ')
print(x * 3)  # input() - принимает только str()

y = int(input('y: '))
print(y * 3)

M = [int(i) for i in input("Введите числа через пробел: ").split()]
print(M)
'''


# Консольный вывод
'''
weather = 'облачно'
temperature = 24
# Привет, сегодня облачно и температура 24
print('Привет, сегодня', weather, 'и температура', temperature)
print('Привет, сегодня ' + weather + ' и температура ' + str(temperature))
print('Привет, сегодня {} и температура {}'.format(weather, temperature))
print(f'Привет, сегодня {weather} и температура {temperature}')  # f-строки

import random
type = '27'
s = 'https://inf-ege.sdamgia.ru/problem?id='
x = random.randint(0, 30)
M = [28133, 33529, 35485, 27424, 33497, 28131, 27891, 27991, 37162, 47024, 46985, 35916, 33106, 38961, 27889, 38604,
     36001, 39256, 28130, 40743, 27990, 41002, 36882, 28129, 29675, 27890, 27989, 33772, 36040, 45261, 33199]
print(f"Кол-во заданий ({type}): ", len(M))
link = f'Задача {M[x]} ({type}):\n{s}{M[x]}'
print(link)
'''


# Базовая арифметика
'''
a = 7
b = 2

print(f'a + b = {a + b}\na - b = {a - b}\na * b = {a * b}')
print()
print(f'Возведение в степень a ** b = {a ** b}')
print(f'Квадратный корень от 16 = {16 ** (1/2)}')
print(f'Кубический корень от 27 = {27 ** (1/3)}')
print()
print(f'Вещественное деление: a / b = {a / b}\n'
      f'Целочисленное деление (без округлений): a // b = {a // b}\n'
      f'Остаток от делений (но в обыкновенной дроби): a % b = {a % b}')
'''

# Задача №1
'''
x = 456
summ = 0
x1 = x // 100
x2 = (x // 10) % 10
x3 = x % 10
summ = x1 + x2 + x3
print(f'x1 = {x1}\nx2 = {x2}\nx3 = {x3}\nsumm = {summ}')
'''

# Задача №2
'''
x = int(input())  # x = 12345
#x = 12345
summ = 0
while x > 0:
    print(x)
    summ += x % 10 # summ = summ + (x % 10)
    x //= 10
print(x)
print(f'summ = {summ}')
'''

# Задача №3
M = [int(i) for i in input()]
print(M)
print(sum(M), max(M), min(M), len(M))




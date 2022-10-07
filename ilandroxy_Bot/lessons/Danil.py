# НА следующем уроке написать примитивн7ый калькулятор

# Типы данных

# Однострочный комментарий - эта строка не видна компьютеру, нужна для пояснений кода напарникам (пользователям)

'''
Многострочный комментарий
'''


X = 5  # переменная - это способ доступа к данным (5) через имя (X) переменной

# Типы данных переменных
'''
a = 4  # int (integer) - целочисленные значения
print(7 / 2, type(7 / 2))

b = 4.0  # float (число с плавающей точкой) - любые дроби
print(a + b, type(a + b))

c = '4'  # str (string) - строковый тип данных, хранит в себе слова, символы, цифры, буквы ...
print(c * 5)

s1 = 'Hello'
s2 = ' Danil'
print(s1 + s2)  # конкотинация - слияние строк

c1 = 'hello'
c2 = 'hello '  # пробел - тоже символ строк, поэтому строки неравны
print(c1 == c2)  # это логическая операция сравнения двух переменных (неравно)

d1 = True  # bool (boolean) - Булева алгебра логики (математическая логика)
d2 = False
print(4 < 10)
'''


# Коллекция это набор значений
# Типы данных коллекций
"""

A = [1, 2, 3]  # list (список / массив)
A[1] = '*'  # отличительная черта списков - в них можно не только хранить, но и менять значение элементов
print(A)


B = (1, 2, 3)  # tuple (кортеж) - только хранит элементы


C = {1, 2, 3}  # set (множество) - неупорядоченный, не содержит повторяющихся элементов

# Тип 14 № 39243
'''
# Значение выражения 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?

x = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M, M.count(0))

M = set(M)
print(M, len(M))
'''

D = {1: 'один', 2: "два"}  # dict (словарь) - элемент словаря имеет ключи и значение, доступ к значению осуществляется через ключ, ключи повторяться не могут
print(D)


M = [1, 2.5, '3', True, 3+4, 7/2, '3'*7, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "один", 2: "два", 3: "три"}]
for i in M:
    print(i, "  <---->  ", type(i))
"""

# Конвертация типов данных
'''
x = 5
print(x, "  <---->  ", type(x))

x = str(x)
print(x, "  <---->  ", type(x))

x = float(x)
print(x, "  <---->  ", type(x))

x = int(x)
print(x, "  <---->  ", type(x))

print()  # пустая строка
# Из int и float удобно переводить в другие типы данных
# ИЗ str можно переводить, если переменная состоит только лишь из цифр

M = [1, 2, 3]
print(M, "  <---->  ", type(M))

M = tuple(M)
print(M, "  <---->  ", type(M))

M = set(M)
print(M, "  <---->  ", type(M))

M = list(M)
print(M, "  <---->  ", type(M))
'''


# Ввод переменных с клавиатуры
'''
name = input('Name: ')  # функция input() получает строку с клавиатуры
print('Hello, ' + name)

x = int(input('x: '))
print(x * 5)

# x = float(input('x: '))
# print(x * 5)


#M = [int(i) for i in input().split()]
#print(M)
'''

# Визуальное оформление вывода функции print() в консоль
'''
weather = 'облачно'
temperature = 24
print('Привет, сегодня', weather, ', а температура ', temperature)
print('Привет, сегодня ' + weather + ', а температура ' + str(temperature))
print('Привет, сегодня {}, а температура {}'.format(weather, temperature))
print('Привет, сегодня %s, а температура %d'%(weather, temperature))  # %s - строка, %d - int, %f - float
print(f'Привет, сегодня {weather}, а температура {temperature}')  # f-строка

print(f'Hello, {input("Введите имя: ")}!')

name = input('Name: ')  # функция input() получает строку с клавиатуры
print('Hello, ' + name + '!')
'''



# Базова арифметика
a = 7
b = 2

print(f'{a} + {b} = {a+b}\n'
      f'{a} - {b} = {a-b}\n'
      f'{a} * {b} = {a*b}\n')

print(f'Возведите число {a} в степень {b}:'
      f'\n{a} ** {b} = {a**b}\n')

print(f'Квадратный корень от 16 = {16 ** (1/2)}')
print(f'Кубический корень от 27 = {27 ** (1/3)}\n')

print(f'Вещественное деление: {a} / {b} = {a/b}\n'
      f'Целочисленное деление (без округлений): {a} // {b} = {a//b}\n'
      f'Остаток от деления (в виде обыкновенной дроби): {a} % {b} = {a%b}\n')


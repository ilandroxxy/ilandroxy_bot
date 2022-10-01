# Однострочный комментарий

"""
Многострочный
комментарий
"""


# Типы данных
x = 4  # переменная - предоставляет доступ к данным (4) по имени (x)


# Типы данных переменных
'''
a = 4  # int (integer) - целочисленный тип данных
print(type(a))

b = 4.0  # float (число с плавающей точкой) - по факту дроби
print(7/2, type(7/2))

c = '4'  # str (string) - строковый тип данных, хранит: символы, цифры, буквы, слова ...

h1 = 'Hello'
h2 = 'Tanya'
print(h1 + ' ' + h2)


d1 = True  # bool (boolean) - Булева алгебра или основы математической логики
d2 = False
print(4 > 10)


M = [a, b, c, d1, d2, 3+4, 7/2, '4' * 8, 4 < 10]
for i in M:
    print(i, '  <--->  ', type(i))
'''



# Типы данных коллекций
'''
print()
A = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for i in A:
    print(i, '  <--->  ', type(i))
'''

# Можно ли менять типа данных? Да, можно
# Из int и float можно легко переводить в другие типы данных
# Из str можно переводить в int и float, если строка состоит только лишь из цифр
'''
temp = 5
print(temp, '  <---->  ', type(temp))

temp = str(temp)
print(temp, '  <---->  ', type(temp))

temp = float(temp)
print(temp, '  <---->  ', type(temp))

temp = int(temp)
print(temp, '  <---->  ', type(temp))

print()
A = [1, 2, 3]
print(A, '  <---->  ', type(A))

A = tuple(A)
print(A, '  <---->  ', type(A))

A = set(A)
print(A, '  <---->  ', type(A))

A = list(A)
print(A, '  <---->  ', type(A))
'''

# Ввод с клавиатуры
'''
name = input('Введите переменную name: ')  # просто input() - получает строку с клавиатуры
print('Hello, ' + name + '!')

x = int(input('x: '))
print(x, '  <---->  ', type(x))

y = float(input('y: '))
print(y, '  <---->  ', type(y))
'''


'''
text = input()
symbol = '!,.?-+=:*&^%$##$@'

M = [i for i in text]
print('M: ', M)
A = []
for i in range(0, len(M)):
    if M[i] not in symbol:
        A.append(M[i])
print('А: ', A)
res = ''.join(A)
print('res: ', res)
result = [i for i in res.split()]
print('result: ', result)
'''


# Вывод в консоль результатов
'''
# Сегодня облачно, хочу погулять, потому что температура 24
weather = 'облачно'
temperature = 24

print('Сегодня ', weather, ', хочу погулять, потому что температура', temperature)
print('Сегодня ' + weather + ', хочу погулять, потому что температура ' + str(temperature))
print('Сегодня {}, хочу погулять, потому что температура {}'.format(weather, temperature))
print('Сегодня %s, хочу погулять, потому что температура %d'%(weather, temperature))  # для float -> %f
print(f'Сегодня {weather}, хочу погулять, потому что температура {temperature}')  # f-строка
print(f'Сегодня {weather}, хочу погулять, '
      f'потому что температура {temperature}')  # f-строка
print(f'Сегодня {weather}, хочу погулять, '
      'потому что температура {temperature}')  # f-строка
'''



# Базова арифметика
a = 7
b = 2

print(f'{a} + {b} = {a + b}\n{a} - {b} = {a - b}\n{a} * {b} = {a * b}')
print()
print(f'Возведение {a} в степень {b}: {a ** b}')
print(f'Корень квадратный от 16: {16 ** (1/2)}')
print(f'Корень кубический от 27: {27 ** (1/3)}')
print('\n')
print(f'Вещественное деление: {a} / {b} = {a / b}\n'
      f'Целая часть от деления (без округления): {a} // {b} = {a // b}\n'
      f'Остаток от деления (от обыкновенной дроби): {a} % {b} = {a % b}')


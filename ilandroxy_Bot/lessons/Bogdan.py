# region Домашка:  ******************************************************************************



# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************

# Условные операторы - ветвление

'''
x = int(input('x: '))

if x > 0:  # if - если
    print(x)
elif x < 0:  # elif - иначе если
    print(-x)
else:     # else - иначе
    print(0)
'''

'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print('Точка лежит на оси')
'''

# Каскадные условия
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print(1)
    else:    # x > 0 and y <= 0
        print(4)
else:
    if y > 0:  # x <= 0 and y > 0:
        print(2)
    else:    # x <= 0 and y <= 0
        print(3)
'''

# Мини калькулятор
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} {s} {b} = {a+b}')
elif s == '-':
    print(f'{a} {s} {b} = {a-b}')
elif s == '*':
    print(f'{a} {s} {b} = {a*b}')
elif s == '/' and b == 0:
    print(f'На ноль делить нельзя')
elif s == '/':
    print(f'{a} {s} {b} = {a/b}')
'''

# ZeroDivisionError: division by zero
# Обработчик исключений
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

try:
    if s == '/':
        print(f'{a} {s} {b} = {a/b}')

except ZeroDivisionError:
    print('На ноль делить нельзя')
'''


# Циклы - повторение каких-либо действий несколько раз

# for - цикл повтори n раз, пробеги строку, пробеги строку через индексы и тд
'''
n = 10
for i in range(n):  # [0, n)     range(START = 0, STOP = x, STEP = 1)
    print(i, end=' ')
print()

for i in range(2, n):  # [2, n)     range(START = y, STOP = x, STEP = 1)
    print(i, end=' ')
print()

for i in range(2, n, 2):  # [2, n)     range(START = y, STOP = x, STEP = z)
    print(i, end=' ')
print()

for i in range(n-1, 0-1, -1):  # в случае, если нужно рассмотреть убывающую последовательность
    print(i, end=' ')
print()

s = '765432'
# i  012345
M = [7, 6, 5, 4, 3, 2]
# i  0  1  2  3  4  5

for x in M:
    print(x, end=' ')
print()

# len() - функция возвращающая длину списка (коллекции) - то есть кол-во элементов в нем
for i in range(0, len(M)):  # [0, 6)
    print(M[i], end=' ')
print()

print(M)
for i in range(0, len(M)):  # [0, 6)
    M[i] = M[i] ** 2
print(M)
'''




# while - циклы с условием (выполняется пока условие истинно)
'''
for i in range(2, 10+1, 2):  # [2, n)     range(START = y, STOP = x, STEP = z)
    print(i, end=' ')
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''

'''
summ = 0
x = 123459304830925209385

s = str(x)
M = [int(i) for i in s]
print(sum(M))


while x > 0:
    summ += (x % 10)
    x //= 10
    print(x, summ)
print(summ)
'''

'''
k = 0
while True:
    print(k)
    k += 1
'''

'''
import random

k = 0
password = 'qwerty'
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный, попробуйте снова.')
    k += 1
    if k == 3:
        symbol = '+-*'
        a = random.randint(1, 10)
        s = random.choice(symbol)
        b = random.randint(1, 10)
        print(f'Пройдите проверку на робота!\nРешив пример: {a} {s} {b} = ')
        x = int(input())

        if s == '+':
            if x == a + b:
                print('Проверка пройдена.')
                k = 0
                continue
            else:
                print('Banned')
                break
        if s == '-':
            if x == a - b:
                print('Проверка пройдена.')
                k = 0
                continue
            else:
                print('Banned')
                break
        if s == '*':
            if x == a * b:
                print('Проверка пройдена.')
                k = 0
                continue
            else:
                print('Banned')
                break
'''


# endregion Урок:  ******************************************************************************


# todo: Богдан = [], на следующем уроке: Подробнее остановиться на комментариях, break и continue и технологии flag, решаем 2 номер

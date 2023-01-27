# region Домашка: ******************************************************************************
'''
one = int(input())
two = int(input())
three = int(input())

xd = int(two-one)
xz = int(three-two)

if xd == xz:
    print("YES")
else:
    print("NO")
'''

'''
one = int(input())
two = int(input())
three = int(input())

xd = int(two-one)
xz = int(three-two)
d = xd == xz

if d:
    print("YES")
else:
    print("NO")
'''

# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************


# Зачем нужен elif пример
'''
x = 4
y = 5

if x > 0 and y > 0:
    print(1)
if x < 0 and y < 0:
    print(3)
if x < 0 and y > 0:
    print(2)
if x > 0 and y < 0:
    print(4)
else:
    print('Точка лежит на оси')
'''


# Циклы - повторение каких-то действий

# Циклы for: если нужно повторить действие n раз, пробежать элементы коллекции, пробежать элементы коллекции по индексам
'''
for _ in range(5):  # просто повтори 5 раз
    print('Привет')

print(4, 5, 6, sep='*')

for i in range(10):  # [0, 10)   range(START=0, STOP-1, STEP=1)
    print(i, end=' ')
print()

for i in range(2, 10):   # [2, 10)   range(START, STOP-1, STEP=1)
    print(i, end=' ')
print()

for i in range(2, 10, 3):  # range(START, STOP-1, STEP)
    print(i, end=' ')
print()

for i in range(10, 0, -1):  # чтобы пробегать убывающие последовательности
    print(i, end=' ')
print()

# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]
s = '12345'

print(len(M), len(s))

for i in range(0, len(M)):  # [0, 5)
    print(M[i], end=' ')
print()

for i in range(0, len(s)):  # [0, 5)
    print(s[i], end=' ')
print()

for x in M:
    print(x, end=' ')
print()

for x in s:
    print(x, end=' ')
print()

for i in range(0, len(M)):  # [0, 5)
    M[i] = M[i] ** 2
print(M)
'''

# Цикл while - цикл с условием, то есть действие выполняется, пока условие истинно: бесконечный цикл
'''
for i in range(2, 20+1, 3):  # range(START, STOP-1, STEP)
    print(i, end=' ')
print()

i = 2
while i <= 20:
    print(i, end=' ')
    i += 3
print()
'''

# Перевод в n-ную систему счисления
'''
x = int(input('x: '))
n = int(input("n: "))
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(*M)
'''

# Бесконечные циклы
'''
import random
import time
username = 'cadet7771'
password = 'qwerty'
count = 0
while True:
    pas = input(f'Введите пароль от учетной записи "{username}": ')
    if pas == password:
        print(f'Добро пожаловать, {username}!')
        break
    else:
        print('Пароль неверный, попробуйте снова.')
        count += 1
        if count == 3:
            sign = ('+', '-')
            a = random.randint(1, 100)
            s = random.choice(sign)
            b = random.randint(1, 100)
            x = int(input(f'Пройдите проверку на робота, решив пример: {a} {s} {b} = '))
            if s == '+':
                if x == a + b:
                    print('Проверка пройдена успешно')
                    count = 0
                else:
                    print('Проверка не пройдена, попробуйте позже')
                    time.sleep(10)
                    count -= 1
            if s == '-':
                if x == a - b:
                    print('Проверка пройдена успешно')
                    count = 0
                else:
                    print('Проверка не пройдена, попробуйте позже')
                    time.sleep(10)
                    count -= 1
'''
# endregion Урок: ******************************************************************************


# todo: Артем = []
# на прошлом уроке: Разобрали теорию циклов и затронули условные операторы.
# на следующем уроке: Разбираем 2 номер, говорим про списки, коллекции, строки, Разбираем 14 номер.

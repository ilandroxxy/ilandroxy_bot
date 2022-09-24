

# Условные операторы (ветвление)
# Ключевые слова: if, elif, else, каскадные условия, логические связки and, or, >, <, <=, ==, != ...

'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # если
    print('1 half')
elif x < 0 and y < 0:  # иначе если
    print('3 half')
elif x < 0 and y > 0:
    print('2 half')
elif x > 0 and y < 0:
    print('4 half')
else:  # иначе
    print('Точка лежит на осях')
'''
print()

# функция модуля числа
'''
number = int(input('number: '))


if number > 0:
    print(number)
elif number < 0:
    print(-number)
else:
    print('Равен нулю')
'''


# Каскадные условия
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print('1 half')
    elif y == 0:  # x > 0, y == 0
        print('Лежит на оси')
    else:  # x > 0, y < 0
        print('4 half')
elif x == 0:
    print('Лежит на осях')
else:
    if y > 0:  # x < 0, y > 0
        print('2 half')
    elif y == 0:
        print('Лежит на осях')
    else:  # x < 0, y < 0
        print('3 half')
'''


# Задача ход Ладьи
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2 and y1 == y2:
    print("Стоять на месте нельзя!")
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print("NO")
'''


# Задача ход Короля
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2 and y1 == y2:
    print("Стоять на месте нельзя!")
elif (x1+1 == x2 and y1 == y2):
    print('YES')
elif (x1-1 == x2 and y1 == y2):
    print('YES')
elif (x1 == x2 and y1+1 == y2):
    print('YES')
elif (x1 == x2 and y1-1 == y2):
    print('YES')
elif (x1+1 == x2 and y1+1 == y2):
    print('YES')
elif (x1-1 == x2 and y1-1 == y2):
    print('YES')
elif (x1-1 == x2 and y1+1 == y2):
    print('YES')
elif (x1+1 == x2 and y1-1 == y2):
    print('YES')
else:
    print("NO")
'''


'''
x = int(input('x: '))
if x > -30 and x <= -2:
    print('YES')
elif x > 7 and x <= 25:
    print("YES")
else:
    print("NO")
'''

'''
x = int(input('x: '))
if -30 < x <= -2:
    print('YES')
elif 7 < x <= 25:
    print("YES")
else:
    print("NO")
'''

'''
x = int(input('x: '))
if -30 < x <= -2 or 7 < x <= 25:
    print("YES")
else:
    print("NO")
'''

# Простейший самописный калькулятор
'''
x = int(input('x: '))
s = input('s: ')
y = int(input('y: '))

if s == '+':
    print(f'{x} {s} {y} = {x + y}')
elif s == '-':
    print(f'{x} {s} {y} = {x - y}')
elif s == '*':
    print(f'{x} {s} {y} = {x * y}')
elif s == '/' and y == 0:
    print('Делить на ноль нельзя!')
elif s == '/':
    print(f'{x} {s} {y} = {x / y}')
'''


'''
x = int(input('x: '))
s = input('s: ')
y = int(input('y: '))

try:
    if s == '/':
        print(f'{x} {s} {y} = {x / y}')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
'''
import random

type = '9'
s = 'https://inf-ege.sdamgia.ru/problem?id='
x = random.randint(0, 34)
M = [33754, 27529, 35898, 33088, 27524, 27524, 36022, 27406, 27525, 33181, 35467, 27518, 46967, 28117, 38588, 39238, 27517, 36864,
             27526, 29657, 27523, 27519, 45243, 40725, 27528, 38943, 27522, 35983, 40984, 33511, 47006, 37144, 33479,
             27520, 27527]
print(f"Кол-во заданий ({type}): {len(M)}")
task = M[x]
link = f'Задача {task} ({type}):\n{s}{task}'
print(link)
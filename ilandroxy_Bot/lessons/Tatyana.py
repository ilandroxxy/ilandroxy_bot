

'''
a=int(input())
b=1000
c=100
d=10
print(f'Цифра в позиции тысяч равна: {a//b}')
x=a//c
print(f'Цифра в позиции сотен равна: {x%d}')
y=a//d
print(f'Цифра в позиции десятков равна: {y%d}')
z=a%b
print(f'Цифра в позиции единиц равна: {z%d}')
'''

"""
a = int(input())  
# 4567
# 0123 # index - это номер элемента строки (списка) 
s = str(a)
print(f'Цифра в позиции тысяч равна: {s[0]}')
print(f'Цифра в позиции сотен равна: {s[1]}')
print(f'Цифра в позиции десятков равна: {s[2]}')
print(f'Цифра в позиции единиц равна: {s[3]}')
"""


"""
a = int(input('Введите минуты: '))
b = a // 60
c = a % 60
print(f'{a} мин - это {b} час {c} минут')
"""

# Условные операторы (ветвление)
# if - если
# elif - иначе если
# else - иначе

"""
x = int(input('x: '))
if x < 0:
    print(-x)
if x > 0:
    print(x)
else:
    print(0)
"""

'''   
if x < 0:
    print(-x)
if x > 0:
    print(x)
if x == 0:
    print(0)
'''

"""
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
    print('Лежит на оси')
"""

# Каскадные условия
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print(1)
    else:  # x > 0 and y <= 0
        print(4)
else:
    if y > 0:  # x <= 0 and y > 0
        print(2)
    else:  # x <= 0 and y <= 0
        print(3)
'''


# Логические связки и логические выражения
"""
x = True
y = False

if x == True and y == True:
    print('YES')
else:
    print('NO')

if x == True or y == True:
    print('YES')
else:
    print('NO')

if not(x == True) and not(y == True):
    print('YES')
else:
    print('NO')

# < > <= >=
# = - присваивание
# == - сравнение (равно ли)
# != - не равно ли

print(4 != 5)  # True
"""


# часы
# 1, 21 - если число оканчивается на 1, то час
# 2, 3, 4 - если число оканчивается на 2, 3, 4 - часа
# иначе - часов

'''
a = int(input('Введите минуты: '))
b = a // 60
c = a % 60

if b % 10 == 1:
    if c % 10 == 1:
        print(f'{a} мин - это {b} час {c} минута')
    elif c == 0:
        print(f'{a} мин - это {b} час')
    elif 2 <= c % 10 <= 4:
        print(f'{a} мин - это {b} час {c} минуты')
    else:
        print(f'{a} мин - это {b} час {c} минут')
elif 2 <= b % 10 <= 4:
    if c % 10 == 1:
        print(f'{a} мин - это {b} часа {c} минута')
    elif c == 0:
        print(f'{a} мин - это {b} часа')
    elif 2 <= c % 10 <= 4:
        print(f'{a} мин - это {b} часа {c} минуты')
    else:
        print(f'{a} мин - это {b} часа {c} минут')
else:
    if c % 10 == 1:
        print(f'{a} мин - это {b} часов {c} минута')
    elif c == 0:
        print(f'{a} мин - это {b} часов')
    elif 2 <= c % 10 <= 4:
        print(f'{a} мин - это {b} часов {c} минуты')
    else:
        print(f'{a} мин - это {b} часов {c} минут')
'''

'''
a = int(input('Введите минуты: '))
b = a // 60
c = a % 60

res = f'{a} мин - это '
s1 = ''
s2 = ''
if b % 10 == 1:
    s1 = f'{b} час'
elif 2 <= b % 10 <= 4:
    s1 = f'{b} часа'
else:
    s1 = f'{b} часов'

if c % 10 == 1:
    s2 = f' {c} минута'
elif c == 0:
    s2 = ''
elif 2 <= c % 10 <= 4:
    s2 = f' {c} минуты'
else:
    s2 = f' {c} минут'

print(res + s1 + s2)
'''


# Ход ладьи
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('x2: '))

if x1 == x2 and y1 == y2:
    print('Ладья должна двигаться!')
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
'''


# Самописный калькулятор
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
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

try:
    if s == '/':
        print(f'{a} {s} {b} = {a/b}')
except ZeroDivisionError:
    print(f'На ноль делить нельзя')





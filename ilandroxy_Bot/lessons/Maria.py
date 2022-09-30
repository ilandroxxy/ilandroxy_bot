# Домашка: Проговорить про оформление домашних заданий

# четырехзначное число
'''
x = int(input('x: '))
x = str(x)
print('цифра в позиции тысяч равна ', int(x[0]))
print('цифра в позиции сотен равна ' + x[1])
print('цифра в позиции десятков равна ' + x[2])
print('цифра в позиции единиц равна ' + x[3])
'''


# сумма квадратов VS квадрат суммы
'''
a = int(input('a: '))
b = int(input('b: '))
c = (a + b)**2
print(f'квадрат суммы {a} и {b} равен = {c}')
print(f'сумма квадратов {a} и {b} равен = {a**2 + b**2} ')
'''

#пересчет временного интервала
'''
x = 150
a = x // 60
b = x - a * 60
print(f'{x} мин - это {a} час {b} минут')

x = int(input('x: '))
a = x // 60
b = x % 60
print(f'{x} мин - это {a} час {b} минут')
'''


# Условные операторы (Ветвления)
'''
x = input('x: ')
print(type(x))

if x == 'green':  # если
    print("Можно идти")
elif x == 'yellow':   # иначе если
    print('Wait')
elif x == 'red':
    print('Стой')
else:  # иначе
    print('Это не светафор')
'''


# логические связки > < >= <=
# != - сравнение (неравно)
# = - присваивание данных
# == - сравнение (равно)
# print(4 != 10) # True

# Задача на координатную плоскость
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
    print('Лежит на осях')
'''


# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print(1)
    else:  # x > 0, y <= 0
        print(4)
else:
    if y > 0:  # x <= 0, y > 0
        print(2)
    else:  # x <= 0, y < 0 or y == 0
        print(3)
'''

# Логические связки: and, or
'''
a = 4
b = 5
c = 0

if (a > 0 and b < 0) or c == 0:
    print(True)
else:
    print(False)

# if a > 0 and b < 0 and c == 0:
#     print(True)
# else:
#     print(False)
'''

# Самописный калькулятор
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} {s} {b} = {a + b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
elif s == '/' and b == 0:
    print(f'Делить на нуль нельзя!')
elif s == '/':
    print(f'{a} {s} {b} = {a / b}')
else:
    print('Нет операции')
'''




# ZeroDivisionError: division by zero
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

try:
    if s == '/':
        print(f'{a} {s} {b} = {a / b}')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
'''

x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2 and y1 == y2:
    print("Надо походить фигурой!")
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
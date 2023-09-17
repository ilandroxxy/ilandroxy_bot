

# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Условные операторы (ветвление): if, elif, else
'''
x = int(input('x: '))
y = int(input('y: '))

# and - связки "и" (то есть все условия должны быть истинными)

if x > 0 and y > 0:  # if (если)
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:  # elif (иначе если)
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else (иначе)
    print('Точка лежит на осях')
'''


# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('Первая четверть')
    else:  # x > 0 and y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0 and y > 0
        print('Вторая четверть')
    else:  # x <= 0 and y <= 0
        print('Третья четверть')
'''

'''
x = int(input('Введите четное число: '))
if x % 2 == 0:
    print(x)
else:
    print('Число нечетное.')
'''

'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))
if s == '+':
    print(f'{a} {s} {b} = {a+b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
elif s == '/':
    try:
        print(f'{a} {s} {b} = {a / b}')    # ZeroDivisionError
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
'''


'''
try:
    a = int(input('a: '))
    s = input('s: ')
    b = int(input('b: '))
    
    if s == '+':
        print(f'{a} {s} {b} = {a+b}')
    elif s == '-':
        print(f'{a} {s} {b} = {a - b}')
    elif s == '*':
        print(f'{a} {s} {b} = {a * b}')
    elif s == '/':
        print(f'{a} {s} {b} = {a / b}')    # ZeroDivisionError
except Exception as e:
    print(f'Сработала ошибка: {e}')
'''

# Логические связки or, and, not
'''
a = 5
b = 6
c = -6
if (a > 0 or b > 0) and c > 0:
    print('YES')
else:
    print('NO')
'''

'''
flag = True
print(not flag)  # False

# Заполните список введнными числами, пока не будет передан 0

M = []
while flag:
    print(M)
    x = int(input('x: '))
    if x == 0:
        flag = False
    M.append(x)
'''

# Напишите программу, которая принимает возраст от пользователя
# и выводит сообщение "Вам можно смотреть этот фильм", если возраст больше или равен 18,
# и "Вы слишком молоды для просмотра этого фильма", если возраст меньше 18.
'''
year = int(input())
if year >= 18:
    print('Вам можно смотреть этот фильм')
else:
    print('Вы слишком молоды для просмотра этого фильма')
'''


# Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
'''


# endregion Урок: ***************************************************************


# todo: Сева = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:



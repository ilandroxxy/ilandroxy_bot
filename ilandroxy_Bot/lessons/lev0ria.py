# region Домашка: ******************************************************************


'''
# Вариант 1
x = input()
if len(x) == 5:
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    e = int(x[4])
    if (a * c) == (b + d + e):
        print("Да")
    else:
        print("Нет")

# Вариант 2
a, b, c, d, e = [int(x) for x in input()]
if (a * c) == (b + d + e):
    print("Да")
else:
    print("Нет")

# Вариант 3
n = int(input())
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10
if a * c == b + d + e:
    print("Да")
else:
    print("Нет")
'''

'''
x = int(input())  # 12345
M = []
while x > 0:
    M.append(x % 10)
    x //= 10
M.reverse()
a, b, c, d, e = M
if a * c == b + d + e:
    print("Да")
else:
    print("Нет")
'''

'''
a = int(input())
b = int(input())
c = int(input())
if (a == b) + (b == c) + (a == c) == 1:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')
'''

# Дано натуральное число n.
# Напишите программу, которая определяет его максимальную и минимальную цифры.
'''
n = int(input())
maxi = -99999999
mini = 99999999
while n > 0:
    x = n % 10
    maxi = max(maxi, x)
    mini = min(mini, x)
    n //= 10
print(maxi)
print(mini)
'''

'''
# Дано натуральное число. Напишите программу, которая вычисляет:
# 
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

import math

n = int(input())   # 12345
N = [int(x) for x in str(n)]  # TypeError: 'int' object is not iterable
print(sum(N))  # сумму его цифр;
print(len(N))  # количество цифр в нем;
print(math.prod(N))  # произведение его цифр;
print(sum(N) / len(N))  # среднее арифметическое его цифр;
print(N[0])  # его первую цифру;
print(N[0] + N[-1])
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 2 №35460
# Логическая функция F задаётся выражением ¬((x ∨ y) → (z ∧ w)) ∧ (x → w).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not((x or y) <= (z and w))) and (x <= w)
                if F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №18483
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                print(x, y, z, w, int(F))
'''


# Тип 6 №52177
# В начальный момент Черепаха находится в начале координат и направлена вверх
# (вдоль положительного направления оси ординат).
#
# Черепаха выполнила следующую программу:
# Повтори 4 [Вперёд 6 Направо 90 Вперёд 6 Налево 90 Вперёд 6 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут
# находиться внутри области, ограниченной линией, полученной при выполнении данной программы.
#
# Точки, расположенные на линии, не учитывать.
'''
import turtle as t
t.tracer(0)
t.left(90)
l = 30

for i in range(4):
    t.forward(6 * l)
    t.right(90)
    t.forward(6 * l)
    t.left(90)
    t.forward(6 * l)
    t.right(90)

t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''

'''
import turtle as t
t.left(90)
t.speed(100)
l = 30

t.begin_fill()
for i in range(4):
    t.forward(6 * l)
    t.right(90)
    t.forward(6 * l)
    t.left(90)
    t.forward(6 * l)
    t.right(90)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-30*l, 30*l, l):
    for y in range(-30*l, 30*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
t.done()
'''
# Ответ: 145


# endregion Урок: ******************************************************************

# Лев = [2.1, 6.1]
# КЕГЭ  = []
# на следующем уроке:

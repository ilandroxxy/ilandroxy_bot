# Точки на линии учитывать не следует. - обращайте внимание на это условие!

# region Тип 6 № 47393
"""
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 6 [Направо 36 Вперёд 10 Направо 36]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать следует.

# её голова направлена вдоль положительного направления оси ординат, хвост опущен.

import turtle as t

t.left(90)  # её голова направлена вдоль положительного направления оси ординат, хвост опущен.

l = 30  # для масштаба (умножаем на forward и x, y)
t.speed(10)

for _ in range(6):
    t.right(36)
    t.forward(10 * l)  # Повтори 6 [Направо 36 Вперёд 10 Направо 36]
    t.right(36)


t.pu()
t.color('red')
for x in range(0, 17):
    for y in range(-9, 9):  # диапазоны пытаемся угадать относительно декартовой системы координат (чтоб фигура входила)
        t.goto(x * l, y * l)  # перейти в точку координат с масштабом l
        t.dot(3) # отрисовка точки с толщиной пера 3

t.done()  # зафиксировать вывод программы
"""
# Ответ: 173
# endregion Тип 6 № 47393

# region Тип 6 № 47406
'''
# Исполнитель Черепаха действует на плоскости с декартовой системой координат.
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 12 Направо 90]
# Повтори 3 [Вперёд 12 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом: Повтори 4 [Вперёд 12 Направо 90]
# и находиться вне области, ограниченной линией, заданной данным алгоритмом: Повтори 3 [Вперёд 12 Направо 120].
# Точки на линии учитывать не следует.

from turtle import *

n = 30  # это переменная для масштаба изображения
left(90)  # условие: голова направлена вдоль положительного направления оси ординат
color('red')  # меняем цвет отрисовки (пожеланию)

# Тут описываем алгоритм из условия и не забываем умножать forward на n
for i in range(4):
    forward(12 * n)
    right(90)
color('green')
for i in range(3):
    forward(12 * n)
    right(120)

# А тут мы рисуем точки декартовой системы (опять же с масштабом n)
pu()  # поднять перо, чтобы не рисовать линии
for x in range(13):
    for y in range(13):
        goto(x * n, y * n)
        dot(5)  # нарисовать точку толщины 5
done()
'''
# Ответ: 65
# endregion Тип 6 № 47406

# region Тип 6 № 47404
"""
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 10 Направо 90]
# Направо 30
# Повтори 5 [Вперёд 6 Направо 60 Вперёд 6 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом: Повтори 4 [Вперёд 10 Направо 90]
# и находиться вне области, ограниченной линией, заданной данным алгоритмом:
# Повтори 5 [Вперёд 6 Направо 60 Вперёд 6 Направо 120].
# Точки на линии учитывать не следует.


from turtle import *

n = 30  # это переменная для масштаба изображения
left(90)  # условие: голова направлена вдоль положительного направления оси ординат
color('red')  # меняем цвет отрисовки (пожеланию)

# Тут описываем алгоритм из условия и не забываем умножать forward на n
for i in range(4):
    forward(10 * n)
    right(90)
right(30)
color('green')
for i in range(5):
    forward(6 * n)
    right(60)
    forward(6 * n)
    right(120)

# А тут мы рисуем точки декартовой системы (опять же с масштабом n)
pu()  # поднять перо, чтобы не рисовать линии
for x in range(13):
    for y in range(13):
        goto(x * n, y * n)
        dot(3)  # нарисовать точку толщины 5
done()
"""
# Ответ: 51
# endregion Тип 6 № 47404

# region Тип 6 № 47246
"""
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 14 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать не следует.

from turtle import *
left(90)
color('red')

n = 30
for i in range(4):
    forward(14 * n)
    right(120)

color('blue')
pu()
for x in range(15):
    for y in range(15):
        goto(x * n, y * n)
        dot(3)
done()
"""
# Ответ: 78
# endregion Тип 6 № 47246

# region Тип 6 № 47407
"""
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 8 Направо 90]
# Повтори 3 [Вперёд 12 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом:Повтори 4 [Вперёд 8 Направо 90]
#
# и находиться вне области, ограниченной линией, заданной данным алгоритмом:
# Повтори 3 [Вперёд 12 Направо 120]. Точки на линии учитывать не следует.

from turtle import *
left(90)
color('red')

n = 50
for i in range(4):
    forward(8 * n)
    right(90)
color('green')
for i in range(3):
    forward(12 * n)
    right(120)

color('blue')
pu()
for x in range(15):
    for y in range(15):
        goto(x * n, y * n)
        dot(3)
done()
"""
# Ответ: 13
# endregion Тип 6 № 47407

# region Тип 6 № 47403
'''
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 12 Направо 90]
# Направо 30
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом: Повтори 4 [Вперёд 12 Направо 90]
#
# и находиться вне области, ограниченной линией, заданной данным алгоритмом:
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]. Точки на линии учитывать не следует.

import turtle as t
t.left(90)
n = 30

for _ in range(4):
    t.forward(12 * n)
    t.right(90)
t.right(30)
t.color('red')
for _ in range(3):
    t.forward(8 * n)
    t.right(60)
    t.forward(8 * n)
    t.right(120)

t.color('blue')
t.pu()
for x in range(13):
    for y in range(13):
        t.goto(x * n, y * n)
        t.dot(3)
t.done()
'''
# Ответ: 73
# endregion Тип 6 № 47403

# region Тип 6 № 47312
'''
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 5 Направо 90 Вперёд 7 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать следует.

from turtle import *
left(90)
color('Blue')
l = 30
for i in range(4):
    forward(5*l)
    right(90)
    forward(7*l)
    right(90)
pu()
for x in range(8):
    for y in range(6):
        goto(x*l, y*l)
        dot(5)
done()
'''
# Ответ 48
# endregion Тип 6 № 47312

# region Тип 6 № 47390
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 10 [Направо 60 Вперёд 1 Направо 60 Вперёд 1 Направо 270]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать НЕ следует. (опечатка)
"""
from turtle import *
left(90)
color('red')
l = 50
for i in range(19):
    right(60)
    forward(1*l)
    right(60)
    forward(1*l)
    right(270)
    
pu()
for x in range(-5, 6):
    for y in range(-6, 5):
        goto(x*l, y*l)
        dot(3)
done()
"""
# Ответ: 38
#  endregion Тип 6 № 47390

# region Тип 6 № 47316
"""
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 5 [Вперёд 9 Направо 90 Вперёд 3 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать следует.

# eё голова направлена вдоль положительного направления оси ординат, хвост опущен.

from turtle import *
left(90)
l = 50
for i in range(5):
    forward(9 * l)
    right(90)
    forward(3 * l)
    right(90)

pu()
color('red')
for x in range(0, 4):
    for y in range(10):
        goto(x * l, y * l)
        dot(5)
done()
"""
# Ответ: 40
# endregion Тип 6 № 47316

# region Тип 6 № 47302
"""
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 10 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

from turtle import *
left(90)
color('red')
l = 20
for i in range(4):
    forward(10*l)
    right(90)
pu()
for x in range(-2, 12):
    for y in range(-2, 12):
        goto(x*l, y*l)
        dot(3)
done()
"""
# Ответ: 81
# endregion Тип 6 № 47302

# region Тип 6 № 47307
'''
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 10 Направо 60 Вперёд 10 Направо 120]
# Определите, сколько точек с целочисленными координатами будут
# находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
from turtle import *
left(90)
color("blue")
l = 15
for i in range(4):
    forward(10 * l)
    right(60)
    forward(10 * l)
    right(120)
pu()
for x in range(0, 15):
    for y in range(0, 15):
        goto(x * l, y * l)
        dot(3)
done()
'''
# Ответ: 80
# endregion Тип 6 № 47307

# region Тип 6 № 47305
'''
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 9 Направо 90 Вперёд 7 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать не следует.

import turtle as t

t.left(90)
t.speed(10)
l = 30

for _ in range(4):
    t.fd(9 * l)
    t.right(90)
    t.fd(7 * l)
    t.right(90)

t.pu()  # pen up - поднять перо
t.color('red')
for x in range(0, 8):
    for y in range(0, 10):
        t.goto(x * l, y * l)
        t.dot(3)
t.done()
'''
# Ответ: 48
# endregion Тип 6 № 47305

# region Тип 6 № 47247 новое решение
'''
# Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 8 [Вперёд 6 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

import turtle as t
t.color('black', 'blue')
t.speed(10)
l = 23

t.begin_fill()
t.left(90)
for i in range(3):  # чтоб отрисовать ровно одну фигуру хватит 3-х шагов
    t.forward(6*l)
    t.right(120)
t.end_fill()

canvas = t.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
t.done()
'''
# Ответ: 13
# endregion  Тип 6 № 47247

# region Тип 6 № 47407 новое решение
'''
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 8 Направо 90]
# Повтори 3 [Вперёд 12 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом:Повтори 4 [Вперёд 8 Направо 90]
# и находиться вне области, ограниченной линией, заданной данным алгоритмом: Повтори 3 [Вперёд 12 Направо 120].
# Точки на линии учитывать не следует.

import  turtle as t
l = 30
t.left(90)
t.color('red')

t.begin_fill()
for _ in range(4):
    t.forward(8 * l)
    t. right(90)
t.end_fill()

t.begin_fill()
for _ in range(3):
    t.forward(12 * l)
    t. right(120)
t.end_fill()

canvas = t.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100 * l, 100 * l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)

t.done()
'''
# Ответ: 13
# endregion Тип 6 № 47407 новое решение

# region Тип 6 № 47303 новое решение
'''
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
#
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 5 Направо 90 Вперёд 10 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать не следует.


import  turtle as t
l = 30
t.left(90)
t.color('red')

t.begin_fill()
for _ in range(2):
    t.forward(5 * l)
    t. right(90)
    t.forward(10 * l)
    t.right(90)
t.end_fill()

canvas = t.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100 * l, 100 * l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)

t.done()
'''
# Ответ: 36
# endregion Тип 6 № 47303 новое решение

# region Тип 6 № 47310 новое решение
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 6 Направо 150 Вперёд 6 Направо 30]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать не следует.

# Вариант 1
'''
import turtle as t
t.left(90)
l = 40

for _ in range(4):
    t.forward(6 * l)
    t.right(150)
    t.forward(6 * l)
    t.right(30)

t.color('red')
t.pu()
for x in range(0, 10):
    for y in range(-10, 10):
        t.goto(x * l, y * l)
        t.dot(3)

t.done()
'''

# Вариант 2
'''
import turtle as t
t.left(90)
l = 40
t.color('red')

t.begin_fill()
for _ in range(2):
    t.forward(6 * l)
    t.right(150)
    t.forward(6 * l)
    t.right(30)
t.end_fill()

canvas = t.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)

t.done()
'''
# Ответ: 12
# endregion Тип 6 № 47310

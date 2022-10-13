# Точки на линии учитывать не следует. - обращайте внимание на это условие!


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



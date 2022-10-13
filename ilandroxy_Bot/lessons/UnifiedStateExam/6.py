# Тип 6 № 47406
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
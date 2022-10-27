# region Домашка:



# endregion Домашка:



# region Урок:

# Тип 6 № 47390
'''
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 10 [Направо 60 Вперёд 1 Направо 60 Вперёд 1 Направо 270]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать следует.

import turtle

l = 60  # масштаб отрисовки
turtle.speed(10)
turtle.left(90)

for _ in range(12):
    turtle.right(60)
    turtle.forward(1 * l)
    turtle.right(60)
    turtle.forward(1 * l)
    turtle.right(270)

turtle.color('red')
turtle.pu()
for x in range(-3, 10):
    for y in range(-7, 3):
        turtle.goto(x * l, y * l)
        turtle.dot(6)


turtle.done()
'''
# Ответ: 38




# Тип 6 № 47407
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 8 Направо 90]
# Повтори 3 [Вперёд 12 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом:Повтори 4 [Вперёд 8 Направо 90]
# и находиться вне области, ограниченной линией, заданной данным алгоритмом: Повтори 3 [Вперёд 12 Направо 120].
# Точки на линии учитывать не следует.


# вариант 1
'''
import turtle

l = 60  # масштаб отрисовки
turtle.speed(10)
turtle.left(90)

for _ in range(4):
    turtle.forward(8 * l)
    turtle.right(90)

turtle.color('blue')
for _ in range(3):
    turtle.forward(12 * l)
    turtle.right(120)


turtle.color('red')
turtle.pu()
for x in range(0, 10):
    for y in range(0, 10):
        turtle.goto(x * l, y * l)
        turtle.dot(2)

turtle.done()
'''


# Вариант 2
'''
import turtle

l = 60  # масштаб отрисовки
# turtle.speed(10)
turtle.left(90)
turtle.color('red') 

turtle.begin_fill()
for _ in range(4):
    turtle.forward(8 * l)
    turtle.right(90)
turtle.end_fill()

turtle.begin_fill()
for _ in range(3):
    turtle.forward(12 * l)
    turtle.right(120)
turtle.end_fill()


canvas = turtle.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)

turtle.done()
'''


# endregion Урок:


# todo: Булат = [2, 5, 6, 8, 12, 14, 16, 17], на следующем уроке: Отрабатываем 17 номер и 6 если понадобится
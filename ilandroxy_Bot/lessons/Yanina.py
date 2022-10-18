
# import turtle  # стандартное подключение библиотеки в Python проект. Везде таскаем с собой turtle.
# turtle.forward(1000)
# turtle.done()

# import turtle as t  # переименуем turtle. в t. (или любое другое имя)
# t.forward(1000)
# t.done()

# from turtle import forward, done  # подключаем только определенные функции из библиотеки
# forward(1000)
# done()

# from turtle import *  # Подключаем все функции из библиотеки (не нужно использовать turtle. )
# forward(1000)
# pu()
# done()


'''
import turtle as t

for i in range(4):
    t.forward(100)
    t.left(90)

t.color('red')
for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)

t.done()

'''

# Тип 6 № 47392
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 6 [Вперёд 10 Направо 60]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать следует.

# Eё голова направлена вдоль положительного направления оси ординат, хвост опущен.

import turtle as t  # 1
t.left(90)   # 2

t.speed(10)  # 3

l = 30  # 4

for _ in range(6):
    t.forward(10 * l)  # 5
    t.right(60)

t.color('red')  # 6
t.pu()  # 7
for x in range(0, 20):
    for y in range(-5, 20):
        t.goto(x * l, y * l)  # 8
        t.dot(3)  # 9
t.done()  # 10

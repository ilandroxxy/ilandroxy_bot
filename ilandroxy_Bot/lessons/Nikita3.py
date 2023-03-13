# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# разность которых четна и хотя бы одно из чисел делится на 19, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# #Порядок элементов в паре не важен.
'''
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] - M[j]) % 2 == 0 and (M[i] % 19 == 0 or M[j] % 19 == 0):
            count += 1
            maxi = max(maxi, M[i] + M[j])
print(count, maxi)
'''
# 2551262 19994


# В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых хотя бы
# одно число делится на минимальный элемент последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
mini = min([int(i) for i in open('17.txt') if int(i) % 21 == 0])  # на минимальный элемент последовательности, кратный 21
M = [int(i) for i in open('17.txt')]
count = 0
maxi = -9999
for i in range(0, len(M)-1):
    if M[i] % mini == 0 or M[i+1] % mini == 0:
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# 126 171120


# № 6741 Апробация 10.03.23 (Уровень: Базовый)
# В начальный момент Черепаха находится в начале координат и направлена вверх (вдоль положительного направления оси ординат).
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 10 Направо 270]
# Поднять хвост
# Вперёд 3 Направо 270 Вперёд 5 Направо 90
# Опустить хвост
# Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270]

# Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур, ограниченных
# заданными алгоритмом линиями, включая точки на линиях.
'''
import turtle as t
t.left(90)
t.speed(10)
l = 30

for i in range(4):
    t.forward(10 * l)
    t.right(270)
t.up()
t.forward(3 * l)
t.right(270)
t.forward(5 * l)
t.right(90)
t.down()
t.color('blue')
for i in range(2):
    t.forward(10 * l)
    t.right(270)
    t.forward(12 * l)
    t.right(270)
t.up()
for x in range(0, -20, -1):
    for y in range(0, 15):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''


# № 6744 Апробация 10.03.23 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, в которых сумма наибольшего и наименьшего чисел меньше суммы двух оставшихся.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if (max(M) + min(M)) < sum(M) - (max(M) + min(M)):
        count += 1
print(count)
'''
# Ответ: 1503

# endregion Урок: ******************************************************************


# todo: Никита3 = [5, 12, 14, 17]
# на прошлом уроке:  Прорешивали задачи с апробации от 10.03.23 + повторили 17 номер
# на следующем уроке:

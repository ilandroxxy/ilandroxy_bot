
# region Домашка: ******************************************************************


# Черепахе был дан для исполнения следующий алгоритм:
# Направо 315 Повтори 7 [Вперёд 12 Направо 45 Вперёд 6 Направо 135].
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
'''
import turtle as t
t.tracer(0)
t.left(90)
l = 30

t.right(315)
for i in range(7):
    t.forward(12*l)
    t.right(45)
    t.forward(6*l)
    t.right(135)

t.up()
for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x*l, y*l)
        t.dot(2, 'red')
t.done()
'''


# КЕГЭ № 6259 Danov2302 (Уровень: Базовый) (А.Богданов)
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 10 [Вперёд 10 Направо 45]
#
# Определите, сколько точек с целочисленными координатами будут
# находиться точно на границе фигуры нарисованной данным алгоритмом.
'''
import turtle as t

t.tracer(0)
l = 20
t.left(90)

for i in range(10):
    t.forward(10 * l)
    t.right(45)

t.up()
for x in range(-20, 40):
    for y in range(-20, 40):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''


# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 6 [Повтори 3 [Вперед 7 Направо 120] Направо 60]
#
# Сколько точек с целочисленными координатами находятся внутри получившейся фигуры?
# Точки на внешних и внутренних линиях учитывать не нужно.

'''
import turtle as t

t.tracer(0)
l = 40
t.left(90)

for _ in range(6):
    for _ in range(3):
        t.forward(7 * l)
        t.right(120)
    t.right(60)

t.up()
for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x * l, y * l)
        t.dot(2, 'blue')
t.done()
'''

# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Теория списков
# - Списки содержат в себе неограниченное кол-во элементов, разных типов данных
# - Каждый элемент имеент порядковый номер - индекс
# - Индексы считаются слева-направо начиная с нуля или справа-налево начиная с -1
# - В списке можно менять элементы используя для этого их индексы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')
'''

# Срезы списков:
'''
M = ['a', 'b', 'c', 'd', 'e']

print(M[:3])  # ['a', 'b', 'c']
print(M[3:])  # ['d', 'e']
print(M[:])  # ['a', 'b', 'c', 'd', 'e']
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a']
print(M[::2])  # ['a', 'c', 'e']
'''

# Изменения элементов списка
'''
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()


for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

M[0] = 'a'
print(M)  # ['a', 'b', 'cc', 'ddd', 'eeee']
'''

# Функции списков
'''
M = [1, 4, 5, 6, 7]

print(len(M))  # длина списка (кол-во элементов)
print(sum(M))
print(max(M))
print(min(M))

print(set(M))  # множество - не может иметь копий элементов (выводим значения списка без копий)
print(len(set(M)))  # "Сколько различных значений?"

print(sorted(M))  # [1, 4, 5, 6, 7]
print(sorted(M, reverse=True))  # [7, 6, 5, 4, 1]
'''

# Методы списков (это частный случай функций, то есть когда функция прописана под определенный тип данных)
'''
M = [1, 3, 4, 5, 6, 1]

print(M.count(1))  # 2 - возвращает кол-во вхождений элемента в список
print(M.index(1))  # 0 - возвращает индекс первого вхождения элемента в список

M.append(100)  # - добавить элемент в конец списка
print(M)  # [1, 3, 4, 5, 6, 1, 100]

M = M + [4, 5, 6]  # добавили элементы справа к списку
print(M)  # [1, 3, 4, 5, 6, 1, 100, 4, 5, 6]

M = [1, 2, 3] + M  # добавили элементы слева к списку
print(M)  # [1, 2, 3, 1, 3, 4, 5, 6, 1, 100, 4, 5, 6]

M.sort()
print(M)  # [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 100]

M.reverse()  # развернули список в обратном порядке 
print(M)  # [100, 6, 6, 5, 5, 4, 4, 3, 3, 2, 1, 1, 1]
'''

# Генераторы списков
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

M = [int(x) for x in open('17.txt')]
chet = [x for x in M if x % 2 == 0]
nechet = [x for x in M if x % 2 != 0]
print(M)
'''
# endregion Урок: ******************************************************************


# Варя = [2.1, 6.1]
# КЕГЭ  = []
# на следующем уроке:

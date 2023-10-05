
# region Домашка: ******************************************************************

# https://stepik.org/lesson/1051612/step/10?unit=1060698
# На вход программе подается последовательность целых чисел,
# каждое число на отдельной строке. Признаком окончания последовательности
# является любое отрицательное число, при этом в саму последовательность оно
# не входит. Напишите программу, которая выводит сумму всех членов данной
# последовательности.

# Вариант 1
'''
summ = 0
while True:
    x = int(input())
    if x < 0:
        break
    summ += x
print(summ)
'''


# Вариант 2
'''
x = int(input())
summ = 0
while x >= 0:
    summ += x
    x = int(input())
print(summ)
'''

#  ¬x    --->  (not x)  - отрицание (инверсия)
# x ∧ y  --->  x and y  - конъюнкция (логическое умножение)
# x ∨ y  --->  x or y  - дизъюнкция (логическое сложение)
# x → y  --->  x <= y  - импликация
# x ≡ y  --->  x == y  - тождество (сравнение)
'''
x, y, z, w = 1, 1, 1, 1

# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))

F = ((x <= y) and (y <= w)) or (z == (x or y))
# https://inf-ege.sdamgia.ru/problem?id=15787

# (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))
F = (x == (w or y)) or ((w <= z) and (y <= w))
# https://inf-ege.sdamgia.ru/problem?id=15814

# (z ∧ y) ∨ ((x → z ) ≡ (y → w))

# https://inf-ege.sdamgia.ru/problem?id=15939

# ((y → x) ≡ (x → w)) ∧ (z ∨ x)
F = ((y <= x) == (x <= w)) and (z or x)
# https://inf-ege.sdamgia.ru/problem?id=16431

import useful
# print(useful.Valid_Parentheses('(((not x or z) == (y and (not w))) <= (z and y)'))

M = ['((y <= x) == (x <= w)) and (z or x)',
     '((x <= y) and (y <= w)) or (z == (x or y))',
     '(x == (w or y)) or ((w <=z) and (y <= w))',
     '']

for x in M:
    print(useful.Valid_Parentheses(x))
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


#  ¬x    --->  (not x)  - отрицание (инверсия)
# x ∧ y  --->  x and y  - конъюнкция (логическое умножение)
# x ∨ y  --->  x or y  - дизъюнкция (логическое сложение)
# x → y  --->  x <= y  - импликация
# x ≡ y  --->  x == y  - тождество (сравнение)

# Тип 2 №18704
# Логическая функция F задаётся выражением (x ∨ ¬y) ∧ ¬(w ≡ z) ∧ w.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (not y)) and (not(w == z)) and w
                if F:
                    print(x, y, z, w, F)
'''


# Тип 2 № 48423
# Логическая функция F задаётся выражением:
# (x → (y ≡ w)) ∧ (y ≡ (w → z))
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x <= (y == w)) and (y == (w <= z))
                print(x, y, z, w, int(F))
'''

#
# № 10084 Демоверсия 2024 (Уровень: Базовый)
# Миша заполнял таблицу истинности логической функции
# F= (x∧¬y)∨(y≡z)∨¬w , но успел заполнить лишь фрагмент из трёх различных
# её строк, даже не указав, какому столбцу таблицы
# соответствует каждая из переменных w,x,y,z.
# F = (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (y == z) or (not w)
                # if F == False:
                if (not F):
                    print(x, y, z, w, int(F))
'''


# № 9733 Основная волна 19.06.23 (Уровень: Базовый)
# Миша заполнял таблицу истинности логической функции

# F = (x ∧ ¬y) ∨ (x ≡ z) ∨ w
'''
x, y, z, w = 1, 1, 1, 1
F = (x and (not y)) or (x == z) or w

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (x == z) or w
                # if F == False:
                if (not F):
                    print(x, y, z, w, int(F))
'''
# if not((x and not(y)) or (y == z) or w)

# F=(y→x)∧¬z∧w,
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y <= x) and (not z) and w
                if F:
                    print(x, y, z, w, int(F))
'''

# ((x → y) ∧ (z ∨ w)) → ((x ≡ w) ∨ (y ∧ ¬z))  |  ((x <= y) and (z or w)) <= ((x == w) or (y and (not z)))
# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))  |  ((x <= y) and (y <= w)) or (z == (x or y))


# Тип 6 №52177
# В начальный момент Черепаха находится в начале координат и
# направлена вверх (вдоль положительного направления оси ординат).
# Черепаха выполнила следующую программу:
#
# Повтори 4 [Вперёд 6 Направо 90 Вперёд 6 Налево 90 Вперёд 6 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться
# внутри области, ограниченной линией, полученной при выполнении данной программы.
# Точки, расположенные на линии, не учитывать.
'''
import turtle as t
t.left(90)
l = 20
t.speed(10)

for _ in range(4):
    t.forward(6 * l)
    t.right(90)
    t.forward(6 * l)
    t.left(90)
    t.forward(6 * l)
    t.right(90)

t.up()
for x in range(0, 18):
    for y in range(-7, 14):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''
# Ответ: 145

# endregion Урок: ******************************************************************


# todo: GOAL = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:  # Циклы и разбор 2-го номера

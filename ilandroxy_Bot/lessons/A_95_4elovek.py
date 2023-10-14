# region Домашка: ************************************************************

'''
n = int(input())
summ = 0
for x in range(1, n+1):
    if (x**2) % 10 in (2, 5, 8):
        summ += x
print(summ)
'''

'''
n = int(input())  # 123456
M = []
while n > 0:
    M.append(n % 10)
    n //= 10
M.reverse()
print(M[2])
'''

'''
n = int(input())
s = str(n)
print(s[2])
'''


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

#  ¬x     --->    (not x)  - инверсия (отрицание)
# x ∧ y   --->    x and y  - конъюнкция (логическое умножение)
# x ∨ y   --->    x or y   - дизъюнкция (логическое сложение)
# x → y   --->    x <= y   - импликация
# x ≡ y   --->    x == y   - тождество (сравнение)
'''
print('x y z w F')
for x in range(2):  # range(START=0, STOP=2-1, STEP=1)
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = (not(y <= x)) or (z <= w) or (not z)   # №47206  ¬(y→x)∨(z→w)∨¬z
                # F = ((x <= y) or (z <= w)) and ((z == y) <= (w == x))  # №56502 ((x→y)∨(z→w)) ∧ ((z≡y)→(w≡x))
                F = (x or (not y)) and (not(w == z)) and w  # Тип 2 №18704  (x ∨ ¬y) ∧ ¬(w ≡ z) ∧ w
                if F:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №52173
# Логическая функция F задаётся выражением: (z≡¬x)→((w→¬y)∧(y→x))
'''
print('x y z w F')
for x in range(2):  # range(START=0, STOP=2-1, STEP=1)
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                print(x, y, z, w, int(F))
'''

# Тип 6 №51975
# В начальный момент Черепаха находится в начале координат и направлена
# вверх (вдоль положительного направления оси ординат).

# Черепаха выполнила следующую программу:
# Повтори 4 [Вперёд 7 Направо 90 Вперёд 7 Налево 90 Вперёд 7 Направо 90]
#
# Определите, сколько точек с целочисленными координатами
# будут находиться внутри области, ограниченной линией, полученной при выполнении данной программы.
# Точки, расположенные на линии, не учитывать.
'''
import turtle as t
t.left(90)
t.speed(100)
l = 20

# Повтори 4 [Вперёд 7 Направо 90 Вперёд 7 Налево 90 Вперёд 7 Направо 90]
for i in range(4):
    t.forward(7*l)
    t.right(90)
    t.forward(7*l)
    t.left(90)
    t.forward(7*l)
    t.right(90)

t.up()
for x in range(0, 25):
    for y in range(-10, 20):
        t.goto(x*l, y*l)
        t.dot(2, 'red')

t.done()
'''

# Вариант 2
'''
import turtle as t
t.left(90)
t.speed(10)
l = 20

t.begin_fill()
for i in range(4):
    t.forward(7*l)
    t.right(90)
    t.forward(7*l)
    t.left(90)
    t.forward(7*l)
    t.right(90)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)  # 204

t.done()
'''

# endregion Урок: ***************************************************************


# todo: Сева = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:

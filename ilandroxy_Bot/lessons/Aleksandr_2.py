# region Домашка:

# Задание №1 "Третья цифра"
'''
n = int(input('n: '))
if n <= 99:
    print(f'Число должно состоять как минимум из трех цифр')
else:
    while n > 1000:
          n //= 10
    print(n % 10)
'''

'''
n = int(input('n: '))
s = str(n)
print(s[2])
'''

# Задание №2 "Квадрат числа"
'''
n = int(input('x: '))
for i in range(0, n+1, 1):
    print(f'Квадрат числа {i} равен {i**2}')
'''


# Задание №3 "Факториал"
'''
n = int(input('n: '))
f = 1
if n > 12:
    print(f'Число должно быть меньше или равно 12')
else:
    while n > 1:
        f = f * n
        n = n - 1
    print(f)
'''
# endregion Домашка:


# region Урок:

# Правила математической логики в Пайтон:
#   ¬w     <--->   (not(w))   инверсия (отрицание)
#  x ∧ y   <--->   x and y    конъюнкция (логическое умножение)
#  x ∨ y   <--->   x or y     дизъюнкция (логическое сложение)
#  x → y   <--->   x <= y     импликация
#  y ≡ z   <--->   y == z     тождество (равны ли)

# Тип 2 № 26974
'''
# Логическая функция F задаётся выражением (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w.
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = ( (x or y) and (not(y == z)) and (not (w)) )
                # if F == True:
                F = (x or y) and (not (y == z)) and (not (w))
                if F:  # если истина
                    print(x, y, z, w, F)
'''
# Ответ: xzyw



# Тип 2 № 17366
'''
# Логическая функция F задаётся выражением ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
#
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ( ((x and w) or (w and z)) == ((z <= y) and (y <= x)) )
                if F == True:
                    print(x, y, z, w, F)
'''
# Ответ: yzwx





# Тип 6 № 47310
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
# Ответ: 12


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
# endregion Урок:


# todo: Александр_2 = [2, 6], на следующем уроке: Разбираем списки и 14, 5







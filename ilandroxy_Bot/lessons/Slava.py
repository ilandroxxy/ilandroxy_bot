
# region Домашка: ******************************************************************************



# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

'''
def F(n):
    if n < 50:
        return n
    if n > 49:
        return 2 * G(50 - n // 2)

def G(n):
    if n > 40:
        return 10
    if n < 41:
        return 30 + F(n + 600//n)
print(F(80))
'''
# Ответ: 812

'''
import turtle as t

t.left(90)
t.speed(1)
l = 30
x, y = 0, 0
k = 1
for _ in range(2):
    x += 6
    y += 2
    t.goto(x*l, y*l)
    print(k, x, y)
    k += 1

    x += 0
    y += -2
    t.goto(x*l, y*l)
    print(k, x, y)
    k += 1

for _ in range(3):
    x += 2
    y += -1
    t.goto(x*l, y*l)
    print(k, x, y)
    k += 1

    x += -2
    y += -1
    t.goto(x * l, y * l)
    print(k, x, y)
    k += 1

for _ in range(6):
    x += -2
    y += 1
    t.goto(x*l, y*l)
    print(k, x, y)
    k += 1
t.done()
'''

# Задание 4750
'''
import turtle as t

t.left(90)
t.speed(10)
l = 30
x, y = 0, 0
t.color('red')
t.begin_fill()
for _ in range(2):
    x += 6
    y += 2
    t.goto(x*l, y*l)

    x += 0
    y += -2
    t.goto(x*l, y*l)

for _ in range(3):
    x += 2
    y += -1
    t.goto(x*l, y*l)

    x += -2
    y += -1
    t.goto(x * l, y * l)

for _ in range(6):
    x += -2
    y += 1
    t.goto(x*l, y*l)
t.end_fill()

canvas = t.getcanvas()
count_in = 0
count_out = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100 * l, 100 * l, l):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5:
            count_in += 1
        if len(item) > 1 and item[0] == 5:
            count_out += 1
print(count_in, count_out)
print(count_in + (count_out / 2) - 1)  # формула Пика
t.done()
'''
# Ответ: 54



#  23 №4478
'''
def F(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return F(a - 3, b) + F(a // 2, b)
print(F(108, 42) * F(42, 12))
'''

#
# № 3693
'''
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**6, найдите все числа, соответствующие маске 12*45* и делящиеся на число 51 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им частные от деления на 51.


M = [i for i in range(0, 100)]
M.append('')
for x in M:
    for y in M:
        a = int(f'12{x}45{y}')
        if a < 10**6:
            if a % 51 == 0:
                print(a, a // 51)
'''
# Ответ:
# 122451 2401
# 122145 2395
# 127245 2495
# 124542 2442
# 124593 2443

# endregion Урок:  ******************************************************************************


# todo: Слава = [2, 5, 6, 8, 9, 12, 14+, 15+, 16, 17, 19, 20, 21, 23, 24+, 25.1], на следующем уроке: Разбираем 18 номера
# todo: сложности 18, 22, 26, 27
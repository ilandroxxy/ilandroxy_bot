# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 15 №29203
# Для какого наименьшего целого неотрицательного числа А выражение
# (3x + 7y < A) ∨ (x ≥ y) ∨ (y > 6)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''
# Вариант 1
def F(x, y, A):
    return (3*x + 7*y < A) or (x >= y) or (y > 6)


for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            # if F(x, y, A) == False:
            if not F(x, y, A):
                flag = False
                break
    # if flag == True:
    if flag:
        print(A)
        break


# Вариант 2
for A in range(300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (3 * x + 7 * y < A) or (x >= y) or (y > 6):
                k += 1
    if k == 90_000:
        print(A)
        break


# Вариант 3
def F(x, y, A):
    return (3*x + 7*y < A) or (x >= y) or (y > 6)


for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break


# Вариант 3.2
def F(x, y, A):
    return (3*x + 7*y < A) or (x >= y) or (y > 6)


R = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)
print(min(R))


# Вариант 4
print(min([A for A in range(0, 1000) if all(((3*x + 7*y < A) or (x >= y) or (y > 6)) for x in range(100) for y in range(100))]))
'''
# Ответ: 58


# Тип 15 №9322
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
# ДЕЛ(x, А) → (¬ДЕЛ(x, 21) + ДЕЛ(x, 35))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
# Задание К.Ю.Полякова
'''
def F(x, A):
    return (x % A == 0) <= ((x % 21 != 0) or (x % 35 == 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''
# Ответ: 5

# print(14 & 5)  # 4

# Тип 15 №34506
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
# x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''
def F(x, A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(0, 1000):
    if all(F(x, A) for x in range(0, 10000)):
        print(A)
        break
'''
# Ответ: 8


# Тип 15 №34540
# На числовой прямой даны два отрезка: Р = [12, 62] и Q = [52, 92].
# Какова наименьшая возможная длина интервала A, что логическое выражение
# ¬(¬(х ∈ А) ∧ (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x, a1, a2):  # a1 - начало интервала, a2 - конец интервала
    P = 12 <= x <= 62
    Q = 52 <= x <= 92
    A = a1 <= x <= a2
    return (not((not A) and P)) or Q


R = []
M = [x/4 for x in range(10*4, 100*4)]
# print(M)  # [10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, ...]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
'''
# Ответ: 39.75 -> 39.8 -> 39.9 -> 40

'''
import turtle as t
t.tracer(0)
t.left(90)
l = 30

for _ in range(4):
    t.forward(8*l)
    t.right(90)

t.color('green')
for _ in range(3):
    t.forward(12 * l)
    t.right(120)

t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''
# endregion Урок: ******************************************************************


# Марго = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 15.1, 16.1, 23.1]
# КЕГЭ  = []
# на следующем уроке: Разобраться с проблемой import turtle - вовторить задачи

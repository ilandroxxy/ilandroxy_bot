# region Домашка: ******************************************************************

# КЕГЭ № 8952 Джобс 02.06.2023 (Уровень: Базовый) (Е. Джобс)
# Найдите минимальное значение А, при котором значение выражения
# (x & 103 = 0) ∧ (x & 94 ≠ 0) → (x & A ≠ 0)
# тождественно истинно, то есть принимает значение 1 при любом натуральном значении х.
'''
def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# КЕГЭ № 7617 Досрочная волна 2023 (Уровень: Базовый)
# Для какого наименьшего неотрицательного целого числа А формула
# (x ≥ 9) ∨ (2x < y) ∨ (xy < A)
# тождественно истинна (т.е. принимает значение 1) при любых неотрицательных целых x и y.
'''
def F(x, y, A):
    return (x >= 9) or (2 * x < y) or (x * y < A)

for A in range (0, 1000):
    if all(F(x, y, A) for x in range (100) for y in range (100)):
        print(A)
        break
'''


# КЕГЭ № 5490 (Уровень: Базовый)
# Укажите наименьшее целое значение A, для которого формула
# (ДЕЛ(108, x)→ ¬ДЕЛ(x, y)) ∨ (x + y > 80) ∨ (A – y > x)
# тождественно истинна при любых натуральных значениях переменных x и y.
'''
def F(x, y, A):
    return ((108 % x == 0) <= (x % y != 0)) or (x + y > 80) or (A - y > x)

for A in range (0, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# КЕГЭ № 7846 Danov2304 (Уровень: Базовый) (А.Богданов)
# На числовой прямой даны два отрезка: P = [13; 19] и Q = [17; 23], A = [a1, a2].
# Укажите наибольшую возможную длину такого отрезка A, что формула
# ¬(¬(x ∈ P) → (x ∈ Q)) → ((x ∈ A) →(¬(x ∈ Q)→(x ∈ P)))
# тождественно истинна, то есть принимает значение 1 при любых x.
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not((not P) <= Q)) <= (A <= ((not Q) <= P))


R = []
M = [x / 5 for x in range(10 * 5, 30 * 5)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(round(max(R)))  
'''
# Ответ: 10.0 -> 10

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Считывание файла для 17 номера:
'''
M = [int(x) for x in open('17.txt')]
'''

# Типы задач 17 номера:
'''
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')
print()

# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    print(f'{x}{y}{z}', end=' ')
print()

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
# 12 13 14 15
# 23 24 25
# 34 35
# 45
'''

# Тип 17 №57424
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100000 включительно.
# Определите количество пар последовательности, в которых только один из элементов является двузначным числом,
# а сумма элементов пары кратна максимальному двузначному элементу последовательности.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (len(str(abs(x))) == 2) != (len(str(abs(y))) == 2):
        if (x + y) % max(A) == 0:
            R.append(x + y)
print(len(R), max(R))
'''
# Ответ: 16 9702


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo № 12418 (Уровень: Средний) - Тимур
# (Л. Шастин) Исполнитель преобразует число на экране.
# У исполнителя есть три команды, которые обозначены латинскими буквами:
# А. Вычесть 2
# В. Умножить на 2
# С. Умножить на 3
# Сколько существует программ, которые преобразуют исходное число 6 в число 48
# и при этом содержат не более двух команд А?

'''
import sys
sys.setrecursionlimit(10000)

def F(a, b, s: str):
    if a > b+2:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-2, b, s+'A') + F(a*2, b, s+'B') + F(a*3, b, s+'C')

print(F(6, 48, ''))

'''

# endregion Разобрать: *************************************************************


# Тимур = [2, 5, 6, 8, 12, 14, 15, 16, 17.1, 23]
# КЕГЭ  = []
# на следующем уроке: Разбираем/Добиваем 17 номера

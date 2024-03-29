# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 15 №8106
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наибольшего натурального числа А формула
# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
# Вариант 1
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)

# Вариант 2
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


for A in range(1, 1000):
    k = 0
    for x in range(1, 10000):
        if F(x, A):
            k += 1
    if k == 9999:
        print(A)

# Вариант 3.1
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)

# Вариант 3.2
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


# Вариант 3.3
print(max([A for A in range(1, 1000) if all(((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) for x in range(1, 10000))]))
'''
# Ответ: 12


# Тип 15 №59756
# Для какого наименьшего целого неотрицательного числа А выражение
# (x < A)∨(y < A) ∨ (y > − 5) ∨ (y< 2x − 15) тождественно истинно?
'''
def F(x, y, A):
    return (x < A) or (y < A) or (y > x - 5) or (y < 2*x - 15)


for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break
'''


# Тип 15 №34511
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Например, 14&5 = 11102&01012 = 01002 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
# x&25 ≠ 0 → (x&19 = 0 → x&А ≠ 0)
# тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''
def F(x, A):
    return (x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x, A) for x in range(10000)):
        print(A)
        break
'''
# Ответ: 8


# Тип 15 №34540
# На числовой прямой даны два отрезка: Р = [12, 62] и Q = [52, 92].
# Какова наименьшая возможная длина интервала A, что логическое выражение
# ¬(¬(х ∈ А) ∧ (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.

def F(x, a1, a2):
    P = 12 <= x <= 62  # (х ∈ Р)
    Q = 52 <= x <= 92  # (х ∈ Q)
    A = a1 <= x <= a2  # (х ∈ А)
    return (not((not A) and P)) or Q


R = []
M = [x / 10 for x in range(10 * 10, 100 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))

# Ответ: 39.75 -> 39.8 -> 39.9 -> 40



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


# Тимур = [2, 5, 6, 8, 12, 14, 15, 16, 23]
# КЕГЭ  = []
# на следующем уроке:

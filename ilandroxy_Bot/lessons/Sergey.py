
# region Домашка: ******************************************************************

# Тип 15 № 19067
# (x + 2y < A) ∨ (y > x) ∨ (x > 30)
'''
def fun(x, y, A):
    return (x + 2 * y < A) or (y > x) or (x > 30)

sps = []
for A in range(1, 1000):
    if all(fun(x, y, A) for x in range(100) for y in range(100)):
        sps.append(A)
print(min(sps))
'''
# ответ 91


# Тип 15 № 38949
# x & 85 = 0 → (x & 54 ≠ 0 → x & А ≠ 0)
'''
def fun(x):
    # return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))
    R = x & 85 == 0
    T = x & 54 != 0
    P = x & A != 0
    return R <= (T <= P)

sps = []
for A in range(0, 1000):
    if all(fun(x) for x in range(0, 1000)):
        sps.append(A)
print(min(sps))
'''
# Ответ: 34



# Тип 15 № 40731
# (x∈Q)→(¬(x∈P)→ ¬((x∈Q)∧¬(x∈A)))
#   ¬(x∈P) ---> (not P)
'''
def fun(x):
    A = a1 <= x <= a2
    P = 19 <= x <= 84
    Q = 4 <= x <= 51
    return Q <= ((not P) <= (not(Q and (not A))))

sps = []
M = [i/4 for i in range(0*4, 100*4)]
for a1 in M:
    for a2 in M:
        if all(fun(x) for x in M):
            sps.append(a2 - a1)
print(min(sps))  # 14.75 - нужно округлить 
'''
# Ответ: 15



# '''Тип 15 № 45249
# def fun(n, m):
#     return n % m == 0
# sps = []
# for A in range(1, 100):
#     if all((fun(x, 3) <= (not fun(x, 5))) or (x + A >= 90) for x in range(1, 100)):
#         sps.append(A)
# print(sps)
# ответ 75
# '''


# '''Тип 15 № 18499
# def fun(m, n):
#     return (2 * m + 3 * n > 40) or ((m < A) and (n <= A))
# sps = []
# for A in range(1, 100):
#     if all(fun(m, n) for m in range(0, 100) for n in range(0, 100)):
#         sps.append(A)
# print(min(sps))
# ответ 21
# '''


# Тип 15 № 9321
# ¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))
'''
def ost(n, m):
    return n % m == 0

def fun(x):
    return (not ost(x, A)) <= ((not ost(x, 21)) and (not ost(x, 35)))

sps = []
for A in range(1, 10000):
    if all(fun(x) for x in range(1, 10000)):
        sps.append(A)
print(max(sps))
'''

'''
def f(x):
    return (x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))

sps = []
for A in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        sps.append(A)
print(max(sps))
'''
# Ответ: 7


'''Тип 15 № 39244
def fun(x, A):
    return (x&105 == 0) <= ((x&58 != 0) <= (x&A != 0))
sps = []
for A in range(100):
    if all(fun(x, A) for x in range(100)):
        sps.append(A)
print(min(sps))
ответ 18
'''


# Тип 15 № 46973
# (x∈Q)→(((x∈P)≡(x∈Q))∨(¬(x∈P)→(x∈A)))
'''
def fun(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))

sps = []
M = [i/4 for i in range(50*4, 150*4)]
for a1 in M:
    for a2 in M:
        if all(fun(x) for x in M):
            sps.append(a2 - a1)
print(min(sps))  # 22.75  - округляем
'''
# Ответ: 23



'''Тип 15 № 29125
def fun(x, y, A):
    return (4 * x + 3 * y < A) or (x > y) or (y > 13)
sps = []
for A in range(100):
    if all(fun(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        sps.append(A)
print(min(sps))
ответ 92
'''

# ¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))

# Тип 15 № 9321
'''
for A in range(1, 10000):
    if all(((x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))) for x in range(1, 10000)):
        print(A)

# Вариант 2
print(max([A for A in range(1, 10000) if all(((x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))) for x in range(1, 10000))]))
'''
# Ответ: 7

# endregion Домашка: ******************************************************************

'''Тип 15 № 9653'''
'''def fun(x):
    P = 10 < x < 29
    Q = 13 < x < 18
    A = a1 < x < a2
    return (A <= P) or Q
rg = [i/4 for i in range(120)]
sps = []
for a1 in rg:
    for a2 in rg:
        if all(fun(x) for x in rg):
            sps.append(a2 - a1)
print(max(sps))
ответ 19
'''
'''Тип 15 № 15986'''
'''def fun(x, y):
    return (y + 2 * x != 48) or (A < x) or (x < y)
sps = []
for A in range(100):
    if all(fun(x, y) for x in range(100) for y in range(100)):
        sps.append(A)
print(max(sps))
ответ 15
'''

# Тип 15 № 3452
'''def fun(x):
    return (x & 51 == 0) or ((x&41 == 0) <= (x&A == 0))
sps = []
for A in range(100):
    if all(fun(x) for x in range(100)):
        sps.append(A)
print(min(sps))
ответ 0
'''
'''Тип 15 № 29663'''
'''def fun(x):
    return (A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))
sps = []
for A in range(1, 1000):
    if all(fun(x) for x in range(1, 1000)):
        sps.append(A)
print(max(sps))
ответ 30
'''
'''Тип 16 № 4978'''
'''def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n - 2) * (n - 1)
print(F(8))
ответ 105
'''

'''Тип 16 № 4658'''
'''def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n - 1) * n - 2 * F(n - 2)
print(F(6))
ответ 44
'''

#Тип 16 № 38591
'''def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    else:
        return 2 * F(n - 2)
print(F(26))
ответ 4122
'''

#Тип 23 № 6508
'''
def F(a, b):
    c = 0
    if a > b:
        return 0
    elif a == b:
        return 1
    elif len(str(a)) == 1:
        return F(a + 1, b) + F(a, b)
    elif len(str(a)) == 2:
        return F(a + 1, b) + F(a + 10, b)
    else:
        return F(a + 1, b) + F(a + 100, b)
print(F(15, 37))
'''

# Тип 23 № 6508 Добавить в вариант
# У исполнителя Прибавитель две команды, которым присвоены номера:
#
# 1. прибавь 1
# 2. увеличь старшую цифру числа на 1.

# Сколько есть программ, которые число 15 преобразуют в число 37?
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 10, b)
print(F(15, 37))


def F(a, b):
    if a >= b:
        return int(a == b)
    else:
        return F(a + 1, b) + F(a + 10, b)
print(F(15, 37))
'''


# Тип 23 № 18598
#
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# 3. Умножить на 3
# Сколько существует программ, которые преобразуют исходное число 1 в число 40,
# и при этом траектория вычислений содержит число 12 и не содержит числа 14?
'''
def F(a, b):
    if a > b or a == 14:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b) + F(a * 3, b)
print(F(1, 12) * F(12, 40))


def F(a, b):
    if a >= b or a == 14:
        return int(a == b)
    else:
        return F(a + 1, b) + F(a * 2, b) + F(a * 3, b)
print(F(1, 12) * F(12, 40))
'''



# Тип 23 № 27248 Добавить в вариант
# Исполнитель РазДва преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:

# 1. Прибавить 1
# 2. Умножить на 2

# Укажите наименьшее натуральное число, которое нельзя получить из исходного числа 1,
# выполнив программу исполнителя РазДва, содержащую не более пяти команд.

'''
def F(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    if c <= 5:
        return F(a + 1, b, c + 1) + F(a * 2, b, c + 1)
sps = []
for b in range(100):
    sps.append(F(1, b, int(0)))
print(sps)
'''

'''
a = set(range(6, 100))
print(a)
def f(x, h):
    if h == 5:
        if x in a:
            a.remove(x)
    else:
        f(x + 1, h + 1)
        f(x * 2, h + 1)
f(1, 0)
print(min(a))
'''


# region Урок: ******************************************************************

# Тип 25 № 27853
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [312614; 312651], числа,
# имеющие ровно шесть различных натуральных делителей. Для каждого найденного числа запишите эти шесть делителей
# в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
for n in range(312614, 312651+1):
    dl = []
    for j in range(1, n+1):
        if n % j == 0:
            dl.append(j)
    if len(dl) == 6:
        print(*dl)
'''
'''
def F(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

for n in range(312614, 312651+1):
    dl = F(n)
    if len(dl) == 6:
        print(*dl)
'''
# 1 2 4 78157 156314 312628
# 1 3 9 34739 104217 312651


# Тип 25 № 29673
# Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
#  Найдите все натуральные числа, принадлежащие
#  отрезку [123456789; 223456789] и имеющие ровно три нетривиальных делителя.
#  Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель.
# Ответы расположите в порядке возрастания.
'''
def F(n):
    dl = set()
    if round(n ** 0.5) == (n ** 0.5):
        for j in range(2, int(n**0.5)+1):  # не равный единице и самому числу
            if n % j == 0:
                dl.add(j)
                dl.add(n // j)
    return sorted(dl)

for n in range(123456789, 223456789+1):
    dl = F(n)
    if len(dl) == 3:
        print(n, max(dl))
'''
# Ответ:
# 131079601 1225043
# 141158161 1295029
# 163047361 1442897


# Тип 25 № 27855 i
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632; 95700], числа,
# имеющие ровно шесть различных чётных натуральных делителей (при этом количество нечётных делителей может быть любым).
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def F(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            if j % 2 == 0:
                dl.add(j)
            if (n // j) % 2 == 0:
                dl.add(n // j)
    return sorted(dl)

for n in range(95632, 95700+1):
    dl = F(n)
    if len(dl) == 6:
        print(*dl)
'''
# 2 10 50 3826 19130 95650
# 2 26 338 566 7358 95654
# 2 4 8 23918 47836 95672


# Тип 25 № 41000
# Пусть M(N) — сумма двух наибольших различных натуральных
# делителей натурального числа N, не считая самого числа и единицы.
# Если у числа N меньше двух таких делителей, то M(N) считается равным 0.
#
# Найдите 5 наименьших натуральных чисел, превышающих 11000000, для которых 0<M(N)<10000.
# В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):  # не считая самого числа и единицы
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

count = 0
for n in range(11000000+1, 10000000000):  # превышающих 11000000
    dl = F(n)
    if len(dl) >= 2:
        M = dl[-1] + dl[-2]
        if 0 < M < 10000:
            print(M)
            count += 1
            if count == 5:
                break
'''
# 8672
# 8388
# 8532
# 7042
# 7364


# Тип 25 № 28121 i
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [2422000; 2422080], простые числа. Выведите все найденные простые числа
# в порядке возрастания, слева от каждого числа выведите его номер по порядку,
# считая, что первое найденное число имеет номер «1», второе — «2», и т.д.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

count = 1
for n in range(2422000, 2422080+1):
    dl = F(n)
    if len(dl) == 0:
        print(count, n)
'''
# 2422027
# 2422033
# 2422037
# 2422073


# № 6276 Danov2302 (Уровень: Базовый)
# (А.Богданов) Найдите все натуральные числа, не превышающие 10**10,
# которые соответствуют маске 1?1?1?1*1 и при этом без остатка делятся на 2023, а сумма цифр числа равна 22.
# В ответе запишите все найденные числа в порядке возрастания.

# print(10**10)
# print('1?1?1?1**1')
'''
import itertools
M = ['']
for t in range(1, 2+1):
    for s in itertools.product('0123456789', repeat=t):
        s = ''.join(s)
        M.append(s)

for x in '0123456789':
    for y in '0123456789':
        for z in '0123456789':
            for w in M:
                A = f'1{x}1{y}1{z}1{w}1'
                B = [int(i) for i in A]
                if int(A) % 2023 == 0:
                    if sum(B) == 22:
                        print(A)
'''
# 19131511
# 1012141291
# 1319111311
# 1516111051



# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 12, 14, 15, 16, 23]
# на прошлом уроке: Плотно разобрали 16, 23 номера. Особенно хорошо проговорили моменты с рекурсией. Решали и аналитические задачи.
# на следующем уроке:

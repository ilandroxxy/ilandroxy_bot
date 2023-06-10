# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# 2
'''
print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((x <= y) == (z <= w)) or (x and w)):
                    print(x, y, z, w)
'''
# zyxw

# Тип 5 № 17324
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится двоичная запись числа N.
# 2. Удаляется первая слева единица и все следующие непосредственно за ней нули.
# Если после этого в числе не остаётся цифр, результат этого действия считается равным нулю.
# 3. Полученное число переводится в десятичную запись.
# 4. Новое число вычитается из исходного, полученная разность выводится на экран.
#
# Сколько разных значений будет показано на экране автомата при
# последовательном вводе всех натуральных чисел от 10 до 1000?
'''
m = []
a = set()
for i in range(10, 1001):
    n = bin(i)[2:]

    n = n[1:]

    n = int(n, 2)
    m.append(i - n)
    a.add(i - n)
print(len(set(m)))
print(len(a))
'''
# 991


# Тип 8 № 16886
# Матвей составляет 6-буквенные коды из букв М, А, Т, В, Е, Й.
# Каждую букву нужно использовать ровно 1 раз,
# при этом код не может начинаться с буквы Й и не может содержать сочетания АЕ.
# Сколько различных кодов может составить Матвей?
'''
alphabet = 'МАТВЕЙ'
count = 0
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    for f in alphabet:
                        slovo = a + b + c + d + e + f
                        if len(set(slovo)) == len(slovo):
                            if a != 'Й' and "АЕ" not in slovo:
                                count += 1
print(count)


import itertools
count = 0
for s in itertools.product('МАТВЕЙ', repeat=6):
    slovo = ''.join(s)
    if len(set(slovo)) == len(slovo):
        if slovo[0] != 'Й' and "АЕ" not in slovo:
            count += 1
print(count)


import itertools
count = 0
for s in itertools.permutations('МАТВЕЙ', 6):
    slovo = ''.join(s)
    if slovo[0] != 'Й' and "АЕ" not in slovo:
        count += 1
print(count)
'''

'''
import itertools
c = 0
for s in itertools.permutations('МАТВЕЙ', 6):
    slovo = ''.join(s)
    if s[0] != 'Й' and 'АЕ' not in slovo:
        c += 1
print(c)
'''


'''
alphabet = sorted('ПАРУС')
print(alphabet)  # ['А', 'П', 'Р', 'С', 'У']

ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(ALPHABET[:8])  # получили алфавит 8-ричной
print(ALPHABET[:16])  # получили алфавит 16-ричной
'''

# 12
'''
s = 1000 * '9'
while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)
print(s)
'''
# 8899

# 14
'''
y = 4 ** 2020 + 2 ** 2017 - 15
y = bin(y)
y = str(y)
print(y.count('1'))
'''
# 2015

# 15
'''
a = set([int(i) for i in range(-1000, 1000)])


def f(x, a):
    return ((x in a) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (x in a))


for x in range(-1000, 1000):
    if not f(x, a):
        a.remove(x)
print(len(a) - 1)
'''

# Тип 15 № 15803
# На числовой прямой задан отрезок A. Известно, что формула
#
# ((x ∈ A) → (x**2 ≤ 100)) ∧ ((x**2 ≤ 64) → (x ∈ A))
#
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?
'''
def F(x, a1, a2):
    A = a1 <= x <= a2
    return (A <= (x**2 <= 100)) and ((x**2 <= 64) <= A)

R = []
M = [i/4 for i in range(-100*4, 100*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(max(R))
'''
# 20


# Тип 15 № 11119
# На числовой прямой даны два отрезка: P = [20, 50] и Q = [30,65]. Отрезок A таков, что формул
#
# ¬(x ∈ A) → ((x ∈ P) →¬ (x ∈ Q))
#
# истинна при любом значении переменной x. Какова наименьшая возможная длина отрезка A?
'''
def F(x, a1, a2):
    P = 20 <= x <= 50
    Q = 30 <= x <= 65
    A = a1 <= x <= a2
    return (not A) <= (P <= (not Q))

R = []
M = [i/10 for i in range(10*10, 70*10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
'''



# 16
'''
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + n


print(f(40))
'''
# 820


# Тип 11 № 5237
# При регистрации в компьютерной системе каждому пользователю выдаётся идентификатор, состоящий из 10 символов,
# первый и последний из которых — одна из 18 букв, а остальные — цифры (допускается использование 10 десятичных цифр).
#
# Каждый такой идентификатор в компьютерной программе записывается минимально возможным и одинаковым целым количеством
# байт (при этом используют посимвольное кодирование; все цифры кодируются одинаковым и минимально возможным количеством
# бит, все буквы также кодируются одинаковым и минимально возможным количеством бит).
#
# Определите объём памяти, отводимый этой программой для записи 25 идентификаторов. (Ответ дайте в байтах.)

# I = pixels  * i
# Colors = 2 ** i
'''
symbols1 = 2  # pixels
alphabet1 = 18  # Colors
i1 = 5

symbols2 = 8
alphabet2 = 10
i2 = 4

bit = symbols2 * i2 + symbols1 * i1  # I
print(bit / 8)
byte = 6

print(25 * byte)
'''
# Ответ: 150


# Тип 17 №
# 40733
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3 и хотя бы один из двух элементов
# меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if i % 2 == 0]
sred = sum(A) / len(A)  # среднего арифметического всех чётных элементов последовательности
count = 0
maxi = -99999999
for i in range(len(M) - 1):
    if M[i] % 3 == 0 or M[i+1] % 3 == 0:
        if M[i] < sred or M[i+1] < sred:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)


c = 0
mn = 0
m = [int(i) for i in open('17.txt')]
a = [i for i in m if i % 2 == 0]
sum = sum(a)/len(a)
for i in range(len(m) - 1):
    if (m[i] % 3 == 0 or m[i + 1] % 3 == 0) and (m[i] < sum or m[i + 1] < sum):
        c += 1
        if (m[i] + m[i + 1]) > mn:
            mn = (m[i] + m[i + 1])
print(c, mn)
'''

'''
f = open('17.txt').readlines()
for i in range(len(f)):
    f[i] = f[i][:-1]
    f[i] = int(f[i])
for i in range(len(f) - 3):
    s = (f[i] + f[i + 1] + f[i + 2] + f[i + 3]) / 4
    if (f[i] % 3 == 0 or f[i + 1] % 3 == 0) and (f[i] < s or f[i + 1] < s):
        c += 1
    if f[i] + f[i + 1] > mn or f[i + 2] + f[i + 3] > mn:
        mn = f[i] + f[i + 1]
print(mn, c)
'''
# 19795 2481

# 19, 20, 21
'''
def f(x, y, h):
    if x + y >= 69 and 3 == h:
        return 1
    elif x + y < 69 and 3 == h:
        return 0
    elif x + y >= 69 and 3 > h:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)


for x in range(1, 59):
    if f(x, 10, 1) == 1:
        print(x)
        break
'''

# 7
# 20
'''
def f(x, y, h):
    if x + y >= 69 and 4 == h:
        return 1
    elif x + y < 69 and 4 == h:
        return 0
    elif x + y >= 69 and 4 > h:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 3, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)


for x in range(1, 59):
    if f(x, 10, 1) == 1:
        print(x)

'''
# 1619

# 21
'''
def f(x, y, h):
    if x + y >= 69 and (3 == h or h == 5):
        return 1
    elif x + y < 69 and 5 == h:
        return 0
    elif x + y >= 69 and 5 > h:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 3, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)


def f1(x, y, h):
    if x + y >= 69 and 3 == h:
        return 1
    elif x + y < 69 and 3 == h:
        return 0
    elif x + y >= 69 and 3 > h:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, y, h + 1) or f1(x * 3, y, h + 1) or f1(x, y + 1, h + 1) or f1(x, y * 2, h + 1)
        else:
            return f1(x + 1, y, h + 1) and f1(x * 3, y, h + 1) and f1(x, y + 1, h + 1) and f1(x, y * 2, h + 1)


for x in range(1, 59):
    if f(x, 10, 1) == 1:
        print(x)
for x in range(1, 59):
    if f1(x, 10, 1) == 1:
        print(x)

'''
#18

#23
'''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(3, 10)*f(10,12))
'''

'''
def f(x, y):
    if x >= y:
        return x == y
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(3, 10)*f(10,12))
'''
# Ответ: 60

# Тип 24 № 36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# X ZZYOOOOXZZ Y
'''
f = open('24.txt').readline()
M = [len(i) for i in f.split('XZZY')]
print(max(M)+6)

f = open('24.txt').readline()
f = f.replace('XZZY', 'XZZ ZZY')
M = [len(i) for i in f.split()]
print(max(M))
'''


# № 8510 Апробация 17.05 (Уровень: Средний)
# Текстовый файл состоит из символов, обозначающих прописные буквы латинского алфавита.
# Определите максимальное количество идущих подряд символов, среди которых никакие две буквы из
# набора букв N, O и P (с учетом повторений) не записаны подряд.
# Для выполнения этого задания следует написать программу.
'''
import itertools
pair = []
for s in itertools.product('NOP', repeat=2):
    pair.append(''.join(s))

f = open('24.txt').readline()
for x in pair:
    f = f.replace(x, '* *')
M = [len(i) for i in f.split()]
print(max(M))
'''
# Ответ: 58

'''
c = 0
f = open('24.txt').readline()
f = f.replace('XZZY', '/')
m = []
for i in range(len(f)):
    if f[i] != '/':
        c += 1
    else:
        m.append(c)
        c = 6
print(max(m))
'''
#1713



# endregion Урок: ******************************************************************


# todo: Эмиль = []
# на прошлом уроке: Разбирали вариант с домашки, номера: 2, 5, 8, 15, 11, 17, 23, 24, 25
# на следующем уроке:

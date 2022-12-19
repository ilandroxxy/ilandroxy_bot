
# region Домашка: ******************************************************************

# Тип 5 № 18487

# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится двоичная запись числа N.
# 2. Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
# 3. Полученное число переводится в десятичную запись и выводится на экран.
# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 13?


# Вариант 1
'''
for n in range(100, 0, -1):
    s = bin(n)[2:]
    s = s[::-1]
    r = int(s, 2)
    if r == 13:
        print(n)
        break
'''
# Ответ: 88

# Вариант 2 через списки
import fileinput

'''
for n in range(1, 100):
    temp = n
    N = []
    while n > 0:
        N.append(n % 2)
        n //= 2
    N.reverse()

    N.reverse()

    res = 0
    N.reverse()
    for i in range(0, len(N)):
        res += N[i] * 2 ** i

    if res == 13:
        print(temp)
'''
# Ответ: 88

# Вариант 3
'''
def systems(x, n):
    alphabet = '0123456789abcdefgh'
    N = []
    while x > 0:
        N.append(alphabet[x % n])
        x //= n
    N.reverse()
    result = ''.join(N)
    return result

for n in range(100, 0, -1):
    s = systems(n, 2)
    s = s[::-1]
    r = int(s, 2)
    if r == 13:
        print(n)
        break
'''
# Ответ: 88

# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************

# Тип 15 № 8666

# На числовой прямой даны два отрезка: P = [25; 50] и Q = [32; 47].
# Укажите наибольшую возможную длину промежутка A,
# для которого формула
# (¬ (x  принадлежит  A) → (x  принадлежит  P)) → ((x  принадлежит  A) → (x  принадлежит  Q))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

# Вариант 2
'''
def F(x):
    P = 25 <= x <= 50
    Q = 32 <= x <= 47
    A = a1 <= x <= a2
    return ((not A) <= P) <= (A <= Q)

L = [i/4 for i in range(10*4, 60*4)]

M = []
for a1 in L:
    for a2 in L:
        if all(F(x) for x in L) == True:
            M.append(a2-a1)
print(max(M))
'''
# Ответ: 15

# Вариант 1
'''
M = []
for a1 in range(0, 100):
    for a2 in range(0, 100):
        flag = True
        for x in range(0, 1000):
            if not((not(a1 <= x <= a2)) <= (25 <= x <= 50)) <= ((a1<= x <= a2) <= (32 <= x <= 47)):
                flag = False
                break
        if flag == True:
            M.append(a2 - a1)
print(max(M))
'''
# Ответ: 15


# Тип 15 № 34542
# На числовой прямой даны два отрезка: P = [1, 39] и Q = [23, 58].
# Какова наибольшая возможная длина интервала A, что логическое выражение
#
# ((x ∈ P) → ¬(x ∈ Q)) → ¬(x ∈ А)
#
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P <= (not Q)) <= (not A)

L = [i/4 for i in range(1*4, 70*4)]

M = []
for a1 in L:
    for a2 in L:
        if all(F(x) for x in L) == True:
            M.append(a2-a1)
print(max(M))
'''
# Ответ: 16


# Тип 15 № 34544
# На числовой прямой даны два отрезка: P = [10, 39] и Q = [23, 58].
# Какова наименьшая возможная длина интервала A, что формула
#
# ((x ∈ P) ∧ (x ∈ Q)) → ((x ∈ Q) ∧ (x ∈ A ))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x):
    P = 10 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P and Q) <= (Q and A)

L = [i/4 for i in range(1*4, 70*4)]

M = []
for a1 in L:
    for a2 in L:
        if all(F(x) for x in L) == True:
            M.append(a2-a1)
print(min(M))
'''
# Ответ: 16

# Тип 15 № 40731 Добавить в вариант
# На числовой прямой даны два отрезка: P=[19;84] и Q=[4;51].
# Укажите наименьшую возможную длину такого отрезка A, для которого формула
#
# (x∈Q)→(¬(x∈P)→¬((x∈Q)∧¬(x∈A)))
#
# тождественно истинна (т. е. принимает значение 1 при любом значении переменной х).

'''
def F(x):
    P = 19 <= x <= 84
    Q = 4 <= x <= 51
    A = a1 <= x <= a2
    return Q <= ((not P) <= (not(Q and (not A))))

L = [i/4 for i in range(1*4, 90*4)]

M = []
for a1 in L:
    for a2 in L:
        if all(F(x) for x in L) == True:
            M.append(a2-a1)
print(min(M))
'''
# Ответ: 15 округляем вверх



# № 3156
'''
# Элементами множеств А, P и Q являются натуральные числа, причём P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# и Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}. Известно, что выражение
#
# ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
#
# истинно (т. е. принимает значение 1) при любом значении переменной х.
# Определите наибольшее возможное количество элементов множества A.

a = set(range(1, 1000))

def F(x):
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    A = x in a
    return (A <= P) and (Q <= (not A))  # ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))

for x in range(1, 1000):
    if F(x) == False:
        a.remove(x)

print(a, len(a))
'''
# Ответ: 8



# № 1409
# Элементами множеств А, P, Q, R являются натуральные числа, причём P={2,4,6,8,10,12,14,16,18,20},
# Q={3,6,9,12,15,18,21,24,27,30}, R={12,24,36,48,60}. Известно, что выражение
#
# (x ∉ A) → (((x ∈ P) ∧ (x ∈ Q)) → (x ∈ R))
#
# истинно (т.е. принимает значение 1 при любом значении переменной х.
# Определите наименьшее возможное произведение элементов в множестве A.
'''
a = set()

def F(x):
    P = x in {2,4,6,8,10,12,14,16,18,20}
    Q = x in {3,6,9,12,15,18,21,24,27,30}
    R  = x in {12,24,36,48,60}
    A = x in a
    return (not A) <= ((P and Q) <= R)

for x in range(1, 1000):
    if F(x) == False:
        a.add(x)

print(a)
print(18 * 6)
'''
# Ответ: 108

# Теория для 17 номера
'''
M = [1, 2, 3, 4, 5]

# Тип 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45

for i in range(0, len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print('\n')

# Тип 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345

for i in range(0, len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')
print('\n')

# Тип 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()
'''


# Тип 17 № 47014
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых один из двух элементов делится на 5,
# а другой меньше среднего арифметического всех нечётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt')
M = [int(i) for i in f]

summ = 0
kol = 0
for x in M:
    if x % 2 != 0:
        summ += x
        kol += 1
sred = summ / kol  # среднего арифметического всех нечётных элементов последовательности

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 5 == 0 and M[i+1] < sred) or (M[i] < sred and M[i+1] % 5 == 0):
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 1061 14847


# Тип 17 № 39246
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 5 == 0 or M[i+1] % 5 == 0) and (M[i] + M[i+1]) % 7 == 0:
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 308 18893


# Тип 17 № 39764
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём тройкой три идущих подряд элемента последовательности.
# Определите количество троек чисел таких, которые могут являться сторонами прямоугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек, а затем — максимальную сумму элементов таких троек.
# Если таких троек не найдётся — следует вывести 0.

f = open('17.txt')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)-2):
    A = sorted([M[i], M[i+1], M[i+2]])
    if A[0]**2 + A[1] ** 2 == A[2] ** 2:
        count += 1
        maxi = max(maxi, M[i] + M[i+1] + M[i+2])
print(count, maxi)
'''
# Ответ: 0 0



# Тип 17 № 37357
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 8, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 8 == 0:
            count += 1
            maxi = max(maxi, M[i] + M[j])
print(count, maxi)
'''
# Ответ: 6243772 19992


# Тип 17 № 37370
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 60 и хотя бы один из элементов кратен 15, затем максимальную из разностей элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] - M[j]) % 60 == 0 and (M[i] % 15 == 0 or M[j] % 15 == 0):
            count += 1
            maxi = max(maxi, M[i] - M[j])
print(count, maxi)
'''
# Ответ: 63517 9960

# Как открывать .txt файлы
'''
file = open('17.txt', 'r')
file.close()  # по хорошему, надо файлы закрывать после использования

# самое идеальное написание, работы с файлами
with open('17.txt', 'r') as file:
    M = [int(i) for i in file]
    

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] - M[j]) % 60 == 0 and (M[i] % 15 == 0 or M[j] % 15 == 0):
            count += 1
            maxi = max(maxi, M[i] - M[j])
print(count, maxi)
'''
# endregion Урок: ******************************************************************




# todo: Валерия = [2, 5, 6, 8, 12, 14+, 15+, 16, 17, 23, 25], на следующем уроке:

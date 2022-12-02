
# region Домашка: **********************************************************

# Тип 15 № 11119
'''
# На числовой прямой даны два отрезка: P = [20, 50] и Q = [30,65]. Отрезок A таков, что формул
#
# ¬(x ∈ A) → ((x ∈ P) →¬ (x ∈ Q))
#
# истинна при любом значении переменной x. Какова наименьшая возможная длина отрезка A?


def F(a1, a2, x):
    return ((not(a1 <= x <= a2)) <= ((20 <= x <= 50) <= (not(30 <= x <= 65))))

M = []
for a1 in range(1, 100):
    for a2 in range(a1+1, 100):
        flag= True
        for x in range(1, 1000):
            if F(a1, a2, x) == False:
                flag = False
                break
        if flag == True:
            M.append(a2-a1)

print(min(M))
'''



# Тип 15 № 35904
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
#
# ДЕЛ(A, 40) ∧ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
def F(x, A):
    return (A % 40 == 0) and ((780 % x == 0) <=  ((A % x != 0) <= (180 % x)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(F(x, A)):
            flag = False
            break
    if flag == True:
        print(A)
        break
# Ответ: 120
'''

# Тип 15 № 33094
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наибольшего натурального числа А формула
#
# (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
def F(x, A):
    return (A < 50) and ((x % A != 0) <= ((x % 10 ==  0) <= (x % 18 != 0)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(F(x, A)):
            flag = False
            break
    if flag == True:
        print(A)
# Ответ: 45
'''



# Тип 15 № 34510
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)
#
# тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''
def F(x, A):
    return ((x & 25 != 0) <=  ((x & 9 == 0) <= (x & A != 0)))
for A in range(0, 10000):
    flag = True
    for x in range(0, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
# Ответ: 16
'''

# Тип 12 № 15630
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из одной единицы и 75 стоящих справа от нее нулей?
# В ответе запишите сколько нулей будет в конечной строке.
#
# НАЧАЛО
# ПОКА нашлось (10) ИЛИ нашлось (1)
# ЕСЛИ нашлось (10)
# ТО заменить (10, 001)
# ИНАЧЕ заменить (1, 00)
# КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
'''
s = '1' + '0' * 75
while '10' in s or '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    else:
        s = s.replace('1', '00', 1)
print(s.count('0'))
# Ответ: 152
'''

# Тип 8 № 9361
# В качестве кодовых слов Игорь использует 5-буквенные слова, в которых есть только буквы П, И, Р, причём буква П появляется ровно 1 раз.
# Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не встречаться совсем.
# Сколько различных кодовых слов может использовать Игорь?
'''
count = 0
s = 'ПИР'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('П') == 1:
                        print(temp)
                        count += 1
print(count)
# Ответ: 80
'''


# endregion Домашка: **********************************************************


# region Урок: **********************************************************

'''
M = [1, 2, 3, 4, 5]

# Тип 1: Назовём парой два идущих подряд элемента последовательности.
# Пары: 12 23 34 45

for i in range(0, len(M)-1):
    print(M[i], M[i+1], end=', ')

print()
# Тип 2: В данной задаче под парой подразумевается два различных элемента последовательности.
# Пары: 12 13 14 15
# Пары: 23 24 25
# Пары: 34 35
# Пары: 45

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(M[i], M[j], end=', ')
'''


# Тип 17 № 40992
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 5
# и хотя бы один из двух элементов меньше среднего арифметического всех элементов последовательности, значение которых нечетно.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt')
M = [int(i) for i in f]

summ = 0
count = 0
for x in M:
    if x % 2 != 0:
        summ += x
        count += 1
sred = summ / count  # среднего арифметического всех элементов последовательности, значение которых нечетно


kol = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 5 == 0 or M[i+1] % 5 == 0) and (M[i] < sred or M[i+1] < sred):
        kol += 1

        # maxi = max(maxi, M[i] + M[i+1])

        if maxi < M[i] + M[i+1]:
            maxi = M[i] + M[i+1]
print(kol, maxi)
'''
# Ответ: 1531 14932


# Тип 17 № 38951
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3, а их сумма делится на 5.
# В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар.

# Вариант 2
M = [int(i) for i in open('17.txt')]

maxi, count = 0, 0
for i in range(0, len(M)-1):
    if (M[i] % 3 == 0 or M[i+1] % 3 == 0):
        if (M[i] + M[i+1]) % 5 == 0:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)

# Ответ: 635 19730

# Вариант 1
f = open('17.txt')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 3 == 0 or M[i+1] % 3 == 0) and (M[i] + M[i+1]) % 5 == 0:
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 635 19730



# Тип 17 № 37360
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 120,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

M = [int(i) for i in open('17.txt')]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 120 == 0:
            count += 1
            maxi = max(maxi, M[i] + M[j])
print(count, maxi)
'''
# Ответ: 414830 19920



# Тип 17 № 37372
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 45 и хотя бы один из элементов кратен 18, затем максимальную из разностей элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.

M = [int(i) for i in open('17.txt')]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] - M[j]) % 45 == 0:
            if M[i] % 18 == 0 or M[j] % 18 == 0:
                count += 1
                maxi = max(maxi, M[i] - M[j])
print(count, maxi)
'''
# Ответ: 92471 9945


# Тип 17 № 39763
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. 
# Назовём тройкой три идущих подряд элемента последовательности.
# Определите количество троек чисел таких, которые могут являться сторонами остроугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек, а затем — максимальную сумму элементов таких троек.
# Если таких троек не найдётся — следует вывести 0 0.


M = [int(i) for i in open('17.txt')]

count = 0
MaxSum = 0
for i in range(0, len(M)-2):
    maxi = max(M[i], M[i+1], M[i+2])
    mini = min(M[i], M[i + 1], M[i + 2])
    sred = (M[i] + M[i+1] + M[i+2]) - (maxi + mini)

    if maxi ** 2 < (sred ** 2 + mini ** 2):
        count += 1
        MaxSum = max(MaxSum, M[i] + M[i+1] + M[i+2])
print(count, MaxSum)
'''
# Ответ: 1175 29451





# endregion Урок: **********************************************************


# todo: Стася = [2, 5, 6, 8, 12, 14+, 15, 16, 23], на следующем уроке: Решаем 17 номер



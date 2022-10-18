
#todo: новый тип задач из демоверсии: Тип 14 № 47218

# region Тип 14 № 18444
'''
# Сколько единиц содержится в двоичной записи значения выражения: 4**16 + 2**36 - 8?
x = 4**16 + 2**36 - 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M, M.count(1))
'''
# Ответ: 30
# endregion Тип 14 № 18444

# region Тип 14 № 25846
'''
#Значение арифметического выражения: 9**8·3**20 − 3**10 − 3— записали в системе счисления с основанием 3.
# Сколько цифр 2 содержится в этой записи?
x = 9 ** 8 * 3**20 - 3**10 - 3
N = []
while x > 0:
    N.append(x % 3)
    x //= 3
    N.reverse()
print(N.count(2))
'''
# Ответ: 34
# endregion Тип 14 № 25846

# region Тип 14 № 38948
"""
# Значение выражения 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49 
# записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?
x = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
print(x)
M = []
while x > 0:
    M.append(x % 16)  # сохраняем остаток от деления
    x //= 16  # делим целочисленно, чтобы двигать процесс
    # x = x // 16
M.reverse()
print(M)
M = set(M)
print(M, len(M))
"""
# Ответ: 5
# endregion Тип 14 № 38948

# region Тип 14 № 35472
"""
# Значение выражения 729**7 + 3**16 − 18 записали в системе счисления с основанием 9.
# Сколько раз в этой записи встречается цифра 0?

x = 729**7 + 3**16 - 18
M = []
while x > 0:
    M.append(x % 9)
    x //= 9
M.reverse()
print(M, M.count(0))
"""
# Ответ: 14
# endregion Тип 14 № 35472

# region Тип 14 № 9367
"""
# Значение арифметического выражения: 9**8 + 3**5 – 9 – записали в системе счисления с основанием 3.
# Сколько цифр «2» содержится в этой записи?

x = 9**8 + 3**5 - 9
M = []
while x > 0:
    M.append(x % 3)
    x //= 3
M.reverse()
print(M, M.count(2))
"""
# Ответ: 3
# endregion Тип 14 № 9367

# region Тип 14 № 47011
'''
# Значение выражения 3*343**8 + 5*49**12 + 7**15 - 49 записали
# в системе счисления с основанием 7 без незначащих нулей.
# Какая цифра чаще всего встречается в этой записи?

x = 3*343**8 + 5*49**12 + 7**15 - 49
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M)

A = {}
for i in M:
    A[i] = M.count(i)
print(A)
'''
# Ответ: 6
# endregion Тип 14 № 47011

# region Тип 14 № 7460
"""
# Сколько единиц содержится в двоичной записи значения выражения: 4**2014 + 2**2015 − 8?
x = 4**2014 + 2**2015 - 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M.count(1))
"""
# Ответ: 2013
# endregion Тип 14 № 7460

# region Тип 14 № 27545
"""
# Значение выражения 49**7*7**20 − 7**8 − 28 записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?

x = 49**7*7**20 - 7**8 - 28
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M.count(6))
"""
# Ответ: 31
# endregion Тип 14 № 27545

# region Тип 14 № 39243
"""
# Значение выражения 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?

x = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M)

# вариант 1
A = []
for i in M:
    if i not in A:
        A.append(i)
print(A, len(A))

# вариант 2
A = set(M)
print(A, len(A))
"""
# Ответ: 6
# endregion Тип 14 № 39243

# region Тип 14 № 47218
"""
# Операнды арифметического выражения записаны в системе счисления с основанием 15:
#
# 123x515 + 1x23315
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 14 и укажите
# его в ответе в десятичной системе счисления. 
# Основание системы счисления в ответе указывать не нужно.

for num in range(15):
    A = list(reversed([1, 2, 3, num, 5]))
    B = list(reversed([1, num, 2, 3, 3]))

    sum1, sum2 = 0, 0
    for i in range(5):
        sum1 += A[i] * 15 ** i
        sum2 += B[i] * 15 ** i
    print(A, B )
    if (sum1 + sum2) % 14 == 0:
        print((sum1 + sum2)// 14)
        break
"""
# Ответ: 8767
# endregion Тип 14 № 47218



# Старые задачи с 2021-2022 года:

# region Задания 14 № 4938
"""
# Решите уравнение 100_7 + x = 200_5.
# Ответ запишите в шестнадцатеричной системе (основание системы счисления в ответе писать не нужно).

M = [1, 0, 0]
M.reverse()
m = 0
for i in range(0, len(M)):
    m += M[i] * 7 ** i


N = [2, 0, 0]
N.reverse()
n = 0
for i in range(0, len(N)):
    n += N[i] * 5 ** i

x = n - m

A = []
while x > 0:
    A.append(x % 16)
    x //= 16
A.reverse()
print(A)
"""
# Ответ: 1
# endregion Задания 14 № 4938

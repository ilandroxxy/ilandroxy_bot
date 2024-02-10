# region Домашка: ******************************************************************

# Тип 14 №48380
# Числа M и N записаны в системе счисления с основанием 12 соответственно.
#
# M = 49x2612, N = 49x7012
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита двенадцатеричной системы счисления.
# Определите наименьшее значение натурального числа A, при котором существует такой x, что M + A кратно N.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for A in range(1, 1000):
    for x in alphabet[:12]:
        M = int(f'49{x}26', 12)
        N = int(f'49{x}70', 12)
        if (A + M) % N == 0:
            R.append(A)
print(min(R))
'''
# Ответ: 54

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 5 №52176
# Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Если сумма цифр десятичной записи заданного числа нечётна,
# то в конец двоичной записи дописывается 1, если чётна — 0.
# 3−4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
# 5. Результатом работы алгоритма становится десятичная запись полученного числа R.

# Определите наименьшее возможное значение R>2054, которое может получиться в результате работы алгоритма.
'''
M = []
for n in range(1, 1000):  # 125
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.
    for i in range(3):  # 3−4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
        summa = sum([int(x) for x in str(int(s, 2))])  # сумма цифр десятичной записи заданного числа
        if summa % 2 != 0:  # 2. если summa нечетна
            s = s + '1'  # в конец двоичной записи дописывается 1
        else:  # если чётна (иначе)
            s = s + '0'  # в конец двоичной записи дописывается 0
    r = int(s, 2)  # 5. Результатом работы алгоритма становится десятичная запись полученного числа R.
    if r > 2054:
        M.append(r)
print(min(M))
'''
# Ответ: 2057


# Тип 5 №18554
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится двоичная запись числа N без ведущих нулей.
# 2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица.
# Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
# 3. Полученное число переводится в десятичную запись и выводится на экран.

# Какое наименьшее число, превышающее 80, может получиться в результате работы автомата?
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N без ведущих нулей.
    if s.count('1') > s.count('0'):  # 2. Если в полученной записи единиц больше, чем нулей
        s = s + '1'  # то справа приписывается единица.
    else:  # Если нулей больше или нулей и единиц поровну
        s = s + '0'  # то справа приписывается ноль.
    r = int(s, 2)  # 3. Полученное число переводится в десятичную запись и выводится на экран.
    if r > 80:
        M.append(r)

print(min(M))
'''


# Тип 5 №18434
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2 дописывается в конец числа
# б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы её цифр на 2.
# Полученная таким образом запись является двоичной записью искомого числа R.
#
# Укажите минимальное число R, которое превышает число 55
# и может являться результатом работы данного алгоритма.
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 55:
        M.append(r)

print(min(M))
'''
# Ответ: 58


# Тип 5 №33750
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Вместо последней (самой правой) двоичной цифры дважды записывается вторая слева цифра двоичной записи.
# 3. Результат переводится в десятичную систему.

# При каком наименьшем числе N в результате работы алгоритма получится R>76?
# В ответе запишите это число в десятичной системе счисления.
'''
M = []
for n in range(2, 1000):
    s = bin(n)[2:]
    s = s[:-1] + s[1] + s[1]
    r = int(s, 2)
    if r > 76:
        M.append(n)

print(min(M))
'''


# Тип 5 №18487
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится двоичная запись числа N.
# 2. Запись «переворачивается», то есть читается справа налево.
# Если при этом появляются ведущие нули, они отбрасываются.
# 3. Полученное число переводится в десятичную запись и выводится на экран.

# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 13?
'''
M = []
for n in range(1, 100):
    s = bin(n)[2:]
    s = s[::-1]
    r = int(s, 2)
    if r == 13:
        M.append(n)

print(max(M))
'''

# endregion Урок: ******************************************************************


# Тимур = [2.1, 6.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:

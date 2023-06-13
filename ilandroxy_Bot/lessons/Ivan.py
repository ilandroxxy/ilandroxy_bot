# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 5 № 8094
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа).
# Например, запись 11100 преобразуется в запись 111001;
# б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы цифр на 2.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в
# записи исходного числа N) является двоичной записью искомого числа R.
#
# Укажите минимальное число R, которое превышает 43 и может
# являться результатом работы алгоритма. В ответе это число запишите в десятичной системе.
'''
R = []
for n in range(1, 1000):
    s = bin(n)[2:]
    for i in range(2):
        summ = s.count('1')
        s += str(summ % 2)
    r = int(s, 2)
    if r > 43:
        R.append(r)
print(min(R))
'''
# Ответ: 46

# № 8511 Апробация 17.05 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.

# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# соответствующие маске 12??15*6, делящиеся на 253 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа
# в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 253.
# Количество строк в таблице для ответа избыточно.

# Вариант 1
'''
import itertools
M = []
for l in range(0, 1+1):
    for s in itertools.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for x in '0123456789':
    for y in '0123456789':
        for z in M:     # перебираем маску "*"
            A = int(f'12{x}{y}15{z}6')
            if A < 10**8:
                if A % 253 == 0:
                    R.append([A, A // 253])

for x in sorted(R):
    print(*x)
'''

# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# соответствующие маске 12??15*6, делящиеся на 253 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа
# в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 253.
# Количество строк в таблице для ответа избыточно.
'''
from fnmatch import *
for x in range(0, 10**8):
    if fnmatch(str(x), '12??15*6'):  # соответствующие маске 12??15*6
        if x % 253 == 0:  # делящиеся на 253 без остатка
            print(x, x // 253)
'''

'''
from fnmatch import *
for x in range(253, 10**8, 253):
    if fnmatch(str(x), '12??15*6'):  # соответствующие маске 12??15*6
        print(x, x // 253)
'''


# № 6210 (Уровень: Средний)
# (Н. Сафронов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Найдите все натуральные числа, не превосходящие 10**7, для которых выполняются одновременно все условия:

# • соответствуют маске *2?2*;
# • являются палиндромами;
# • делятся на число 53 без остатка;
# • количество делителей больше 30.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — сумму делителей.
'''
from fnmatch import *
for x in range(53, 10**7, 53):
    if fnmatch(str(x), '*2?2*'):
        if str(x) == str(x)[::-1]:  # • являются палиндромами;
            divisors = set()
            for d in range(1, int(x**0.5)+1):
                if x % d == 0:
                    divisors.add(d)
                    divisors.add(x // d)
            if len(divisors) > 30:  # • являются палиндромами;
                print(x, sum(divisors))
'''
# 212212 508032
# 2527252 5588352
# 4282824 13789440
# 4626264 11787120
# 8125218 19595520
# 8824288 19908504



# № 5889 Danov2301 (Уровень: Базовый)
# (А.Богданов) Найдите девятизначные числа, отвечающих маске «1*1*1?»,
# которые делятся на 19, 6 и 2023.
# В ответе запишите пять наибольших найденных чисел в порядке возрастания.
'''
x = 100_002_023
while x % 2023 != 0:
    x -= 1
print(x)
'''

'''
from fnmatch import *
for x in range(100000936, 1_000_000_000, 2023):
    if fnmatch(str(x), '1*1*1?'):
        if x % 19 == 0 and x % 6 == 0 and x % 2023 == 0:
            print(x)
'''
# Показать ответ
# 174119610
# 181499514
# 183575112
# 195106212
# 197181810


#
# № 5678 Вариант 09.01.23 (Уровень: Средний)
# (М. Ишимов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# · символ «?» означает ровно одну произвольную цифру;
# · символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# которые делятся на сумму нечётных цифр числа и соответствующие маске 124*5*79.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – сумму всех цифр этого числа.
'''
from fnmatch import *
for x in range(124579, 10**8):  # 124*5*79
    if fnmatch(str(x), '124*5*79'):
        nechet = [int(i) for i in str(x) if int(i) % 2 != 0]
        if x % sum(nechet) == 0:
            print(x, sum([int(i) for i in str(x)]))
'''
# Показать ответ
# 1249579 37
# 12409579 37
# 12452979 39
# 12456179 35


# № 5476 (Уровень: Средний)
# (В. Петров) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**9, найдите все числа,
# семеричная запись которых соответствует маске ?213*5664, делящиеся на 33310 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 33310.  Все числа в ответе указывать в десятичной системе счисления.

# Показать ответ
# 24888420 74740
# 371885742 1116774
# 654120891 1964327
# 937155573 2814281

from fnmatch import *
for x in range(333,10**9,333):
    if fnmatch(str(x), '?213*5664'):
        print(x,x // 333)

# endregion Урок: ******************************************************************************


# todo: Иван = [2, 3, 6, 7, 8, 10, 11, 12, 13, 14+, 15+, 16, 17, 19-21, 23]
# на прошлом уроке: Прорешали два вопроса по 5 номеру и разобрали 25 номера с новым решением через fnmatch
# на следующем уроке:
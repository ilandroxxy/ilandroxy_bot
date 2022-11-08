# region Домашка:  ******************************************************************************


S = {1, 2, 3}  # тип данных множество set()
D = {1: 'one', 2: 'two', 3: 'three'}   # тип данных словарь dict()

S = set()  # пустое множество

D = {}  # создает пустой словарь
D = dict()

T = ()
T = tuple()  # пустой кортеж

#список кубов
'''
lst = list()  # пустой список
lst = []  # пустой список
for _ in range(int(input())):
    lst.append(int(input()) ** 3)
print(lst)
'''

'''
#списочное выражение 1
n = int(input())
x = [i**2 for i in range(1, n+1)]
print(*x, sep='\n')

print(*[i**2 for i in range(1, int(input())+1)], sep='\n')
'''


#Google search 1
'''
n = int(input('n: '))
a = []
for _ in range(n):
    a.append(input('Введите строку текста: '))
search = input('Введите поисковой запрос: ')

for x in a:
    if search.lower() in x.lower():
        print(x)
'''


# Negativis, Zeros and Pozities
'''
n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()
print(*A, sep="\n")
'''

'''
n = int(input())
A = [int(input()) for _ in range(n)]
N = []
Z = []
P = []
for i in A:
    if i < 0:
        N.append(i)
    elif i == 0:
        Z.append(i)
    else:
        P.append(i)
B = N + Z + P
for b in B:
    print(b, '\n')
'''

# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************

# Задача № 2197 (М.В. Кузнецова)
'''
# Значение арифметического выражения: 32**30 + 8**60 – 32 записали в системе счисления с основанием 4.
# Сколько цифр «3» в этой записи?

x = 32**30 + 8**60 - 32
M = []
while x > 0:
    M.append(x % 4)
    x //= 4
M.reverse()
print(M.count(3))
'''
# Ответ: 72


# Задача № 5497 (В. Шубинкин)
'''
# Числа M и N записаны в системах счисления с основаниями 15 и 13 соответственно.
# M = 2y23x5_15, N = 67x9y_13
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите наименьшее значение натурального числа A, при котором существуют такие x, y, что M + A кратно N.

for A in range(1, 100000):
    for x in '0123456789abc':
        for y in '0123456789abc':
            M = int(f'2{y}23{x}5', 15)
            N = int(f'67{x}9{y}', 13)

            if (M + A) % N == 0:
                print(A)
                exit()
'''
# Ответ: 1535


# Тип 5 № 15622
'''
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу: складываются все цифры двоичной записи, если
# а) сумма нечетная к числу дописывается 11,
# б) сумма четная, дописывается 00.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является
# двоичной записью искомого числа R. Укажите такое наименьшее число R, которое превышает 114 и может
# являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе счисления.

M = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.

    summ = s.count('1')
    if summ % 2 != 0:
        s += '11'  # а) сумма нечетная к числу дописывается 11,
    else:
        s += '00'  # б) сумма четная, дописывается 00.

    r = int(s, 2)  # В ответе это число запишите в десятичной системе счисления.

    if r > 114:
       M.append(r)

print(min(M))
'''
# Ответ: 115


# Тип 5 № 18075
''' 
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) находится остаток от деления на 2 суммы двоичных разрядов N, полученный результат дописывается в конец двоичной последовательности N.
# б) пункт а повторяется для вновь полученной последовательности.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
# Укажите минимальное число R, которое превышает 123 и может являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе.

M = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.

    for _ in range(2):
        summ = s.count('1')
        s += str(summ % 2)

    r = int(s, 2)  # В ответе это число запишите в десятичной системе счисления.

    if r > 123:
       M.append(r)

print(min(M))


# Вариант 2
M = []
for n in range(1, 1000):
    A = []
    while n > 0:
        A.append(n % 2)
        n //= 2
    A.reverse()

    for _ in range(2):
        A.append(sum(A) % 2)

    r = 0
    A.reverse()
    for i in range(0, len(A)):
        r += A[i] * 2 ** i

    if r > 123:
       M.append(r)  

print(min(M))
'''
# Ответ: 126.


# endregion Урок:  ******************************************************************************


# todo: Екатерина = [2, 14, 5], на следующем уроке: Повторяем 5 номер если нужно, Разбираем 8 номер


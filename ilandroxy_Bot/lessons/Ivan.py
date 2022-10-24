
# region Домашка

# endregion Домашка


# region Урок
# Тип 14 № 27545
'''
# Значение выражения 49**7*7**20 − 7**8 − 28 записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?
x = 49**7*7**20 - 7**8 - 28
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M.count(6))
'''
# Ответ: 31



# Тип 14 № 47218
'''
# Операнды арифметического выражения записаны в системе счисления с основанием 15:
#
# 123x5_15 + 1x233_15
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
# Для найденного значения x вычислите частное от деления значения арифметического
# выражения на 14 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.

for x in range(0, 15):
    A = [1, 2, 3, x, 5]
    A.reverse()
    a = 0
    for i in range(0, len(A)):
        a += A[i] * 15 ** i

    B = [1, x, 2, 3, 3]
    B.reverse()
    b = 0
    for i in range(0, len(B)):
        b += B[i] * 15 ** i

    if (a + b) % 14 == 0:
        print((a + b) // 14)
        break
'''
# Ответ: 8767




# Тип 14 № 27385
'''
# Значение выражения 343**5 + 343**4 + 49**6 − 7**13 − 21 записали в системе счисления с основанием 7.
# Сколько различных цифр содержит эта запись?
x = 343**5 + 343**4 + 49**6 - 7**13 - 21
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M)
B = set(M)
print(len(B), B)

A = {}
for x in M:
    A[x] = M.count(x)
print(A)
'''


# Тип 5 № 37140
# Автомат обрабатывает натуральное число N по следующему алгоритму.
# 1. Строится двоичная запись числа N.
# 2. Если N четное, то в конец полученной записи (справа) дописывается 0, в начало — 1; если N — нечётное в конец и начало дописывается по две единицы.
# 3. Результат переводится в десятичную систему и выводится на экран.
#
# Пример. Дано число N=13. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 1101.
# 2. Число нечетное, следовательно, по две единицы по краям — 11110111.
# 3. На экран выводится число 247.
#
# Укажите наименьшее число, большее 52, которое может является результатом работы автомата.

'''
A = []
for n in range(1, 1000):
    x = n

    M = []
    while x > 0:
        M.append(x % 2)  # 1. Строится двоичная запись числа N.
        x //= 2
    M.reverse()

    if n % 2 == 0:  # 2. Если N четное, то в конец полученной записи (справа) дописывается 0, в начало — 1;
        M.append(0)
        M.reverse()
        M.append(1)
        M.reverse()
    else:          # 2.  если N — нечётное в конец и начало дописывается по две единицы.
        M.append(1)
        M.append(1)
        M.reverse()
        M.append(1)
        M.append(1)
        M.reverse()

    M.reverse()
    r = 0
    for i in range(0, len(M)):  # 3. Результат переводится в десятичную систему и выводится на экран.
        r += M[i] * 2 ** i

    if r > 52:
        A.append(r)
print(min(A))
'''

# Вариант 2
'''
A = []
for n in range(1, 1000):

    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.

    if n % 2 == 0:
        s = '1' + s + '0'  # 2. Если N четное, то в конец полученной записи (справа) дописывается 0, в начало — 1;
    else:
        s = '11' + s + '11'  # 2.  если N — нечётное в конец и начало дописывается по две единицы.

    r = int(s, 2)  # 3. Результат переводится в десятичную систему и выводится на экран.

    if r > 52:
        A.append(r)
print(min(A))
'''





# print(min(4, 5, 63, 46, 543, 5434))



# Тип 5 № 16435
"""
# Автомат обрабатывает натуральное число N > 1 по следующему алгоритму.
#
# 1. Строится двоичная запись числа N.
# 2. Последняя цифра двоичной записи удаляется.
# 3. Если исходное число N было нечётным, в конец записи (справа) дописываются цифры 10, если четным — 01.
# 4. Результат переводится в десятичную систему и выводится на экран.
#
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
# 1. Двоичная запись числа N: 1101.
# 2. Удаляется последняя цифра, новая запись: 110.
# 3. Исходное число нечётно, дописываются цифры 10, новая запись: 11010.
# 4. На экран выводится число 26.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 2017?

for n in range(1, 10000):
    s = bin(n)[2:]

    s = s[:-1]  # 2. Последняя цифра двоичной записи удаляется.

    if n % 2 != 0:
        s += '10'
    else:
        s += '01'

    r = int(s, 2)

    if r == 2017:
        print(n)
"""
# Ответ: 1008




# Тип 5 № 7751
'''
# Автомат получает на вход четырёхзначное число. По этому числу строится новое число по следующим правилам:
#
# 1. Складываются первая и вторая, а также третья и четвёртая цифры исходного числа.
#
# 2. Полученные два числа записываются друг за другом в порядке возрастания (без разделителей).
#
# Пример. Исходное число: 2366. Суммы: 2 + 3 = 5; 6 + 6 = 12.
# Результат: 512.
# Укажите наибольшее число, в результате обработки которого автомат выдаст число 117.

for n in range(9999, 999, -1):
    s = str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[2]) + int(s[3])

    r = str(min(a, b)) + str(max(a, b))

    if r == '117':
        print(n)
        break
'''
# Ответ: 9810



# Тип 5 № 13563
'''
# Автомат получает на вход четырёхзначное десятичное число, в котором все цифры нечётные.
# По этому числу строится новое число по следующим правилам.
#
# 1. Складываются первая и вторая, а также третья и четвёртая цифры.
# 2. Полученные два числа записываются друг за другом в порядке неубывания (без разделителей).
#
# Пример. Исходное число: 7511. Суммы: 7 + 5 = 12; 1 + 1 = 2. Результат: 212.
# Сколько существует чисел, в результате обработки которых автомат выдаст число 616?
def F(s):
    num = '02468'
    for i in num:
        if i in s:
            return False
    return True


count = 0
for n in range(1000, 10000):
    s = str(n)
    if F(s) == True:
        a = int(s[0]) + int(s[1])
        b = int(s[2]) + int(s[3])

        r = str(min(a, b)) + str(max(a, b))

        if r == '616':
            count += 1
print(count)
'''







# Тип 16 № 5682
'''
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n) = 2 при n ≤ 2;
# F(n) = F(n− 1) + 3·F(n − 2) при n > 2.
#
# Чему равно значение функции F(5)? В ответе запишите только натуральное число.


def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return F(n - 1) + 3 * F(n - 2)

print(F(5))
'''
# Ответ: 38
# endregion Урок


# todo: Иван = [2, 13, 14, 5, 16], на следующем уроке: 8, 12 номера












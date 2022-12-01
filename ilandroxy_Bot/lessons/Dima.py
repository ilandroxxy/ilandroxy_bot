
# region Домашка: ******************************************************************************

# 46999
'''
# Логическая функция F задаётся выражением (x ≡ (y → z)) ∧ (¬w → (x ≡ y)).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
# содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности
# функции F соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x == (y <= z)) and ((not(w)) <= (x == y)))
                if F == True:
                    print(x, y, z, w, F)
# ywzx
'''

# 33504
'''
# Логическая функция F задаётся выражением ((x ≡ ¬y) → (y ∧ ¬z)) ∨ (z ∧ ¬w). 
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
# содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции 
# F соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x == (not(y))) <= (y and (not(z)))) or (z and (not(w))))
                if F == False:
                    print(x, y, z, w, F)
# wzxy
'''

# 33472
'''
# Логическая функция F задаётся выражением (w → x) ∧ ((y → z) ≡ (x → y)). 
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, 
# содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции 
# F соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= x) and ((y <= z) == (x <= y)))
                if F == True:
                    print(x, y, z, w, F)
# xzyw
'''

# 45236
'''
# Миша заполнял таблицу истинности логической функции F ¬ (x → w) ∨ (y ≡ z) ∨ y, 
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, 
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(x <= w)) or (y == z)or y)
                if F == False:
                    print(x, y, z, w, F)
# zxwy
'''

# 25832
'''
# Миша заполнял таблицу истинности функции (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w, 
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, 
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x and (not(y))) or (x == z) or (not(w)))
                if F == False:
                    print(x, y, z, w, F)
# wzyx
'''

# 15856
'''
# Сколько единиц содержится в двоичной записи значения выражения: 4^12 + 23^2 − 16.

s = bin(4**12 + 2**32 - 16)
print(s[2:].count('1'))

# 21
'''

# 48391
'''
# Операнды арифметического выражения записаны в системах счисления с основаниями 12 и 14: yAAx 12 + x02y 14. 
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры. 
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 80. 
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 80 
# и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

for x in '0123456789ab':
    for y in '0123456789ab':
        M = int(f'{y}AA{x}', 12)
        N = int(f'{x}02{y}', 14)
        if (M + N) % 80 == 0:
            print((M + N) / 80)
            exit()
# 119
'''


# 18614

# Логическая функция F задаётся выражением ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((w <= (not(x))) == (z <= y)) and (y or w))
                print(x, y, z, w, F)
'''
# xwyz


# endregion Домашка: ******************************************************************************






# region Урок: ******************************************************************************



# Тип 14 № 39243
'''
# Значение выражения 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?

# Вариант 1
x = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M)

A = set(M)
print(A, len(A))

# Вариант 2
x = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
M = set()
while x > 0:
    M.add(x % 16)
    x //= 16
print(sorted(M), len(M))
'''




# Тип 5 № 10309
# Автомат получает на вход пятизначное число. По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая, третья и пятая цифры, а также вторая и четвёртая цифры.
# 2. Полученные два числа записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. Результат: 1016.
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 621.

'''
for n in range(10000, 100000):
    M = [int(i) for i in str(n)]

    a = M[0] + M[2] + M[4]
    b = M[1] + M[3]

    r = str(min(a, b)) + str(max(a, b))

    if r == '621':
        print(n)
        break
'''
# Ответ: 30969



# Тип 5 № 14692
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 1984. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 4 = 12. Удаляется 10. Результат: 1217.
# Укажите наибольшее число, при обработке которого автомат выдаёт результат 613.

'''
for n in range(10000-1, 1000-1, -1):
    M = [int(i) for i in str(n)]

    a = M[0] + M[1]
    b = M[1] + M[2]
    c = M[2] + M[3]

    maxi = max(a, b, c)
    sred = (a + b + c) - (maxi + min(a, b, c))

    r = str(sred) + str(maxi)

    if r == '613':
        print(n)
        break
'''
# Ответ: 9424


# Тип 5 № 35894
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Подсчитывается количество нулей и единиц в полученной записи.
# Если их количество одинаково, в конец записи добавляется её последняя цифра.
# В противном случае в конец записи добавляется та цифра, которая встречается реже.
# 3. Шаг 2 повторяется ещё два раза
# 4. Результат переводится в десятичную систему.
#
# Пример. Дано число N=19. Алгоритм работает следующим образом:
# 1. Двоичная запись числа N: 10011.
# 2. В полученной записи нулей меньше, чем единиц, в конец записи добавляется 0. Новая запись: 100110.
# 3. В текущей записи нулей и единиц поровну, в конец записывается последняя цифра, это 0. Получается 1001100.
# В этой записи единиц меньше, в конец добавляется 1: 10011001.
# 4. Результат работы алгоритма R=153.
#
# При каком наименьшем числе N>104 в результате работы алгоритма получится число, кратное 4?

# Вариант 1
'''
for n in range(104+1, 10000):
    s = bin(n)[2:]

    for _ in range(3):
        if s.count('0') == s.count('1'):
            s += s[-1]
        else:
            if s.count('0') < s.count('1'):
                s += '0'
            else:
                s += '1'

    if int(s, 2) % 4 == 0:
        print(n)
        break
'''


# Вариант 2
'''
for n in range(104+1, 10000):
    temp = n

    N = []
    while n > 0:
        N.append(n % 2)
        n //= 2
    N.reverse()

    for _ in range(3):
        if N.count(0) == N.count(1):
            N.append(N[-1])
        else:
            if N.count(0) < N.count(1):
                N.append(0)
            else:
                N.append(1)

    M = [str(i) for i in N]
    s = ''.join(M)
    r = int(s, 2)

    # r = 0
    # N.reverse()
    # for i in range(0, len(N)):
    #     r += N[i] * 2 ** i

    if r % 4 == 0:
        print(temp)
        break
'''


# Тип 5 № 17370
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится двоичная запись числа N.
# 2. Удаляется первая слева единица и все следующие непосредственно за ней нули.
# Если после этого в числе не остаётся цифр, результат этого действия считается равным нулю.
# 3. Полученное число переводится в десятичную запись.
# 4. Новое число вычитается из исходного, полученная разность выводится на экран.

# Пример. Дано число N = 11. Алгоритм работает следующим образом.
# 1. Двоичная запись числа N: 1011.
# 2. Удаляется первая единица и следующий за ней ноль: 11.
# 3. Десятичное значение полученного числа 3.
# 4. На экран выводится число 11 – 3 = 8.

A = set()
for n in range(100, 3000+1):
    s = bin(n)[2:]

    s = s[1:]  # 2. Удаляется первая слева единица и все следующие непосредственно за ней нули.

    r = int(s, 2)

    A.add(n - r)
print(A, len(A))

print(int('00000001000', 2))
#
#
# Сколько разных значений будет показано на экране автомата при последовательном вводе всех натуральных чисел от 100 до 3000?


# endregion Урок: ******************************************************************************


#todo: Дмитрий = [2, 5, 14+], на следующем уроке: Добить вопросы по 5-тому номеру и теория строк + 8, 12
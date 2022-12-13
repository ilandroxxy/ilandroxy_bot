# region Домашка:  **************************************************

#48383
#Операнды арифметического выражения записаны в системе счисления с основанием 9:
#88x4x_9 + 7x344_9
#В записи чисел переменной x обозначена неизвестная цифра из алфавита девятеричной системы счисления.
#Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 67.
#Для найденного значения x вычислите частное от деления значения арифметического выражения на 67 и укажите его в ответе в десятичной системе счисления.
#Основание системы счисления в ответе указывать не нужно
'''
for x in '012345678':
    a = int(f'88{x}4{x}', 9)
    b = int(f'7{x}344', 9)
    if (a+b) % 67 == 0:
        print((a + b) // 67)
        break
'''
#Ответ: 1597

#48392
#Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 12:
#2y66x_9 + x0y1_12
#В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
#Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 170.
#Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 170 и укажите его в ответе в десятичной системе счисления.
#Основание системы счисления в ответе указывать не нужно.
'''
for x in '012345678':
    for y in '012345678':
        a = int(f'2{y}66{x}', 9)
        b = int(f'{x}0{y}1', 12)
        if (a+b) % 67 == 0:
            print((a+b) // 67)
            break
'''
#Ответ: 403

#Операнды арифметического выражения записаны в системе счисления с основаниями 13 и 17:
#8x7113 + 3xDF17
#В записи чисел переменной x обозначена неизвестная цифра из алфавита десятичной системы счисления.
#Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 197.
#Для найденного значения x вычислите частное от деления значения арифметического выражения на 197 и укажите его в ответе в десятичной системе счисления.
#Основание системы счисления в ответе указывать не нужно.
'''   
for x in '0123456789abc':
    a = int(f'8{x}71', 13)
    b = int(f'3{x}DF', 17)
    if (a+b) % 197 == 0:
         print ((a+b) // 197)
         break
'''
#Ответ: 175

# endregion Домашка: **************************************************




# region Урок:  **************************************************

# Тип 5 № 15128
'''
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 1982. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 2 = 10. Удаляется 10. Результат: 1017.
# Укажите наибольшее число, при обработке которого автомат выдаёт результат 1315.

for n in range(10000-1, 1000-1, -1):
    M = [int(i) for i in str(n)]

    a = M[0] + M[1]
    b = M[1] + M[2]
    c = M[2] + M[3]

    # Вариант 1
    # A = [a, b, c]
    # A.remove(min(a, b, c))

    # r = str(min(A)) + str(max(A))

    # Вариант 2
    maxi = max(a, b, c)
    sred = (a + b + c) - maxi - min(a, b, c)

    r = str(sred) + str(maxi)

    if r == '1315':
        print(n)
        break
'''
# Ответ: 9676



# Тип 5 № 10282
'''
# Автомат получает на вход пятизначное число. По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая, третья и пятая цифры, а также вторая и четвёртая цифры.
# 2. Полученные два числа записываются друг за другом в порядке неубывания без разделителей.

# Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. Результат: 1016.
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 723

for n in range(10000, 100000):
    M = [int(i) for i in str(n)]

    a = M[0] + M[2] + M[4]
    b = M[1] + M[3]

    r = str(min(a, b)) + str(max(a, b))

    if r == '723':
        print(n)
        break
'''
# Ответ: 50979



# Тип 5 № 18434
'''
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.

# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
# б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы её цифр на 2.

# Укажите минимальное число R, которое превышает число 55 и может являться результатом работы данного алгоритма. В ответе это число запишите в десятичной системе счисления.

Result = []
for n in range(1, 100):
    s = bin(n)[2:]  # функция переводящая число из 10-ной в 2-ную (в виде строки)

    for _ in range(2):
        s += str(s.count('1') % 2)

    r = int(s, 2)

    if r > 55:
        Result.append(r)

print(min(Result))
'''
# Ответ: 58



# Тип 5 № 26978
'''
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются разряды по следующему правилу:
# а) если число четное, то к двоичной записи числа в конце дописываются 1 и 0;
# б) если число нечетное, то к двоичной записи числа в конце дописывается 01.
#
# Полученная таким образом запись является двоичной записью искомого числа R.
# Укажите наибольшее число R меньшее 109, которое может получиться после обработки этого алгоритма. В ответе это число запишите в десятичной системе.

Result = []
for n in range(1, 1000):
    s = bin(n)[2:]

    if n % 2 == 0:
        s += '10'
    else:
        s += '01'

    r = int(s, 2)

    if r < 109:
        Result.append(r)
print(max(Result))
'''


# Тип 5 № 28542
'''
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится троичная запись числа N.
# 2. В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3. Результат переводится из троичной системы в десятичную и выводится на экран.
#
# Какое наименьшее четырёхзначное число может появиться на экране в результате работы автомата?

# Универсальная программа замены bin() 
def system(x, n):
    M = []
    while x > 0:
        M.append(str(x % n))
        x //= n
    M.reverse()

    s = ''.join(M)
    return s


for n in range(1, 1000):
    s = system(n, 3)

    s += str(n % 3)

    r = int(s, 3)

    if 1000 <= r < 10000:
        print(r)
        break
'''

# Методы split() и join()
'''
ip = '29.32.43.123'

A = [int(i) for i in ip.split('.')]
print('A: ', A)

M = ip.split('.')
print('M: ', M)

r = '*'.join(M)  # только со списками из строк
print('r: ', r)
'''



# Тип 5 № 47002
'''
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Вычисляется количество единиц, стоящих на чётных местах в двоичной записи числа N без ведущих нулей, и количество нулей, стоящих на нечётных местах.
# Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных двух чисел.
#
# При каком наименьшем N в результате работы алгоритма получится R = 4?

for n in range(1, 100000):
    s = bin(n)[2:]

    count_0 = 0
    count_1 = 0
    for i in range(0, len(s)):
        if (i+1) % 2 == 0 and s[i] == '1':
            count_1 += 1
        if (i+1) % 2 != 0 and s[i] == '0':
            count_0 += 1
    r = abs(count_1 - count_0)
    if r == 4:
        print(n)
        break
'''
# Ответ: 255



# Тип 5 № 29113
'''
# Автомат обрабатывает натуральное число N (128 ≤ N ≤ 255) по следующему алгоритму:
#
# 1. Строится восьмибитная двоичная запись числа N.
# 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3. Полученное число переводится в десятичную запись.
# 4. Из исходного числа вычитается полученное, разность выводится на экран.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 185?

for n in range(128, 255+1):

    s = bin(n)[2:]

    # while len(s) != 8:
    #     s = '0' + s

    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')

    r = int(s, 2)

    res = n - r

    if res == 185:
        print(n)
'''
# Ответ: 220


'''
a = 5
b = 10
print(a, b)

temp = a
a = b
b = temp
print(a, b)

a, b = b, a  # быстрый свап без третьей переменной в Python 
print(a, b)

'''

# endregion Урок:  **************************************************


# todo: Кирилл = [2, 5, 14+], на следующем уроке: Ответить на вопросы по 14 номеру и теории списков/строк. Если вопросов нет, то 5, 8, 12 номера
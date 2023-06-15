# region Домашка:  ******************************************************************************



# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************


# Тип 5 № 7663
# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
# 1. Складываются первая и вторая, а также вторая и третья цифры исходного числа.
# 2. Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
#
# Пример. Исходное число: 348. Суммы: 3 + 4 = 7; 4 + 8 = 12. Результат: 127.
# Укажите наименьшее число, в результате обработки которого автомат выдаст число 1412.
'''
for n in range(100, 1000):
    B = str(n)
    a = int(B[0]) + int(B[1])
    b = int(B[1]) + int(B[2])

    r = str(max(a, b)) + str(min(a, b))

    if r == '1412':
        print(n)
        break


for n in range(100, 1000):
    M = [int(i) for i in str(n)]
    a = M[0] + M[1]
    b = M[1] + M[2]
    r = str(max(a, b)) + str(min(a, b))
    if r == '1412':
        print(n)
        break
'''
# Ответ: 395


# Тип 25 № 45259
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
#
# Среди натуральных чисел, не превышающих 10**9, найдите все числа,
# соответствующие маске 12345?7?8, делящиеся на число 23 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа
# в порядке возрастания, а во втором столбце — соответствующие им результаты деления этих чисел на 23.

'''
for i in range(123450708, 123460000):
    if (i%23==0) and (i%10==8) and ((i//100)%10==7):
        print(i, i//23)
'''

'''
for x in '0123456789':
    for y in '0123456789':
        A = int(f'12345{x}7{y}8')
        if A % 23 == 0:
            print(A, A // 23)
'''


# Тип 25 № 47229
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
#
# Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 1?2139*4,
# делящиеся на 2023 без остатка. В ответе запишите в первом столбце таблицы все найденные
# числа в порядке возрастания, а во втором столбце — соответствующие им результаты деления этих чисел на 2023.

# print(10**10)
# print('1?2139*4')

# 10000000000
# 1?2139***4
'''
import itertools
M = []
for l in range(0, 3+1):
    for s in itertools.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for x in '0123456789':
    for y in M:
        A = int(f'1{x}2139{y}4')
        if A < 10**10:
            if A % 2023 == 0:
                R.append([A, A // 2023])

for x in sorted(R):
    print(*x)
'''


'''
from fnmatch import *
for x in range(2023, 10**10, 2023):
    if fnmatch(str(x), '1?2139*4'):  # соответствующие маске 1?2139*4
        print(x, x // 2023)
'''

# 1321399324 653188
# 1421396214 702618
# 1521393104 752048
# 162139404 80148


# № 8481 (Уровень: Базовый)
# (В. Рыбальченко) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Найдите все натуральные числа меньшие 10**8, которые кратны 237,
# соответствуют маске «81?2*80», но не соответствуют маске «*9*».
# В ответ в первом столбике перечислите все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на 237.
'''
from fnmatch import *
for x in range(237, 10**8, 237):
    if fnmatch(str(x), '81?2*80'):
        if not fnmatch(str(x), '*9*'):
            print(x, x // 237)
'''
# Ответ:
# 815280 3440
# 8162280 34440
# 81324180 343140
# 81727080 344840
# 81821880 345240


# Тип 25 № 27850
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245690;245 756] простые числа.
# Выведите на экран все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его порядковый номер в последовательности.
# Каждая пара чисел должна быть выведена в отдельной строке.
'''
def Prime(x):
    for divsors in range(2, x):
        if x % divsors == 0:
            return False
    return True

i = 1
for x in range(245690, 245756+1):
    if Prime(x) == True:
        print(i, x)
    i += 1
'''
# Ответ:
# 22 245711
# 30 245719
# 34 245723
# 52 245741
# 58 245747
# 64 245753


# Тип 25 № 38603
# Пусть M — сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа.
# Если таких делителей у числа нет, то значение M считается равным нулю.
#
# Напишите программу, которая перебирает целые числа, бо́льшие 700000,
# в порядке возрастания и ищет среди них такие, для которых значение M оканчивается на 8.
# Выведите первые пять найденных чисел и соответствующие им значения M.
#
# Формат вывода: для каждого из пяти таких найденных чисел в отдельной
# строке сначала выводится само число, затем — значение М.
#
# Строки выводятся в порядке возрастания найденных чисел.

'''
def Divisors(x):
    divisors = set()
    for j in range(2, int(x**0.5)+1):    # не считая единицы и самого числа.
        if x % j == 0:
            divisors.add(j)
            divisors.add(x // j)
    return sorted(divisors)

count = 0
for x in range(700_000+1, 10**10):  # бо́льшие 700000
    divisors = Divisors(x)
    if len(divisors) >= 2:
        M = max(divisors) + min(divisors)
        if M % 10 == 8:
            print(x, M)
            count += 1
            if count == 5:
                break
'''
# 700005 233338
# 700007 100008
# 700012 350008
# 700015 140008
# 700031 24168


# endregion Урок:  ******************************************************************************

# todo: Бронислав = [1-, 2, 3, 4, 5, 6-, 8, 9, 10, 12, 14, 15, 16, 18-, 19-21-, 22, 23]
# todo:   КЕГЭ    = []
# на прошлом уроке: Половину урока прорешивали 2 номера (составление таблиц) и разобрали 3, 22 номера через ВПР (записали видео).
# на следующем уроке: #todo: если на след. уроке останутся вопросы по Теории игры, то разобрать. Вопросы с домашки по 25 номера.

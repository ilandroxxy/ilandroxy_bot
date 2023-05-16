# region Домашка:  **************************************************


# endregion Домашка: **************************************************


# region Урок:  **************************************************


# № 5427 Джобс 21.12.22 (Уровень: Базовый)
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Из числа N вычитается количество нулей в двоичной записи числа N.
# 2. Строится двоичная запись полученного числа.
# 3. К полученной записи слева дописывается три младших разряда.
# 4. Результат переводится в десятичную систему и выводится на экран.

# Какое наименьшее число, большее 224, может появиться на экране в результате работы автомата?
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]

    n2 = n - s.count('0')

    s2 = bin(n2)[2:]

    s2 = s2[-3:] + s2

    r = int(s2, 2)

    if r > 224:
        M.append(r)
print(min(M))
'''
# Показать ответ: 227



# № 5431 Джобс 21.12.22 (Уровень: Базовый)
# В каждой строке таблицы приведено 5 чисел.
# Найдите количество строк, в которых квадрат максимального значения
# в строке больше произведения оставшихся четырех чисел.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[4] ** 2 > (M[0] * M[1] * M[2] * M[3]):
        count += 1
print(count)
'''
# Ответ: 2


# На вход редактору подается строка, содержащая 33 единицы, 33 двойки
# и некоторое количество троек. Порядок цифр в строке неизвестен.
#
# Исполнителю для выполнения дан следующий алгоритм
#
# НАЧАЛО
# ПОКА нашлось(11) или нашлось(22) или нашлось(13) или нашлось(23)
#    заменить(11, 2)
#    заменить(22, 1)
#    заменить(13, 2)
#    заменить(23, 1)
# КОНЕЦ ПОКА
# КОНЕЦ
# После выполнения алгоритма исполнителем получена строка,
# имеющая минимально возможное числовое значение из возможных результатов работы алгоритма.
# Сколько троек должно быть в начальной строке? Если вариантов начальной строки несколько,
# выберите ту, в которой количество троек наименьшее
'''
import itertools as it
mini = 9999999
for n in range(1, 100):
    for s in it.permutations('1' * 33 + '2' * 33 + '3' * n):
        s = ''.join(s)

        while '11' in s or '22' in s or '13' in s or '23' in s:
            s = s.replace('11', '2', 1)
            s = s.replace('22', '1', 1)
            s = s.replace('13', '2', 1)
            s = s.replace('23', '1', 1)

        summ = sum([int(i) for i in s])
        if mini > summ:
            mini = summ
            print(n, mini)
'''
# Показать ответ: 1



# 14 № 5436 Джобс 21.12.22 (Уровень: Сложный)
# Известно, что значение выражения 36x53_8 – 4y3_8 является положительным и минимальным.
# Известно, что x и y – допустимые комбинации из одной или более цифр.
#
# Определите значение выражения.
# В качестве ответа запишите полученное число в десятичной системе счисления.
# Основание системы счисления указывать не нужно.
'''
import itertools
alphabet = [0, 1, 2, 3, 4, 5, 6, 7]

M = []
for l in range(1, 4):
    for s in itertools.product(alphabet, repeat=l):
        M.append(list(s))


print(M)
mini = 999999
for x in M:
    for y in M:

        A = [3, 6] + x + [5, 3]
        A.reverse()
        a = 0
        for i in range(0, len(A)):
            a += A[i] * 8 ** i

        B = [4] + y + [3]
        B.reverse()
        b = 0
        for i in range(0, len(B)):
            b += B[i] * 8 ** i

        r = a - b

        if r > 0:
            if mini > r:
                mini = r
                print(mini, r)
'''


'''
import itertools

mini = 999999
M = []
for l in range(1, 4):
    for s in itertools.product('01234567', repeat=l):
        s = ''.join(s)
        M.append(s)


for x in M:
    for y in M:
        A = int(f'36{x}53', 8)
        B = int(f'4{y}3', 8)

        r = A - B

        if r > 0:
            if mini > r:
                mini = r
                print(mini)
'''
# Показать ответ:
# 12848

# endregion Урок:  **************************************************

import useful
print(useful.Who_Is_Name())

# todo: Денис = [1, 2, 3, 5, 8, 9, 16, 17, 18, 19-21, 22, 23, 24], на следующем уроке:
# на прошлом уроке: Прорешивали вариант с сложными задачами от Джобса, чтобы подготовиться к апробации.
# на следующем уроке:

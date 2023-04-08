# region Домашка: ********************************************************

#НАЧАЛО
#ПОКА нашлось (49) ИЛИ нашлось (97) ИЛИ нашлось (47)
#ЕСЛИ нашлось (47)
#ТО заменить (47, 74)
#КОНЕЦ ЕСЛИ
#ЕСЛИ нашлось (97)
#ТО заменить (97, 79)
#КОНЕЦ ЕСЛИ
#ЕСЛИ нашлось (49)
#О заменить (49, 94)
# Запишите без разделителей символы, которые имеют порядковые номера 25, 71 и 105в получившейся строке.
'''
from random import shuffle

n = list('7' * 40 + '9' * 40 + '4' * 50)
shuffle(n)
n = ''.join(n)
while '49' in n or '97' in n or '47' in n:
    if '49' in n:
        n = n.replace('47', '74',1)
    elif '97' in n:
        n = n.replace('97','79',1)
    elif '49' in n:
        n = n.replace('49','94',1)
print(n[25],n[71],n[105])
'''


#Дана программа для Редактора:

#НАЧАЛО
#ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#заменить (01, 103)
#заменить (02, 10)
#заменить (03, 210)
#КОНЕЦ ПОКА
#КОНЕЦ

#Известно, что исходная строка начинается с цифры 0, а далее содержит 12 цифр 1, 15 цифр 2 и 17 цифр 3,
# расположенных в произвольном порядке.
# Сколько цифр 2 будет в строке, которая получится после выполнения данной программы?
'''
from random import shuffle

n = list('0' + '1' * 12 + '2' * 15 + '3' * 17)
shuffle(n[1:])
n = ''.join(n)
while '01' in n or '02' in n or '03' in n:
    if '01' in n:
        n = n.replace('01','103',1)
    elif '02' in n:
        n = n.replace('02','10',1)
    elif '03' in n:
        n = n.replace('03','210',1)
print(n.count('2'))
'''
#3. Тип 12 № 28550

#Дана программа для Редактора:

#НАЧАЛО
#ПОКА нашлось (21)
#аменить (21, 5)
#КОНЕЦ ПОКА
#КОНЕЦ

#Исходная строка содержит десять единиц и некоторое количество двоек, других цифр нет,
# точный порядок расположения единиц и двоек неизвестен.
# После выполнения программы получилась строка с суммой цифр 34.
# Какое наименьшее количество двоек могло быть в исходной строке?
'''
from random import shuffle
for i in range(1,20):
    s = list('1' * 10 + '2' * i)
    shuffle(s)
    s = ''.join(s)
    while '21' in s:
        if '21' in s:
            s = s.replace('21', '5', 1)
            for j in range(len(s)):
                count = 0
                j = int(j)
                count += j
                if count == 34:
                    print(i)
'''

#Тип 12 № 33514

#Дана программа для редактора:

#НАЧАЛО
#ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#заменить (01, 30)
#заменить (02, 101)
#аменить (03, 202)
#ОНЕЦ ПОКА
#КОНЕЦ

#Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 15 единиц, 10 двоек и 60 троек.
# Сколько единиц было в исходной строке?

'''
for i in range(60):
    for j in range(60):
        for k in range(60):
            s = '0' + '1' * i + '2' * j + '3' * k
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '201', 1)
            if s.count('1')== 15 and s.count('2') == 10 and s.count('3') == 60:
                print(i)
'''


#1. КЕГЭ № 6637 Пробник ИМЦ СПб (Уровень: Базовый)
#Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#– символ «?» означает ровно одну произвольную цифру;
#– символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
#Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 1?2139*4, делящиеся на 3052 без остатка.
#В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 3052.
'''
import itertools as it

for x in range(0, 10):
    M = []
    for l in range(0, 2 + 1):
        for s in it.product('0123456789', repeat=l):
            s = ''.join(s)
            M.append(s)

for x in M:
    for y in '0123456789':
        A = int(f'1{x}2139{y}4')
        B = A // 3052
        print(A,B)
'''


# № 837 Джобс 14.12.2020 (Уровень: Сложный)
# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения
# двух натуральных чисел и найдём для каждого такого произведения разность сомножителей, каждый из которых больше единицы.
# Например, для числа 24 получим: 24 = 2*12 = 3*8 = 4*6, множество разностей содержит числа 10, 5 и 2.
# Найдите числа в диапазоне [543210; 987654], для которых:
# - есть как минимум две различных пары натуральных сомножителей,
# - максимальная разность сомножителей кратна минимальной разности сомножителей, не равной нулю;
# - минимальная разность сомножителей больше 4444.
# Для каждого найденного числа выведите два числа: найденное число и минимальную разность сомножителей, не равную нулю.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            dl.add((n // j) - j)  # в dl складываем разность сомножителей
    return sorted(dl)

for n in range(543210, 987654 + 1):
    dl = F(n)
    if len(dl) >= 2:
        if min(dl) != 0 and max(dl) % min(dl) == 0:
            if min(dl) > 4444:
                print(n, min(dl))
'''
# Показать ответ:
# 647224 4623
# 705460 4899
# 832204 5475
# 900904 5775


# № 6637 Пробник ИМЦ СПб (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа,
# соответствующие маске 1?2139*4, делящиеся на 3052 без остатка.

# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на 3052.

# print(10**10)
# print('1?2139***4')
'''
import itertools
M = []
for l in range(0, 3+1):
    for s in itertools.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for y in '0123456789':
    for x in M:
        A = int(f'1{y}2139{x}4')
        if A % 3052 == 0:
            R.append([A, A//3052])

for x in sorted(R):
    print(*x)
'''
# Ответ:
# 1421398804 465727
# 1521397584 498492
# 1621396364 531257
# 1721395144 564022
# 1821393924 596787
# 1921392704 629552


# 6276 Danov2302 (Уровень: Средний) (А.Богданов) Найдите все натуральные числа, не превышающие 10**10,
# которые соответствуют маске 1?1?1?1*1 и при этом без остатка делятся на 2023, а сумма цифр числа равна 22.
# В ответе запишите все найденные числа в порядке возрастания.

# print(10**10)
# print('1?1?1?1**1')
'''
import itertools
M = []
for l in range(0, 2+1):
    for s in itertools.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for a in '0123456789':
    for b in '0123456789':
        for c in '0123456789':
            for x in M:
                A = int(f'1{a}1{b}1{c}1{x}1')
                if A % 2023 == 0 and sum([int(i) for i in str(A)]) == 22:
                    R.append(A)

for x in sorted(R):
    print(x)
'''
# Ответ:
# 19131511
# 1012141291
# 1319111311
# 1516111051


# № 5678 Вариант 09.01.23 (Уровень: Средний)
# (М. Ишимов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# которые делятся на сумму нечётных цифр числа и соответствующие маске 124*5*79.

# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – сумму всех цифр этого числа.

# print(10**8)
# print('1245**79')
'''
import itertools
M = []
for l in range(0, 2+1):
    for s in itertools.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for x in M:
    for y in M:
        A = int(f'124{x}5{y}79')
        SUMM = sum([int(i) for i in str(A) if int(i) % 2 != 0])
        if A <= 10**8 and A % SUMM == 0:
            R.append([A, sum([int(i) for i in str(A)])])

for x in sorted(R):
    print(*x)
'''
# Ответ:
# 1249579 37
# 12409579 37
# 12452979 39
# 12456179 35


# № 7595 Досрочная волна 2023 (Уровень: Базовый)
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
#
# F(n) = n, если n ≥ 2025,
#
# F(n) = n + 3 + F(n+3), если n < 2025.

# Чему равно значение выражения F(23) – F(21)?
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n+3)

print(F(23) - F(21))
'''
# Ответ: 1338


#
# № 7596 Досрочная волна 2023 (Уровень: Базовый) В файле содержится последовательность целых чисел. Элементы
# последовательности могут принимать целые значения от 1 до 100 000 включительно. Определите количество пар
# последовательности, в которых только одно число трехзначное, и сумма элементов пары кратна минимальному
# трехзначному значению последовательности, оканчивающемуся на 5. В ответе запишите два числа: сначала количество
# найденных пар, затем минимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих
# подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if len(str(i)) == 3 and str(i)[-1] == '5']
count = 0
mini = 999999
for i in range(0, len(M)-1):
    if (len(str(M[i])) == 3 and len(str(M[i+1])) != 3) or (len(str(M[i])) != 3 and len(str(M[i+1])) == 3):
        if (M[i] + M[i+1]) % min(A) == 0:
            count += 1
            mini = min(mini, M[i] + M[i+1])
print(count, mini)
'''
# Ответ: 2 33120


# № 7600 Досрочная волна 2023 (Уровень: Базовый)
# Текстовый файл состоит не более, чем из 1 200 000 прописных символов латинского алфавита.
# Определите максимальное количество идущих подряд символов,
# среди которых любые два символа из набора Q, R, S в различных комбинациях (с учётом повторений) не стоят рядом.
# Для выполнения этого задания следует написать программу
'''
import itertools
R = []
for s in itertools.product('QRS', repeat=2):
    s = ''.join(s)
    R.append(s)
print(R)

s = open('24.txt').readline()
for x in R:
    s = s.replace(x, ' ')

M = [len(i) for i in s.split()]
print(1 + max(M) + 1)

#     +1     +1
s = 'RR000000RR'
s = s.replace('RR', ' ')
s = ' 000000 '  # потеряли два символа
'''
# Показать ответ: 544



# endregion Домашка: ********************************************************


# region Урок: ********************************************************



# endregion Урок: ********************************************************


# todo: Никита = [2, 3, 4, 5, 6, 7, 8, 9.1, 11, 12, 13, 14+, 15+, 16, 17, 18, 19-21, 23, 24+, 25.2]
# на прошлом уроке: Повторяли задачи 25 с масками, прорешивали номера 16, 17, 24 с досрока 2023 года
# на следующем уроке:

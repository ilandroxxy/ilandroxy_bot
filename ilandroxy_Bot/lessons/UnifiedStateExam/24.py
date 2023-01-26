
# region Тип 24 № 27686
'''
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readline()

count = 1
Maxcount = 0
for i in range(0, len(s)-1):
    if s[i] == 'X' and s[i+1] == 'X':
        count += 1
        if Maxcount < count:
            Maxcount = count
    else:
        count = 1
print(Maxcount)
'''
# Ответ: 19
# endregion Тип 24 № 27686


# region Тип 24 № 36879
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между
# одинаковыми буквами в одной строке.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.


f = open('24.txt', 'r')
s = f.readlines()
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
M = []

for strings in s:
    maxi = 0
    if strings.count('G') < 25:
        # print(strings.count('G'), strings)
        for i in alphabet:
            if maxi < strings.rindex(i) - strings.index(i):
                maxi = strings.rindex(i) - strings.index(i)
        M.append(maxi)
print(max(M))
'''
# Ответ: 1001
# endregion Тип 24 № 36879


# region Тип 24 № 35998
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
#
# Пример. Исходный файл:
# GIGA
# GABLAB
# NOTEBOOK
# AGAAA
#
# В этом примере во всех строках меньше 25 букв A.
# Самое большое расстояние между одинаковыми буквами – в третьей строке между буквами O, расположенными в строке на 2-й и 7-й позициях.
# В ответе для данного примера нужно вывести число 5.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
f = open('24.txt', 'r')
S = f.readlines()
for i in range(0, len(S)):
    print(len(S[i]))
print("Количество строк: ", len(S))
maxi = 0
Alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for i in S:
    for j in Alphabet:
        if i.count("A") < 25:
            if maxi < i.rfind(j) - i.find(j):
                maxi = i.rfind(j) - i.find(j)
print(maxi)
'''
# Ответ: 1004
# endregion Тип 24 № 35998

# region Тип 24 № 33526
'''
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
#
# Например, в тексте CBCABABACCC есть комбинации CBC, ABA (два раза), BAB и CCC.
# Чаще всего— 3 раза — между двумя одинаковыми символами стоит B, в ответе для этого случая надо написать B.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
f = open('24.txt', 'r')
s = f.readline()
M = []
for i in range(0, len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])
print(len(s), len(M))
Alphabet = 'qwertyuiopasdfghjklzxcvbnm'
Alphabet = Alphabet.upper()  # просто было лень переписывать, подняли регистр всех символов
print(Alphabet)
maxi = -9999999  # если бы я попросил найти максимальный элемент в списке отрицательных числе, то maxi = 0 не имело бы смысла
res = 0
for x in Alphabet:
    print(x, M.count(x))
    if maxi < M.count(x):
        maxi = M.count(x)
        res = x
print("Ответ: ", maxi, res)
'''
# Ответ: D
# endregion Тип 24 № 33526

# region Тип 24 № 33196
'''
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
#
# Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу — A и D. Для этого текста ответом будет B.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
f = open('24.txt', 'r')
s = f.readline()
M = []
for i in range(0, len(s)-1):
    if s[i] == "A":
        M.append(s[i+1])
print(len(s), len(M))
Alphabet = 'qwertyuiopasdfghjklzxcvbnm'
Alphabet = Alphabet.upper()  # просто было лень переписывать, подняли регистр всех символов
print(Alphabet)
maxi = -9999999  # если бы я попросил найти максимальный элемент в списке отрицательных числе, то maxi = 0 не имело бы смысла
res = 0
for x in Alphabet:
    print(x, M.count(x))
    if maxi < M.count(x):
        maxi = M.count(x)
        res = x
print("Ответ: ", maxi, res)
'''
# Ответ: G
# endregion Тип 24 № 33196

# region Тип 24 Статград

# Текстовый файл состоит из символов A, C, D, F, O.
# Определите максимальное количество идущих подряд пар символов вида
# cогласная + гласная в прилагаемом файле.
# Для выполнения этого задания следует написать программу

'''
n = open('24.txt').readline()
sogl, gl = 'CDF', 'AO'
counter = max_counter = 0

for i in range(0, len(n)-1):
    if (n[i] in gl and n[i+1] in sogl) or (n[i] in sogl and n[i+1] in gl):
        counter += 1
        max_counter = max(max_counter, counter)
    else:
        counter = 0

print(max_counter / 2)
'''
# Ответ: 95

# endregion Тип 24 Статград

# region Тип 24 № 45258
# Текстовый файл состоит из символов A, B и C.
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB,
# или только из пар AB и CB в произвольном порядке следования этих пар.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.replace('AB', '*').replace('CB', '*')
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 65

# endregion Тип 24 № 45258

# region Тип 24 № 36037

# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки 444.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
# Вариант 1
print(3+max(len(i) for i in open('24.txt').readline().replace('XZZY', ' ').split())+3)
# Ответ: 1713

# Вариант 2
s = open('24.txt').readline()
count = 3
max_count = 0
for i in range(0, len(s)-3):
    if s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y':
        count = 3
    else:
        count += 1
        max_count = max(max_count, count)
print(max_count)

# Вариант 3
s = open('24.txt').readline()
count = 3
max_count = 0
for i in range(0, len(s)-3):
    if s[i:i+4] == 'XZZY':
        count = 3
    else:
        count += 1
        max_count = max(max_count, count)
print(max_count)
'''
# Ответ: 1713

# endregion Тип 24 № 36037

# region Тип 24 № 27688

# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов Z.
# Хотя бы один символ Z находится в последовательности.

# Вариант 1
'''
s = open('24.txt').readline()
count = 1
max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'Z' and s[i+1] == 'Z':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
'''

# Вариант 2
'''
print(max([len(i) for i in open('24.txt').readline().replace('X', ' ').replace('Y', ' ').split()]))
# Ответ: 7
'''

# Вариант 3
'''
s = open('24.txt').readline()
s = s.replace('X', ' ').replace('Y', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 7

# endregion Тип 24 № 27688


# region Тип 24 № 37159

# Текстовый файл состоит не более, чем из 10**7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
s = s.replace('ad', ' ').replace('da', ' ')
M = [len(i) for i in s.split()]
print(1+max(M)+1)  # длина подстроки ad, da - 1 = 1
'''
# Ответ: 2252

# endregion Тип 24 № 37159


# region Тип 24 № 36037

# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
# s = 'XZZYAAAXZZY'
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3+max(M)+3)    # длина подстроки XZZY - 1 = 3
'''
# XZZYAAAXZZY
# некорректно AAA
# корректно ZZYAAAXZZ

# Ответ: 1713

# endregion Тип 24 № 36037


# region Тип 24 № 27689

# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZXY... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
print(s)
print(len('XYZXYZXYZXYZX'))
'''


'''
s = open('24.txt').readline()
count = 2
max_count = 0
for i in range(0, len(s)-2):
    # if (s[i] == 'X' and s[i+1] == 'Y' and s[i+2] == 'Z') or (s[i] == 'Y' and s[i+1] == 'Z' and s[i+2] == 'X') or (s[i] == 'Z' and s[i+1] == 'X' and s[i+2] == 'Y'):
    if s[i:i+3] == 'XYZ' or s[i:i+3] == 'YZX' or s[i:i+3] == 'ZXY':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 2
print(max_count)
'''
# Ответ: 13

# endregion Тип 24 № 27689


# region Тип 24 № 27692

# Текстовый файл состоит не более чем из 10**6 символов A, B и C. Определите максимальное количество идущих подряд символов B.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Вариант 1
'''
s = open('24.txt').readline()
count = 1
max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'B' and s[i+1] == 'B':
        count += 1
        # if max_count < count:
        #     max_count = count
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
'''

# Вариант 2
'''
s = open('24.txt').readline()
s = s.replace('A', ' ').replace('C', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''

# Вариант 3
'''
print(max([len(i) for i in open('24.txt').readline().replace('A', ' ').replace('C', ' ').split()]))
'''
# ответ: 11

# endregion Тип 24 № 27692
# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************
'''
s = sorted('ПАРУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if slovo.count('У') <= 1:
                        if 'АА' not in slovo:
                            print(num, slovo)
'''
# 2969


# № 11201 (Уровень: Средний)
# (С. Якунин) Полина составляет слова, переставляя
# буквы в слове ПАЙТОН. Сколько слов может составить Полина,
# если известно, что сумма порядковых номеров гласных букв, в каждом из них, равна 6?
# Буквы нумеруются слева направо, начиная с единицы.
'''
s = 'ПАЙТОН'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(slovo) == len(set(slovo)):
                            M = [i+1 for i in range(len(slovo)) if slovo[i] in 'АО']
                            if sum(M) == 6:
                                cnt += 1
print(cnt)
'''

#
# № 10090 Демоверсия 2024 (Уровень: Базовый)
# Сколько существует восьмеричных пятизначных чисел, не
# содержащих в своей записи цифру 1, в которых
# все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0' and num.count('1') == 0:
                        if len(num) == len(set(num)):
                            num = num.replace('0', '2').replace('4', '2').replace('6', '2')
                            num = num.replace('3', '1').replace('5', '1').replace('7', '1')
                            if '22' not in num and '11' not in num:
                                cnt += 1
print(cnt)


s = '01234567'
s1 = '1357'
s2 = '0246'
cnt = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    num = a + b + c + d + e
                    if num[0] != '0' and num.count('1') == 0:
                        if len(num) == len(set(num)):
                            cnt += 1
for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    num = a + b + c + d + e
                    if num[0] != '0' and num.count('1') == 0:
                        if len(num) == len(set(num)):
                            cnt += 1
print(cnt)
'''

# № 9777 Основная волна 20.06.23 (Уровень: Базовый)
'''
s = sorted('КОМПЬЮТЕР')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if num % 2 != 0:
                        if a != 'Ь':
                            if slovo.count('К') == 2:
                                print(num, slovo)
'''

# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
# Сколько существует семизначных семеричных чисел, которые
# содержат в своей записи ровно две чётные цифры?
'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if num[0] != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                    cnt += 1
print(cnt)
'''


# № 16328 Открытый вариант 2024 (Уровень: Базовый)
'''
M = [int(x) for x in open('17.txt')]
D = [x for x in M if abs(x) % 19 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % min(D) == 0 or y % min(D) == 0:
        R.append(x + y)
print(len(R), max(R))
'''

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-2:] == '13']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    D = [p for p in (x, y, z) if len(str(abs(p))) == 3]
    if len(D) == 2:
        if (x + y + z) <= max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''

# endregion Урок: ***************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Сева = [1, 2, 3, 4, 6, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
# КЕГЭ  = [5, 8, 12, 14, 15, 16, 23, 25]
# на следующем уроке: 9, 17, 24

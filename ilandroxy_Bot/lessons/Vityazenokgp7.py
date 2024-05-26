# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 24 №27697
# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов D.
# Хотя бы один символ D находится в последовательности.
'''
s = open('24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'D' and s[i+1] == 'D':
    if s[i:i+2] == 'DD':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)

# Вариант 2
s = open('24.txt').readline()
s = s.replace('L', ' ').replace('R', ' ')
print(max([len(x) for x in s.split()]))
'''


# № 16388 ЕГКР 27.04.24 (Уровень: Базовый)
'''
s = open('24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('KLMN', 'LMNK', 'MNKL', 'NKLM'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 3
print(maxi)
'''
# Ответ: 182


# Тип 24 №47228
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида согласная + гласная.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('O', 'A')
while 'DD' in s or 'AA' in s:
    s = s.replace('DD', 'D D').replace('AA', 'A A')
print(max([len(x) for x in s.split()]) // 2)
'''
# Ответ: 95


# Тип 24 №27690
'''
s = open('24.txt').readline()
while 'AA' in s or 'BB' in s or 'CC' in s:
    s = s.replace('AA', 'A A').replace('BB', 'B B').replace('CC', 'C C')
print(max([len(x) for x in s.split()]))


s = open('24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''


# Тип 24 №48445
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите максимальное количество идущих подряд групп символов вида
# согласная + согласная + гласная.
'''
s = open('24.txt').readline()
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('O', 'A')
s = s.replace('DDA', '*')
s = s.replace('D', ' ').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''

'''
s = open('24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-2):
    if int(s[i]) + int(s[i+1]) > int(s[i+2]):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

# Тип 24 №39253
'''
s = open('24.txt').readline().split('D')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'D' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 354

# endregion Урок: **********************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Михаил = [2, 5, 6, 8, 12, 14, 15, 16, 23, 24-, 25]
# КЕГЭ  = []
# на следующем уроке:

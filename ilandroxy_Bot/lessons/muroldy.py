
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 16389 ЕГКР 27.04.24 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(98591, 10**10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)

        # 52253230 530
        # 5024493133 50963
        # 5125253135 51985
        # 5226013137 53007
        # 5326773139 54029
        # 5524053730 56030
        # 5624813732 57052
        # 5725573734 58074
        # 5826333736 59096
        # 5927093738 60118
'''


# № 13868 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4'):
        if sum(map(int, str(x))) % 2 != 0:
            print(x, x // 2024)
            
            # 11275704 5571
            # 1124576904 555621
            # 1126570544 556606
            # 1127572424 557101
            # 1128574304 557596
'''


# № 12932 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '1?2*4'):
        if x ** 0.5 == int(x ** 0.5):  #  и являющиеся полными квадратами
            print(x, x // 2024)
            
            # 1024144 506
            # 1327290624 655776
            # 1721586064 850586
'''

# № 16388 ЕГКР 27.04.24 (Уровень: Базовый)
'''
s = open('24.txt').readline()
count = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('KLMN', 'LMNK', 'MNKL', 'NKLM'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 3
print(maxi)
'''


# № 16333 Открытый вариант 2024 (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.replace('Q', 'R').replace('W', 'R')
s = s.replace('1', '2').replace('4', '2')
while '22' in s or 'RR' in s:
    s = s.replace('22', '2 2').replace('RR', 'R R')
print(max([len(x) for x in s.split()]))
'''


# № 12254 ЕГКР 16.12.23 (Уровень: Базовый)
'''
s = open('24.txt').readline()
count = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('RSQ', 'SQR', 'QRS'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''

'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 9845 Основная волна 27.06.23 (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
s = s.replace('9', '8')
while '88' in s or 'AA' in s:
    s = s.replace('88', '8 8').replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''


# № 9791 Основная волна 20.06.23 (Уровень: Средний)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('24.txt').readline()
for x in alphabet[16:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

'''
s = open('24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 8510 Апробация 17.05 (Уровень: Средний)
'''
s = open('24.txt').readline()
for x in 'NN OO PP NO ON PO OP NP PN'.split():
    s = s.replace(x, f'{x[0]} {x[1]}')
print(max([len(x) for x in s.split()]))


s = open('24.txt').readline()
s = s.replace('O', 'N').replace('P', 'N')
while 'NN' in s:
    s = s.replace('NN', 'N N')
print(max([len(x) for x in s.split()]))
'''


# № 7272 OpenFIPI (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.replace('AB', '*').replace('CB', '*')
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# № 7094 OpenFIPI (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.replace('U', 'A')
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('DA', '*')
s = s.replace('D', ' ').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''

# № 6757 Апробация 10.03.23 (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.replace('CFE', '*').replace('FCE', '*')
for x in 'CDEF':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

'''
s = open('24.txt').readline()
s = s.replace('3', '1').replace('5', '1')
s = s.replace('4', '2')
s = s.replace('21', '*')
s = s.replace('2', ' ').replace('1', ' ')
print(max([len(x) for x in s.split()]))
'''
# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Геля = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 13, 14, 17, 18, 19-21, 22, 23, 24, 25]
# на следующем уроке:

# region Домашка: ************************************************************

# endregion Домашка: ************************************************************

# region Урок: **************************************************************


# № 16388 ЕГКР 27.04.24 (Уровень: Базовый)
'''
s = open('24.txt').readline()
count = 3  # локальный счетчик
maxi = 0  # глобальный счетчик
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
    s = s.replace('RR', 'R R').replace('22', '2 2')
print(max([len(x) for x in s.split()]))
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 9791 Основная волна 20.06.23 (Уровень: Средний)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('24.txt').readline()
for x in alphabet[16:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''
# endregion Урок: ************************************************************


# region Разобрать: ***************************************************************

# endregion Разобрать: *************************************************************

# Никита = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:

# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

# КЕГЭ № 12254 ЕГКР 16.12.23 (Уровень: Базовый)
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

# Не менее трех раз
# oooXooooooXooooXoooooXoooooXoooooXooooXoooooXoooo
# ['ooo', 'oooooo', 'oooo', 'ooooo', 'ooooo', 'ooooo', 'oooo', 'ooooo', 'oooo']
'''
s = open('24.txt').readline().split('X')
mini = 10**9
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''


'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ


s = open('24.txt').readline()
for a in 'AEIOUY':
    s = s.replace(a, 'A')

for b in alphabet:
    if b not in 'AEIOUY':
        s = s.replace(b, 'B')

while 'AA' in s or 'BB' in s:
    s = s.replace('AA', 'A A').replace('BB', 'B B')

print(max([len(x) for x in s.split()]))
'''


s = open('24.txt').readline()
maxi = 0
s = s.replace('C', 'C ').replace('D', 'D ').split()
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('D') == 2 and r.count('C') == 2:
        maxi = max(maxi, len(r))
print(maxi)



# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Дмитрий = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

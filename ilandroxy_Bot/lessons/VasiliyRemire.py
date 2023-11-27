
# region Домашка: ******************************************************************

'''
count = 0
m = 0
f = open('17.txt')
l = [int(i) for i in f]

max_dvy = 0
for i in range(len(l)):
    if l[i] % 100 == 25:
        max_dvy = max(max_dvy, l[i])
print(max_dvy)
for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1], l[i+2]]
    for x in s:
        if 999 < abs(x) < 10000:
            c += 1
    if c <= 2 and sum(s) <= max_dvy:
        m = max(m, sum(s))
        count += 1
print(count, m)


l = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
max_dvy = max([x for x in l if x % 100 == 25])
for i in range(len(l) - 2):
    S = [l[i], l[i + 1], l[i + 2]]
    if len([x for x in S if len(str(abs(x))) == 4]) <= 2:
        if sum(S) <= max_dvy:
            m = max(m, sum(S))
            count += 1
print(count, m)  # 6315 84523
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 2499 (Уровень: Базовый)
#
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
#
# Сколько раз в файле встречается последовательность символов XXXX?
'''
s = open('24.txt').readline()
print(s.count('XXXX'))
s = s.replace('XXXX', '****')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(len(s.split()))
'''

s = open('24.txt').readline()
count = 0
for i in range(0, len(s)-3):
    if s[i:i+4] == 'XXXX':
        count += 1
print(count)
# endregion Урок: ******************************************************************


# Василий = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1]
# КЕГЭ  = []
# на следующем уроке:

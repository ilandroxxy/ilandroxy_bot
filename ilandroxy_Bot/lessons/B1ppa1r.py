# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 24 №33103
# Текстовый файл содержит строки различной длины.
# Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква A встречается чаще, чем буква E.
'''
F = open('24.txt').readlines()
count = 0
for s in F:
    if s.count('A') > s.count('E'):
        count += 1
print(count)
'''
# Ответ: 485


# Тип 24 №35913
# Текстовый файл содержит строки различной длины.
# Необходимо найти строку, содержащую наименьшее количество букв N
# (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
F = open('24.txt').readlines()
r = ''
mini = 9999999
for s in F:
    if s.count('N') < mini:
        mini = s.count('N')
        r = s


for a in sorted(set(r)):
    print(a, r.count(a))
'''

'''
F = open('24.txt').readlines()
r = ''
mini = 9999999
for s in F:
    if s.count('N') < mini:
        mini = s.count('N')
        r = s

R = []
for a in sorted(set(r)):
    R.append([r.count(a), a])
print(max(R))
'''
# Ответ: Y


# Тип 24 №35998
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное
# расстояние между одинаковыми буквами в одной строке.
'''
F = open('24.txt').readlines()
maxi = 0
for s in F:
    if s.count('A') < 25:
        for a in set(s):
            maxi = max(maxi, s.rindex(a) - s.index(a))
print(maxi)
'''
# Ответ: 1004


'''
s = 'abcdb'
print(s.rindex('b') - s.index('b'))  # 4 - 1 = 3
# print(s.rindex('2') - s.index('2'))  # ValueError: substring not found

print(s.rfind('b') - s.find('b'))  # 4 - 1 = 3
print(s.rfind('2') - s.find('2'))  # 0
'''

# Тип 24 №37159
# Текстовый файл состоит не более, чем из 10**7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
'''
s = open('24.txt').readline()
s = s.replace('ad', '* *').replace('da', '* *')
print(max([len(x) for x in s.split()]))
'''
# Ответ: 2252.


# todo № 10105 Демоверсия 2024 (Уровень: Средний) Никита
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-101):
    maxi = max(maxi, len('T'.join(s[i:i+101])))
print(maxi)
'''

# Среди которых символ T встречается ровно 3 раз (максимальную)
'''
s = 'xxxxTxxxxxxxTxxxxxxxxTxxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxxTxxx'
# 'xxxxTxxxxxxxTxxxxxxxxTxxxxxxxxx'
# 'xxxxxxxTxxxxxxxxTxxxxxxxxxTxxxxxxxxxxx'
# 'xxxxxxxxTxxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxx'  # 44
# 'xxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxxTxxx'
s = s.split('T')
# ['xxxx', 'xxxxxxx', 'xxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxxxx', 'xxxxxxxxxxxxx', 'xxx']
maxi = 0
for i in range(len(s)-4):
    if maxi < len('T'.join(s[i:i+4])):
        maxi = len('T'.join(s[i:i+4]))
        print('T'.join(s[i:i+4]))
print(maxi)
'''

# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности),
# среди которых символ Y встречается не более 150 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)-151):
    maxi = max(maxi, len('Y'.join(s[i:i+151])))
print(maxi)
'''
# Ответ: 244


# Тип 24 №59794
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную длину подстроки, содержащую ровно 110 символов "U".
# Для выполнения этого задания следует написать программу.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('U')
mini = 999999999
for i in range(len(s)-110-1):
    mini = min(mini, len('U'.join(s[i:i+110-1])))
print(mini+2)


s = open('24.txt').readline().split('U')
mini = 999999999
for i in range(len(s)-108):
    mini = min(mini, len(''.join(s[i:i+108+1])) + 108)
print(mini+2)
'''


# Среди которых символ T встречается ровно 3 раз (минимальную)
s = 'xxxxTxxxxxxxTxxxxxxxxTxxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxxTxxxT'
# 'xxxxTxxxxxxxTxxxxxxxxTxxxxxxxxx'
# 'xxxxxxxTxxxxxxxxTxxxxxxxxxTxxxxxxxxxxx'
# 'xxxxxxxxTxxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxx'
# 'xxxxxxxxxTxxxxxxxxxxxTxxxxxxxxxxxxxTxxx'
'''
s = s.split('T')
mini = 9999999
for i in range(len(s)-2):
    print('T'.join(s[i:i + 2]))
    # if mini > len('T'.join(s[i:i+2])):
    #     mini = len('T'.join(s[i:i+2]))
    #     print('T'.join(s[i:i+2]))
print(mini+2)
'''

# Ответ: 1765


# Тип 13 №6271
# По заданным IP-адресу узла и маске определите адрес сети.
#
# IP-адрес узла: 128.64.208.32
# Маска: 255.255.224.0

# IP-адрес узла  &  Маска = адрес сети
'''
from ipaddress import *
net = ip_network('128.64.208.32/255.255.224.0', 0)
print(net)
'''
# Ответ: 128.64.192.0


# Тип 13 №15824
# Для узла с IP-адресом 98.162.198.94 адрес сети равен 98.162.192.0.
# Для скольких различных значений маски это возможно?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'98.162.198.94/{mask}', 0)
    print(net, net.netmask)
    # 98.162.192.0/18 255.255.192.0
    # 98.162.192.0/19 255.255.224.0
    # 98.162.192.0/20 255.255.240.0
    # 98.162.192.0/21 255.255.248.0
'''
# Ответ: 4

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Никита = [5.1, 7.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1]
# КЕГЭ  = []
# на следующем уроке: Разбираем 25 номера

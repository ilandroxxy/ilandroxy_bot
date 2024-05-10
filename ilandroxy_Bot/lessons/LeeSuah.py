# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************
'''
m = [int(x) for x in open('17.txt')]
maxel = max([x for x in m if len(str(abs(x))) == 5 and abs(x) % 100 == 21])

R = []
for i in range(len(m) - 1):
    x, y = m[i], m[i + 1]
    if (len(str(abs(x))) == 5 and str(x)[-2:] == '21') != (len(str(abs(y))) == 5 and str(y)[-2:] == '21'):
        if (x ** 2 + y ** 2) >= maxel ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

'''
m = [int(x) for x in open('17.txt')]
maxel = max([x for x in m if len(str(abs(x))) == 5 and abs(x) % 100 == 21])

maxi = 0
k = 0
for i in range(len(m) - 1):
    x, y = m[i], m[i + 1]
    if ((len(str(abs(x))) == 5 and abs(x) % 100 == 21) and (len(str(abs(y))) != 5 and abs(y) % 100 != 21)) or (
            (len(str(abs(y))) == 5 and abs(y) % 100 == 21) and (len(str(abs(x))) != 5 and abs(x) % 100 != 21)):
        if (x ** 2 + y ** 2) >= maxel ** 2:
            k += 1
            maxi = max(maxi, x + y)
print(k, maxi)
'''

# NKLMNKLMNKL
'''
s = open('24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    r = s[i:i+4]
    # if r == 'KLMN' or r == 'LMNK' or r == 'MNKL' or r == 'NKLM':
    if any(r == a for a in 'KLMN LMNK MNKL NKLM'.split()):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 3
print(maxi)
'''


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************


# todo Подумать и разобрать (задача на компьютер в сети)
'''
from ipaddress import *
net = ip_network('10.18.134.220/255.255.255.192', 0)
print(net)  # 10.18.134.192
ip1 = ip_address('10.18.134.220')  # Адрес узла
ip2 = ip_address('10.18.134.192')  # Адрес сети
print(int(ip1) - int(ip2))
'''

# todo Разобрать  КЕГЭ #10789 (в ответах 4, у меня 5)
# Для узла с IP-адресом 203.75.227.102 адрес сети равен 203.75.224.0. Для скольких
# значений третьего слева байта маски допустим такой адрес сети?

'''
from ipaddress import *

for mask in range(16, 33):
    net = ip_network(f'203.75.227.102/{mask}', 0)
    for ip in net:
        print(ip, net.netmask)
'''

# маски получились (255.255.192/224/240/248/252.0)

# Проверка полученных масок
''' 
from ipaddress import *
net = ip_network('203.75.227.102/255.255.192.0', 0)
for x in net:
    print(x)
    break
'''

# todo Разобрать Тип 13 №64898
# Узлы с IP-адресами 114.91.57.39 и 114.91.19.61 находятся в одной сети.
# Укажите наименьшее возможное количество принадлежащих этой сети IP-адресов,
# в двоичной записи которых чётное число единиц.
'''
from ipaddress import *
R = []
for mask in range(32+1):
    net1 = ip_network(f'114.91.57.39/{mask}', 0)
    net2 = ip_network(f'114.91.19.61/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            s = f'{ip:b}'
            if s.count('1') % 2 == 0:
                cnt += 1
        R.append(cnt)
print(min(R))
'''

# endregion Разобрать: *************************************************************


# Олеся = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21 (кодом), 24, 25]
# КЕГЭ = []
# на следующем уроке: Вариант PRO100EGE 4 решить теорию Игр

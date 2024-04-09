
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Теория:
# Адрес сети = IP-адресу узла & Маска
# IP адрес это четыре числа разделенных точкой, на каждое такое число выделяется по 1 байту
# То есть числа лежат в диапазоне от 0 (00000000) до 255 (11111111) так как в 1 байте 8 бит

# Маска имеет длину 32 бита и вид: 11111...000, например: # 11111111.11111111.11110000.00000000

# КЕГЭ № 10777(Уровень: Базовый)
#
# По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 140.37.235.224 (10001100.00100101.11101011.11100000)
# Маска: 255.255.240.0
'''
knot = '.'.join([bin(int(x))[2:].zfill(8) for x in '140.37.235.224'.split('.')])
mask = '.'.join([bin(int(x))[2:].zfill(8) for x in '255.255.240.0'.split('.')])

address = ''
for i in range(len(knot)):
    if knot[i] == '1' and mask[i] == '1':
        address += '1'
    elif knot[i] == '.' and mask[i] == '.':
        address += '.'
    else:
        address += '0'

print(knot, mask, address, sep='\n')
# 10001100.00100101.11101011.11100000
# 11111111.11111111.11110000.00000000
# 10001100.00100101.11100000.00000000

print([int(x, 2) for x in address.split('.')])
# [140, 37, 224, 0]
'''
# Ответ: BFEH


# КЕГЭ № 10777(Уровень: Базовый)
#
# По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 140.37.235.224
# Маска: 255.255.240.0
'''
from ipaddress import *
net = ip_network('140.37.235.224/255.255.240.0', 0)
print(net)  # 140.37.224.0/20
'''
# Ответ: BFEH


# № 10778 (Уровень: Базовый)
# Для узла с IP-адресом 163.232.136.60 адрес сети равен 163.232.136.0.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'163.232.136.60/{mask}', 0)
    print(net, mask)
    # 163.232.136.0/21 21 где 21 - кол-во единиц в маске
    # 163.232.136.0/22 22
    # 163.232.136.0/23 23
    # 163.232.136.0/24 24
    # 163.232.136.0/25 25
    # 163.232.136.0/26 26
'''
# Ответ: 26


# КЕГЭ № 10776 (Уровень: Базовый)
#
# Для узла с IP-адресом 111.91.200.28 адрес сети равен 111.91.192.0.
# Найдите наименьшее возможное количество нулей в двоичной записи маски подсети.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    print(net, 32 - mask)

    # 111.91.192.0/18 14
    # 111.91.192.0/19 13
    # 111.91.192.0/20 12
'''
# Ответ: 12

'''
from ipaddress import *
mini = 9999
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    if str(net) == f'111.91.192.0/{mask}':
        mini = min(mini, 32 - mask)
print(mini)
'''
# Ответ: 12


# № 10773 (Уровень: Базовый)
# Для узла с IP-адресом 133.57.64.130 адрес сети равен 133.57.64.0.
# Для скольких различных значений маски это возможно?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'133.57.64.130/{mask}', 0)
    print(net)
    # 133.57.64.0/18
    # 133.57.64.0/19
    # 133.57.64.0/20
    # 133.57.64.0/21
    # 133.57.64.0/22
    # 133.57.64.0/23
    # 133.57.64.0/24
'''
# Ответ: 7

'''
from ipaddress import *
cnt = set()
for mask in range(32+1):
    net = ip_network(f'133.57.64.130/{mask}', 0)
    if str(net) == f'133.57.64.0/{mask}':
        cnt.add(mask)
print(len(cnt))
'''
# Ответ: 7


# КЕГЭ № 10715 (Уровень: Средний)
#
# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240.
# Сколько в этой сети IP-адресов, для которых количество нулей в двоичной записи IP-адреса больше 21?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('0') > 21:
        cnt += 1
print(cnt)
'''
# Ответ: 11


# № 10577 (Уровень: Базовый)
# Два узла, находящиеся в одной сети, имеют IP-адреса 165.112.200.70 и 165.112.175.80.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
maxi = 0
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        maxi = max(maxi, mask)
print(maxi)
'''


# КЕГЭ № 12088 (Уровень: Средний)
# Сеть задана IP-адресом 112.154.133.208 и маской сети 255.255.252.0.
# Сколько в этой сети узлов (устройств), для которых в двоичной записи
# IP-адреса суммарное количество единиц в левых двух байтах не больше
# суммарного нечётного количества нулей в правых двух байтах.
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('112.154.133.208/255.255.252.0', 0)
count = 0
for ip in net:
    s = f'{ip:b}'
    if s[17:].count('0') % 2 != 0:
        if s[:16].count('1') <= s[17:].count('0'):
            count += 1
print(count)
'''


# КЕГЭ № 11835 (Уровень: Средний)
# Сеть, в которой содержится узел с IP-адресом 207.0.A.167,
# задана маской сети 255.255.255.192, где A - некоторое допустимое для записи IP-адреса число.
# Определите количество значений A, для которых для всех IP-адресов этой сети в двоичной
# записи IP-адреса суммарное количество нулей в левых двух байтах больше
# суммарного количества нулей в правых двух байтах.
# В ответе укажите только число.
'''
from ipaddress import *
cnt = 0
for A in range(0, 255+1):
    net = ip_network(f'207.0.{A}.167/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0') for ip in net):
        cnt += 1
print(cnt)
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Василий = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 15, 17, 10, 3, 22

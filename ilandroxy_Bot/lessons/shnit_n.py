# region Домашка: ************************************************************
'''
for n in range(3, 10001):
    s = '5' + '2' * n
    while s.count('72') or s.count('522') or s.count('2222'):
        if s.count('72'):
            s = s.replace('72', '22', 1)
        if s.count('522'):
            s = s.replace('522', '25', 1)
        if s.count('2222'):
            s = s.replace('2222', '5', 1)
    if (s.count('2') * 2 + s.count('5') * 5 + s.count('7') * 7) == 63:
        print(n)
'''


# КЕГЭ № 10777 (Уровень: Базовый)
# По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 140.37.235.224
# Маска: 255.255.240.0
'''
from ipaddress import *
net = ip_network('140.37.235.224/255.255.240.0', 0)
print(net)  # 140.37.224.0/20
'''
# Ответ: BFEH


# КЕГЭ № 10778 (Уровень: Базовый)
# Для узла с IP-адресом 163.232.136.60 адрес сети равен 163.232.136.0.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'163.232.136.60/{mask}', 0)
    print(net, mask, net.netmask)
    # 163.232.136.0/21 21 255.255.248.0
    # 163.232.136.0/22 22 255.255.252.0
    # 163.232.136.0/23 23 255.255.254.0
    # 163.232.136.0/24 24 255.255.255.0
    # 163.232.136.0/25 25 255.255.255.128
    # 163.232.136.0/26 26 255.255.255.192
'''
'''
from ipaddress import *
R = []
for mask in range(32+1):
    net = ip_network(f'163.232.136.60/{mask}', 0)
    if str(net) == f'163.232.136.0/{mask}':
        # print(net, mask, net.netmask)
        R.append(mask)
print(max(R))
'''
# Ответ: 26


# КЕГЭ № 12922 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# Сеть задана IP-адресом 136.36.240.16 и маской сети 255.255.255.248.
# Сколько в этой сети IP-адресов, в которых в двоичной записи IP-адреса не встречается 101?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if '101' not in s:
        cnt += 1
print(cnt)
'''
# Ответ: 4


# КЕГЭ № 10577 (Уровень: Базовый)
# Два узла, находящиеся в одной сети, имеют IP-адреса 165.112.200.70 и 165.112.175.80.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
R = []
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        R.append(mask)
print(max(R))
'''
# Ответ: 17

# endregion Домашка: ************************************************************

# region Урок: **************************************************************

# endregion Урок: ************************************************************


# region Разобрать: ***************************************************************

# endregion Разобрать: *************************************************************

# Никита = [3, 5, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:

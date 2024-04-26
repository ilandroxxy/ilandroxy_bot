# region Домашка: ************************************************************

# КЕГЭ № 10577 (Уровень: Базовый)
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
# Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
#
# Два узла, находящиеся в одной сети, имеют IP-адреса 165.112.200.70 и 165.112.175.80.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
maxi = 0
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        # print(net1, mask, net1.netmask)
        maxi = max(maxi, mask)
print(maxi)
'''
# Ответ: 17

# endregion Домашка: *********************************************************


# region Урок: ************************************************************


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Максим = [2, 3, 6, 5, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:

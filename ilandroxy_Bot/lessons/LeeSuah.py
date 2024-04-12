# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

print('x y z w')
for x in range(0, 2):
 for y in range(0, 2):
  for z in range(0, 2):
   for w in range(0, 2):
    if ((x or y) <= (y and z)) and ((w == z) or (w <= (not z))):
     print(x, y, z, w)

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
# на следующем уроке:

# region Домашка: ******************************************************************

from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for i in net:
    s = f'{i:b}'
    if '101' not in s:
        cnt += 1
print(cnt)

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Данил = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

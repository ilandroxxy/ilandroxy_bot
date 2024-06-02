# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

# № 12721 (Уровень: Базовый)
'''
R = []
for n in range(80, 1000):
    s = f'{n:o}'  # s = oct(n)[2]
    chet = [x for x in s if x in '02468']
    if len(chet) % 2 != 0:
        s = s[-3:] + '46'
    else:
        x = (n % 8) * 5
        s = oct(x)[2:] + s
    r = int(s, 8)
    R.append(r)
print(min(R))
'''

'''
def convert(num, base):
    res = ''
    while num > 0:
        res += str(num % base)
        num //= base
    return res[::-1]


R = []
for n in range(80, 1000):
    s = convert(n, 8)
    chet = [x for x in s if x in '02468']
    if len(chet) % 2 != 0:
        s = s[-3:] + '46'
    else:
        x = (n % 8) * 5
        s = convert(x, 8) + s
    r = int(s, 8)
    R.append(r)
print(min(R))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res += alphabet[num % base]
        num //= base
    return res[::-1]


R = []
for n in range(80, 1000):
    s = convert(n, 8)
    chet = [x for x in s if x in '02468']
    if len(chet) % 2 != 0:
        s = s[-3:] + '46'
    else:
        x = (n % 8) * 5
        s = convert(x, 8) + s
    r = int(s, 8)
    R.append(r)
print(min(R))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res += alphabet[num % base]
        num //= base
    return res[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0] + '1'
    else:
        s += str(n % 3)
    r = int(s, 4)
    if r <= 340:
        R.append(r)
print(max(R))
'''

'''
def convert(num, base):
    res = []
    while num > 0:
        res.append(num % base)
        num //= base
    return res[::-1]

x = 2*729**2014 + 2*243**2016-2*81**2018+2*27**2020 - 2*9**2022 - 2024
s = convert(x, 27)
print(len([i for i in s if i > 9]))
'''

# Вариант 2
'''
num = 2*729**2014 + 2*243**2016-2*81**2018+2*27**2020 - 2*9**2022 - 2024
res = []
while num > 0:
    res.append(num % 27)
    num //= 27
print(len([i for i in res if i > 9]))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:27]:
    A = int(f'123{x}24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''
# Ответ: 1213206


# № 16379 ЕГКР 27.04.24 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('112.208.0.0/255.255.128.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 11 == 0:
        cnt += 1
print(cnt)
'''
# Ответ: 3003


'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)
    if net1 != net2:
        print(net1.netmask)
'''

'''
from ipaddress import *
for A in range(0, 256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break
'''

'''
maxi = 0
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum([int(x) for x in s])
    if maxi < summa:
        maxi = summa
        print(maxi)
'''

'''
R = []
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum([int(x) for x in s])
    R.append(summa)
    print(max(R))
'''

# № 12729 (Уровень: Базовый)
'''
for n in range(1, 1000):
    s = '3' + '9' * n + '5' * n
    while '39' in s or '35' in s or '555' in s:
        if '39' in s:
            s = s.replace('39', '55', 1)
        if '35' in s:
            s = s.replace('35', '9', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    summa = sum([int(x) for x in s])
    if summa % len(s) == n:
        print(n)
'''
# Ответ: 54

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Екатерина = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 12, 13, 14]
# на следующем уроке:

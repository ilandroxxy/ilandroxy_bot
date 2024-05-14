
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# s = '12345'
# print(s[2:])  # 345
# print(s[-2:])  # 45
'''
R = []
for n in range(1, 1000):
    s = bin(n)[2:]  # s = f'{n:b}'
    if n % 3 == 0:
        s += s[-2:]
    else:
        s += bin((n % 3) * 3)[2:]
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''
# Ответ: 199


'''
from math import *
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(not_copied) == 5:
        if prod(sorted(not_copied)[:3]) > prod(copied):
            cnt += 1
print(cnt)
'''

'''
from ipaddress import *
net = ip_network(f'112.208.0.0/255.255.128.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 11 == 0:
        cnt += 1
print(cnt)
'''

'''
from math import *
M = [1, 2, 3, 4, 5]
print(sum(M))  # 15 - сумма чисел списка
print(prod(M))  # 120 - произведение чисел списка
'''

'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''
# Ответ: 196


M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-2:] == '21' and len(str(x)) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i:i+2]
    if (str(x)[-2:] == '21' and len(str(abs(x))) == 5) != (str(y)[-2:] == '21' and len(str(abs(y))) == 5):
        if x ** 2 + y ** 2 >= max(A) ** 2:
            R.append(x + y)
print(len(R), max(R))

M = [int(x) for x in open('17.txt')]
D = [int(x) for x in M if str(x)[-2:] == '21' and len(str(abs(x)))==5 ]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in D and y not in D) or (y in D and x not in D):
        if (x**2)+(y**2) >= max(D)**2:
            R.append(x + y)
print(len(R), max(R))


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Геля = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 13, 14, 18, 19-21, 22, 23]
# на следующем уроке: 17, 24, 25

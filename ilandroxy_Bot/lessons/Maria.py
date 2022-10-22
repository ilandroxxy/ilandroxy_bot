# Домашка

# Список кубов
"""
M = []
n = int(input('n: '))
for i in range(n):
    x = int(input())
    M.append(x ** 3)
print(M)
"""

# Список букв
"""
n = int(input())
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if n <= 36:
    print(s[:n])

n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
M = []
for i in range(0, n):
    M.append(s[i])
print(M)
"""


# Сумма двух списков
'''
L = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

S = []
for i in range(0, len(M)):
    S.append(L[i] + M[i])
print(S)
'''


# Тип 14 № 36869
'''
# Значение выражения 729**8 − 3**18 + 85 записали в системе счисления с основанием 9.
# Сколько раз в этой записи встречается цифра 0?

x = 729**8 - 3**18 + 85
M = []
while x > 0:
    M.append(x % 9)
    x //= 9
M.reverse()
print(M.count(0))
'''
# Ответ: 7



# Тип 14 № 17380
# Значение выражения 3*216**4 + 2*36**6 − 648 записали в системе счисления с основанием 6.
# Сколько цифр 5 содержится в этой записи?

x = 3*216**4 + 2*36**6 - 648
M = []
while x > 0:
    M.append(x % 6)
    x //= 6
M.reverse()
print(M.count(5))
# Ответ: 8



# todo: на следующем уроке разбираем 14, 5 номер

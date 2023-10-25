
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Списки и строки
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')

s = 'abcde'
print(f'Первый элемент списка: {s[0]} \n'
      f'Последний элемент списка: {s[-1]}')

print(len(M))  # 5 - функция len() возвращает длину списка (кол-во элементов)

for i in range(0, len(M)):
    print(M[i], end=' ')
print()

for i in range(0, len(s)):
    print(s[i], end=' ')
print()
'''

# Разница между списками и строками - в том, что в строках нельзя менять элементы по индексам
'''
for i in range(0, len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

'''
M = [1, 2, 3, 4, 5]
M[2] = '*'
print(M)  # [1, 2, '*', 4, 5]

s = '12345'
s = s[:2] + '*' + s[3:]
print(s)  # '12*45'

print(' '.join([x for x in s]))  # 1 2 * 4 5
'''

# Срезы списков и строк
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[1:3])  # ['b', 'c']
print(M[:3])  # ['a', 'b', 'c'] - все, что слева до 3-1
print(M[2:])  # ['c', 'd', 'e'] - все, что справа от 2
print(M[:])  # ['a', 'b', 'c', 'd', 'e'] - от левого до правого
print(M[0:5])
print(M[::])
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] - разворачивает список наоборот

s = 'abcde'
print(s[::-1])  # edcba
'''


# Функции списков и строк
'''
M = [4, 6, 2, 3, 4, 6]

print(len(M))
print(sum(M))
print(max(M))
print(min(M))

print(sorted(M))  # [2, 3, 4, 4, 6, 6]
print(sorted(M, reverse=True))  # [6, 6, 4, 4, 3, 2]

print(set(M))  # {2, 3, 4, 6} - удовлетворяет условию "сколько различных значений"


s = '462346'
print(len(s))
print(max(s))
print(min(s))

print(sorted(s))  # ['2', '3', '4', '4', '6', '6']
print(sorted(s, reverse=True))  # ['6', '6', '4', '4', '3', '2']

print(set(s))    # {'2', '3', '6', '4'}
'''


# Методы списков
'''
M = [1, 2, 3, 12, 3, 23, 12, 2, 3, 12, 3]

print(M.count(3))  # 4 - кол-во вхождений элемента в список
print(M.index(3))  # 2 - возвращает индекс первой тройки

M.append(100)  # добавил 100 в конец списка
print(M)  # [1, 2, 3, 12, 3, 23, 12, 2, 3, 12, 3, 100]

M += [1, 2, 3]
print(M)  # [1, 2, 3, 12, 3, 23, 12, 2, 3, 12, 3, 100, 1, 2, 3]

M.sort()
print(M)  # [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 12, 12, 12, 23, 100]

M.reverse()
print(M)  # [100, 23, 12, 12, 12, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1]
'''

# Методы строк
'''
s = 'asbdasbdbasdbasbd'

print(s.count('d'))  # 4
print(s.index('d'))  # 3
print(s.rindex('d'))  # 16
print(s.isdigit())  # False

print(s.replace('d', '*'))  # asb*asb*bas*basb*
print(s)  # asbdasbdbasdbasbd

s = s.replace('d', '*')
print(s)   # asb*asb*bas*basb*

s = s.replace('*', 'd', 2)
print(s)  # asbdasbdbas*basb*

s = '12345trfw3e4rfew34'
print(sum([int(x) for x in s if x.isdigit()]))  # 29

s = s.upper()
print(s)
s = s.lower()
print(s)

ip = '123.42.56.9'
print(ip.split('.'))  # ['123', '42', '56', '9']  # разбивает строку на список строк
IP = [int(x) for x in ip.split('.')]
print(IP)  # [123, 42, 56, 9]

new_ip = '*'.join(ip.split('.'))  # склеивает список строк в общую строчку 
print(new_ip)  # 123*42*56*9
'''

# генераторы списков
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

M = [x**2 for x in range(10) if x % 2 != 0]
print(M)  # [0, 4, 16, 36, 64]

M = [int(x) for x in input('Введите числа через пробел: ').split()]
print(M)
# endregion Урок: ******************************************************************


# todo: Лиза = [2.1, 6.1]
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:

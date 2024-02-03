# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Циклы в Пайтон

# for - отвечает запросам: "повтори n раз", "пройди от А дол В"
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(8):  # range(START=0, STOP=8-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7
print()


for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]
for i in range(len(M)):  # len(M) - вернет длину (кол-во элементов) в списке М
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # 1 2 3 4 5
print()


# Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45

M = [1, 2, 3, 4, 5]
for i in range(len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')  # 12 23 34 45
print()

# Назовём тройкой три идущих подряд элемента последовательности.
for i in range(len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')  # 123 234 345
print()

# Можно пробегать последовательности напрямую
M = [1, 2, 3, 4, 5]
for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 2 4
print()

# Через range() мы можем изменять элементы списков
M = [1, 2, 3, 4, 5]
for i in range(len(M)-1):
    M[i] = M[i] ** 2
print(M)   # [1, 4, 9, 16, 5]
'''


# while - отвечает запросам: "выполняй действие, пока условие истинно", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''

# Перевод числа из 10-ной в n-ную систему счисления
# 8_10 = 1000_2
'''
num = int(input())
system = int(input())
N = []
while num > 0:
    N.append(num % system)
    num //= system
N.reverse()
print(N)
'''

'''
num = int(input())
system = int(input())
s = ''
while num > 0:
    s += str(num % system)
    num //= system
s = s[::-1]
print(s)  # 1000
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
num = int(input())  # 12345678976543213
system = int(input())  # 20
s = ''
while num > 0:
    s += alphabet[num % system]
    num //= system
s = s[::-1]
print(s)  # 305CD1E037I0D
'''
'''
print(int('305CD1E037I0D', 20))
'''


# Бесконечный цикл
'''
k = 0
while True:
    k += 1
    print(k)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('case 1: Перевод из 10-ой в n-ую систему счисления \n'
                 'case 2: Перевод из n-ой в 10-ую систему счисления \n'
                 'case 3: Перевод из n-ой в k-ую систему счисления \n'
                 'case 0: exit\n')

    if case == '1':
        num = int(input('Введите 10-е число: '))
        system = int(input('Введите n-ую систему счисления: '))  # 20
        ex_num = num
        s = ''
        while num > 0:
            s += alphabet[num % system]
            num //= system
        s = s[::-1]
        print(f'Число {ex_num} при переводе в {system}-ую систему счисления дает результат: {s} \n\n')

    elif case == '2':
        system = int(input('Введите n-ую систему счисления: '))
        s = input(f'Введите число в {system}-ой системе счисления: ')
        num = int(s, system)
        print(f'При переводе числа {s} из {system}-ой системы счисления, получили: {num} \n\n')

    elif case == '3':
        system_n = int(input('Введите n-ую систему счисления: '))
        s = input(f'Введите число в {system_n}-ой системе счисления: ')
        system_k = int(input('Введите k-ую систему счисления: '))
        num = int(s, system_n)
        ex_num = num
        s = ''
        while num > 0:
            s += alphabet[num % system_k]
            num //= system_k
        s = s[::-1]
        print(f'Число {ex_num} при переводе из {system_n}-ой в {system_k}-оую системы получили: {s} \n\n')

    elif case == '0':
        break
'''


# Тип 14 №7460
# Сколько единиц содержится в двоичной записи значения выражения: 4**2014 + 2**2015 - 8?
'''
x = 4**2014 + 2**2015 - 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M.count(1))  # 2013

# Вариант 2
print(bin(4**2014 + 2**2015 - 8)[2:].count('1'))  # .count() - возвращает кол-во вхождений 
'''
# Ответ: 2013


# Тип 14 №27385
# Значение выражения 343**5 + 343**4 + 49**6 - 7**13 - 21 записали в системе счисления с основанием 7.
# Сколько различных цифр содержит эта запись?
'''
x = 343**5 + 343**4 + 49**6 - 7**13 - 21
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(set(M))  # {0, 1, 4, 6}
print(len(set(M)))  # 4
'''
# Ответ: 4

# endregion Урок: ******************************************************************

# Данил = []
# КЕГЭ  = []
# на следующем уроке:

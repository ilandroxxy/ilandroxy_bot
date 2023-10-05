# region Домашка: ***************************************************************

'''
a = input()
b = int(input())
for i in range(b):
    print(a)
'''

'''
n = int(input())
for i in range(n + 1):  # range(START=0, STOP=10, STEP=1)
    # print('Квадрат числа', i, 'равен', i**2)
    print(f'Квадрат числа {i} равен {i ** 2}')
'''
'''
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())
'''

'''
while True:
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        break
'''
'''
a = int(input())
summ = 0
while a >= 0:
    summ += a
    a = int(input())
print(summ)
'''
'''
a = int(input())
count = 0
while 0 <= a <= 55:
    if a == 5:
        count += 1
    a = int(input())
print(count)
'''
# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Перевод из 10-ной в 2-ную.
'''
x = int(input('x: '))
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()  # развернуть список в обратном порядке
print(M)  # [0, 0, 0, 1]


x = int(input('x: '))
s = ''
while x > 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]  # развернуть строчку в обратном порядке
print(s)
'''

'''
# Как получить отсортированный алфавит цифр + букв

# 1.
import string
alphabet1 = string.digits + string.ascii_uppercase

print(alphabet1)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

# 2.
alphabet2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

# Калькулятор перевода из 10-ной в n-ную
x = int(input('Введите число в 10-ной: '))
n = int(input('Введите n-ную систему: '))
s = ''
while x > 0:
    s += alphabet1[x % n]
    x //= n
s = s[::-1]  # развернуть строчку в обратном порядке
print(s)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('\n\ncase 1: Перевод из 10-ной в n-ную систему \n'
                 'case 2: Перевод из n-ной в 10-ную систему \n'
                 'case 3: Перевод из k-ной в n-ную систему \n'
                 'case 0: exit \n\n')
    if case == '1':
        x = int(input('Введите число в 10-ной: '))
        n = int(input('Введите n-ную систему: '))
        s = ''
        x10 = x
        while x > 0:
            s += alphabet[x % n]
            x //= n
        s = s[::-1]  # развернуть строчку в обратном порядке
        print(f'Результат перевода числа {x10} в {n}-ную систему счисления: {s}')

    elif case == '2':
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе счисления: ')
        x = int(s, n)  # встроенная функция для перевода из n-ной системы в 10-ную
        print(f'Результат перевода числа {s} из {n}-ной системы счисления в 10-ную: {x}')

    elif case == '3':
        k = int(input('Введите k-ую систему счисления: '))
        s = input(f'Введите число в {k}-ой системе счисления: ')
        n = int(input('Введите n-ую систему счисления: '))

        x = int(s, k)

        r = ''
        while x > 0:
            r += alphabet[x % n]
            x //= n
        r = r[::-1]  # развернуть строчку в обратном порядке
        print(f'Результат перевода числа {s} из {k}-ой в {n}-ную систему счисления: {r}')

    elif case == '0':
        break
'''
# endregion Урок: ***************************************************************


# todo: Анастасия = [1.1, 2.1, 3.1, 4.1, 5.1, 7.1, 11.1, 12.1, 13.1, 14.1]
# todo:  КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:

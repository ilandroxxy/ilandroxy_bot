
# region Домашка: ******************************************************************

'''
s = input()
n = int(input())
for _ in range(n):
    print(s)
'''

'''
for n in range(int(input() + 1)):
    print(f'Квадрат числа {n} равен {n**2}')
'''

'''
while True:
    x = int(input())
    if x % 7 == 0:
        print(x)
    else:
        break
'''
'''
R = []
while True:
    x = int(input())
    if x >= 0:
        R.append(x)
    else:
        break
print(sum(R))
'''

'''
count = 0
while True:
    x = int(input())
    if x < 0 or x > 55:
        break
    if x == 5:
        count += 1
print(count)
'''

'''
ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# Напишем маленький калькулятор систем счисления:
while True:
    case = input('\ncase 1: Перевод из 10-ной в n-ную систему счисления \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления \n'
                 'case 3: Перевод из k-ой в n-ную систему счисления \n'
                 'case 0: exit \n')
    if case == '1':
        x = int(input('Введите 10-ное число: '))
        x2 = x
        n = int(input('Ведите n-ную систему счисления: '))
        s = ''
        while x2 > 0:
            s += ALPHABET[x2 % n]
            x2 //= n
        s = s[::-1]
        print(f'Результат перевода числа {x} из 10-ной в {n}-ную систему: {s}')

    elif case == '2':
        n = int(input('Ведите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе счисления: ')
        x = int(s, n)  # то это встроенная функция для перевода из n-ной системы счисления в 10-ную
        print(f'Результат перевода числа {s} из {n}-ной в 10-ную систему: {x}')

    elif case == '3':
        k = int(input('Ведите k-ую систему счисления: '))
        c = input(f'Введите число в {k}-ой системе счисления: ')
        x = int(c, k)

        n = int(input('Ведите n-ную систему счисления: '))
        s = ''
        while x > 0:
            s += ALPHABET[x % n]
            x //= n
        s = s[::-1]
        print(f'Результат перевода числа {c} из {k}-ой в {n}-ную систему: {s}')

    elif case == '0':
        break
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 2 №16805
# Логическая функция F задаётся выражением (¬x≡z)→(y≡(w∨x)).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in [0, 1]:
                # F = ((not x) == z) <= (y == (w or x))
                F = ((not x) == z) <= (y == (w or x))
                if F == False:
                    print(x, y, z, w, int(F))

# endregion Урок: ******************************************************************


# todo: Екатерина = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:

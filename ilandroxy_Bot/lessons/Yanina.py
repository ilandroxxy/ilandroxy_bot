

import math
M = [i for i in input('Введите две дроби и знак операции между ними: ').split()]  # 1 2 + 3 4  ,    5 6 + 3 10

a = int(M[0])
b = int(M[1])
s = M[2]
m = int(M[3])
n = int(M[4])

# region Операция сложения дробей
if s == '+':
    NOK = math.lcm(b, n)

    a = a * (NOK // b)
    m = m * (NOK // n)
    znam = n * (NOK // n)

    print(f'{a}/{znam} {s} {m}/{znam}')

    print(f'{a + m}/{znam}')

    cel = (a + m) // znam
    ost = (a + m) % znam

    NOD = math.gcd(ost, znam)

    if cel != 0:
        print(f'{cel} ({ost // NOD}/{znam // NOD})')
    else:
        print(f'({ost // NOD}/{znam // NOD})')
# endregion Операция сложения дробей

# region Операция вычитание дробей
elif s == '-':
    NOK = math.lcm(b, n)

    a = a * (NOK // b)
    m = m * (NOK // n)
    znam = n * (NOK // n)

    print(f'{a}/{znam} {s} {m}/{znam}')

    print(f'{a - m}/{znam}')

    cel = (a - m) // znam
    ost = (a - m) % znam

    NOD = math.gcd(ost, znam)

    if cel != 0:
        print(f'{cel} ({ost // NOD}/{znam // NOD})')
    else:
        print(f'({ost // NOD}/{znam // NOD})')
# endregion Операция вычитание дробей

# region Операция умножения дробей
elif s == '*':
    NOK = math.lcm(b, n)

    x = a * m
    znam = b * n

    print(f'{x}/{znam}')

    cel = (x) // znam
    ost = (x) % znam

    NOD = math.gcd(ost, znam)

    if cel != 0:
        print(f'{cel} ({ost // NOD}/{znam // NOD})')
    else:
        print(f'({ost // NOD}/{znam // NOD})')
# endregion Операция умножения дробей

# region Операция Деления дробей
elif s == '/':
    NOK = math.lcm(b, n)

    x = a * n
    znam = b * m

    print(f'{x}/{znam}')

    cel = (x) // znam
    ost = (x) % znam

    NOD = math.gcd(ost, znam)

    if cel != 0:
        print(f'{cel} ({ost // NOD}/{znam // NOD})')
    else:
        print(f'({ost // NOD}/{znam // NOD})')

# endregion Операция Деления дробей

# todo: НОД, НОК, Квадратное уравнение, Квадратный корень, Кубический корень, Факториал, Среднее арифметическое
# todo: На следующем уроке: В боте правим команды разность, умножение и деление. Оформляем авторов и придумываем новые команды.


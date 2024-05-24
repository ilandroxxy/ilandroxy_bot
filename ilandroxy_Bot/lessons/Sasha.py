# region Домашка: ************************************************************

# endregion Домашка: ************************************************************


# region Урок: *************************************************************


# Первый прототип:

# Тип 1 №10859
'''
one_symbols = 4  # байт
rivers = 'Нил, Амур, Волга, Ангара, Макензи, Амазонка'.split(', ')
search = 32 - (2 * one_symbols)
for elem in rivers:
    if len(elem) == (search / one_symbols):
        print(elem)
'''

# Тип 1 №10310
'''
one_symbols = 2  # байт
D = 'Уфа, Азов, Пермь, Белово, Вологда, Камбарка, Соликамск'.split(', ')
search = 22 - (2 * one_symbols)
for elem in D:
    if len(elem) == (search / one_symbols):
        print(elem)
'''

# Второй прототип:

# Тип 1 №18031
'''
one_symbols = 1  # байт
D = 'Мой дядя самых честных правил Когда не в шутку занемог'.split()
search = 5 - one_symbols
for elem in D:
    if len(elem) == (search / one_symbols):
        print(elem)


one_symbols = 1  # байт
D = 'Скользя по утреннему снегу Друг милый предадимся бегу Нетерпеливого коня И навестим поля пустые'.split()
search = 8 - one_symbols
for elem in D:
    if len(elem) == (search / one_symbols):
        print(elem)
'''

'''
from itertools import *
my_dict = {'01': 'А', '011': 'В', '100': 'Д', '111': 'О', '010': 'Р', '001': 'У'}
codes = ('01001001', '11101001', '10001010')
symb = '01 011 100 111 010 001'.split()
for l in range(1, 6+1):
    for per in product(symb, repeat=l):
        s = ''.join(per)
        for code in codes:
            if s == code:
                print(per)
                for elem in per:
                    if my_dict.get(elem):
                        print(my_dict[elem], end=' ')
                print(code)
                print('-----------------')
'''
# Ответ: 10001010


'''
for x in range(1, 100):
    if (not(x < 6) and (x % 2 != 0)) == True:
        print(x)
        break
'''
# Ответ: 7

# Тип 3 №18287
'''
for x in range(1, 100):
    if ((x > 3) or not(x > 2)) == False:
        print(x)
        break
'''
# Ответ: 3

# Тип 3 №10875
'''
R = []
for x in range(1, 100):
    if (not(x <= 11) and not(x >= 17)) == True:
        R.append(x)
print(max(R))
'''
# Ответ: 16


# Тип 3 №35575
'''
R = []
for x in range(1, 100):
    if (not(x > 15) and not(x % 2 == 0)) == True:
        R.append(x)
print(len(R))
'''
# Ответ: 8


# Тип 5 №10885
'''
stop = 17
for b in range(3, 1000):
    start = 41
    start += 4
    start /= b
    start += 4
    start += 4
    start += 4
    if start == stop:
        print(b)
'''

'''
def F(start, stop, command, track):
    if start > stop or command > 5:
        return 0
    elif start == stop and command <= 5:
        print(track)
        return (start == stop)
    return F(start**2, stop, command+1, track+'1') + F(start+3, stop, command+1, track+'2')

print(F(1, 25, 0, ''))
'''

def F(a, b, c, t):
    if a > b or c > 5:
        return 0
    elif a == b and c <= 5:
        print(t)
        return 1
    return F(a**2, b, c+1, t+'1') + F(a+3, b, c+1, t+'2')

F(1, 25, 0, '')


# Тип 5 №16013
def F(a, b, t):
    if a > b or len(t) > 5:
        return 0
    elif a == b and len(t) <= 5:
        print(t)
        return 1
    else:
        return F(a**2, b, t+'1') + F(a+3, b, t+'2')

F(1, 25, '')  # 21222


# Тип 5 №18289

def F(a, b, t):
    if a < b or len(t) > 5:
        return 0
    elif a == b and len(t) <= 5:
        print(t)
        return 1
    else:
        return F(a / 2, b, t+'1') + F(a-1, b, t+'2')

F(65, 4, '')  # 21111


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Александра = []
# КЕГЭ = []
# на следующем уроке:

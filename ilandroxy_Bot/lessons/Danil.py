# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Вариант 1
s = '012345'
count = 0
for i in '12345':
    for d in s:
        for c in s:
            for z in s:
                for f in s:
                    for g in s:
                        slovo = i + d + c + z + f +g
                        if slovo.count('2') == 1:
                            if '12'not in slovo:
                                if '21'not in slovo:
                                    if '32' not in slovo:
                                        if '23' not in slovo:
                                            if '52' not in slovo:
                                                if '25' not in slovo:
                                                    count +=1
print(count)

# Вариант 2
s = '012345'
count = 0
for i in '12345':
    for d in s:
        for c in s:
            for z in s:
                for f in s:
                    for g in s:
                        slovo = i + d + c + z + f +g
                        if slovo.count('2') == 1:
                            if all(x not in slovo for x in '12 21 32 23 52 25'.split()):
                                count +=1
print(count)

# Вариант 3
import itertools
count = 0
for s in itertools.product('012345', repeat=6):
    slovo = ''.join(s)
    if slovo.count('2') == 1 and slovo[0] != '0':
        if all(x not in slovo for x in '12 21 32 23 52 25'.split()):
            count += 1
print(count)

# endregion Урок: ******************************************************************************


# todo: Данил = [2, 3, 5, 7.1, 8, 9.1, 12, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25.2]
# на прошлом уроке: Даниил сам прорешивал часть номеров, с варианта
# на следующем уроке:

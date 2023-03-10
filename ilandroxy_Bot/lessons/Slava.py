
# region Домашка: ******************************************************************************


# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

# № 5888 Danov2301 (Уровень: Сложный)
# (А.Богданов) Строка содержит символы латинского алфавита.
# Определите максимальную длину подстроки не содержащей подстрок, отличающейся от «DANOV» лишь на одну букву.
'''
s = open('24.txt').readline()
count = 4
Maxcount = 0
for i in range(0, len(s)-4):
    if (int(s[i] == 'D') + int(s[i+1] == 'A') + int(s[i+2] == 'N') + int(s[i+3] == 'O') + int(s[i+4] == 'V')) == 4:
        count = 4
    else:
        count += 1
        Maxcount = max(Maxcount, count)
print(Maxcount)
'''
# 229549


#
# № 4549 (Уровень: Сложный)
# Текстовый файл содержит строку из набора A, B, C, D, E, F, всего не более чем из 106 символов.
# Найдите максимальное количество подряд идущих троек символов ABC, BAC, CAB, CBA,
# стоящих одна за другой и пересекающихся с соседними тройками одной буквой.
# Например, в строке BDEABCBABCABBD такие пары составляют подстроку ABCBABCAB = ABC + СBA + ABC + CAB, итого 4 тройки.
'''
s = open('24.txt').readline()
s = s.replace('D', ' ').replace('E', ' ').replace('F', ' ')
s = s.replace('AA', ' ').replace('BB', ' ').replace('CC', ' ')
while 'ABCAB' in s or 'ABCBA' in s or 'BACAB' in s or 'BACAB' in s or 'CABAC' in s or 'CBABC' in s:
    s = s.replace('ABCAB', 'ABC*CAB')
    s = s.replace('ABCBA', 'ABC*CBA')
    s = s.replace('BACAB', 'BAC*CAB')
    s = s.replace('BACBA', 'BAC*CBA')
    s = s.replace('CABAC', 'CAB*BAC')
    s = s.replace('CBABC', 'CBA*ABC')
print(s)
M = [len(i) for i in s.split()]
print(max(M))
'''


# № 6087 /dev/inf 02.2023 (Уровень: Сложный)
# (А. Рогов) На числовой прямой даны три отрезка: D = [15; 40], C = [21; 63] и А = [7; E].
# Укажите наименьшее возможное целое значение E такое, что формула
#
# (x ∈ D) → ((¬(x ∈ C) /\ ¬(x ∈ A)) → ¬(x ∈ D))
#
# истинна (то есть принимает значение 1 при любом значении переменной х).
'''
def F(x):
    D = 15 <= x <= 40
    C = 21 <= x <= 63
    A = 7 <= x <= E
    return D <= (((not C) and (not A)) <= (not D))

M = [i/4 for i in range(10*4, 70*4)]
for E in M:
    if all(F(x) for x in M):
        print(E)
        break
'''
# Ответ: 21

message_text = open('9.txt').read()
numbers = max([int(i) for i in message_text.replace(')', ' ').replace('(', ' ').split() if i.isdigit()][:2])

print(type(numbers))

# endregion Урок:  ******************************************************************************

# Слава
# todo: РЕШУ ЕГЭ = [1, 2, 5, 6, 8, 9, 12, 13, 14+, 15+, 16, 17, 18, 19-21, 23, 24+, 25.2]
# todo: КЕГЭ [1, 5, 8, 9, 13, 14, 17, 24, 25] # рассмотреть: 6, 9, 22, 17 КЕГЭ
# на прошлом уроке: Прорешивали вариант из демо версии СБП
# на следующем уроке:
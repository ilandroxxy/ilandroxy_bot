# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 3 раз.
'''
s = 'xxxxxxxxxxxTxxxxxxxTxxTxxxxxTxxxxTxxxxxxTxxxxxxxTxxxxxxxxxxTxxxxxxx'
# ['xxxxxxxxxxx', 'xxxxxxx', 'xx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxxxx', 'xxxxxxx']
# xxxxxxxxxxxTxxxxxxxTxxTxxxxx 28
# xxxxxxxTxxTxxxxxTxxxx 21
# xxTxxxxxTxxxxTxxxxxx 20
# xxxxxTxxxxTxxxxxxTxxxxxxx 25
# xxxxTxxxxxxTxxxxxxxTxxxxxxxxxx 30
# xxxxxxTxxxxxxxTxxxxxxxxxxTxxxxxxx 33

s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
    print(r, len(r))
print(maxi)
'''

# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 133


# Определите минимальную длину подстроки, содержащую ровно 3 символов T.
# Для выполнения этого задания следует написать программу.
'''
s = 'xxxxxxxxxxxTxxxxxxxTxxTxxxxxTxxxxTxxxxxxTxxxxxxxTxxxxxxxxxxTxxxxxxx'
# ['xxxxxxxxxxx', 'xxxxxxx', 'xx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxxxx', 'xxxxxxx']
# TxxxxxxxxxxxTxxxxxxxT 21
# TxxxxxxxTxxT 12
# TxxTxxxxxT 10
# TxxxxxTxxxxT 12
# TxxxxTxxxxxxT 13
# TxxxxxxTxxxxxxxT 16
# TxxxxxxxTxxxxxxxxxxT 20
# TxxxxxxxxxxTxxxxxxxT 20

s = s.split('T')
mini = 9999999
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(r, len(r))
    mini = min(mini, len(r))
print(mini)
'''


# Тип 24 №59794
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную длину подстроки, содержащую ровно 110 символов "U".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('U')
mini = 99999
for i in range(len(s)-108):
    r = 'U' + 'U'.join(s[i:i+109]) + 'U'
    mini = min(mini, len(r))
print(mini)
'''
# Ответ: 1765


#
# № 12476 PRO100 ЕГЭ 29.12.23 (Уровень: Сложный)
# Текстовый файл состоит из символов P, R, O, E, G – зашифрованное письмо Деду Морозу.
#
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых комбинация
# символов RO встречается ровно 21 раз, а комбинации символов ORO и ROR ни разу не встречаются.
'''
s = open('24.txt').readline().split('RO')
maxi = 0
for i in range(len(s)-21):
    r = 'RO'.join(s[i:i+22])
    if 'ORO' not in r and 'ROR' not in r:
        maxi = max(maxi, len(r))
print(maxi)
'''

# endregion Урок: *******************************************************************


# region Разобрать: *************************************************************


# todo разобрать Марк № 14100 (Уровень: Средний)
# (П. Говоров) В файле содержится строка длиной не более 106 из букв A,B,C.
# Определите в прилагаемом файле максимальную длину подпоследовательности, составленную конкатенацией из
# следующих подстрок (могут использоваться любое количество раз): ABA, CB, AC, BB, ABC, BCB, BA, AB.
'''
s = open('24.txt').readline()
dp = [0] * len(s)
prim = ['ABA', 'CB', 'AC', 'BB', 'ABC', 'BCB', 'BA', 'AB']

for i in range(1, len(s)):
    for j in prim:
        if i >= len(j) - 1:
            if s[i - len(j) + 1:i + 1] == j:
                dp[i] = max(dp[i], dp[i - len(j)] + len(j))
print(max(dp))


# наше решение:
s = open('24.txt').readline()
maxi = 0
for a in "ABA CB AC BB ABC BCB BA AB".split():
    s = s.replace(a, '*' * len(a))
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))
'''


# todo Разобрать Марк почему ответ не сходится № 13715 (Уровень: Средний)
# Текстовый файл состоит из символов A, B, C, D и E.
#
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых комбинация символов AB встречается ровно 50 раз.
'''
s = open('24.txt').readline().split('AB')
maxi = 0
for i in range(len(s)-50):
    r = 'AB'.join(s[i:i+51])
    print(len(r), r.count('AB'), r)
    maxi = max(maxi, len(r))
print(maxi)
'''

# todo Придумать как быть с незначащими нулями Марк № 10724 (Уровень: Базовый)
'''
s = open('24.txt').readline()
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')[16:]
for a in alphabet:
    s = s.replace(a, ' ')
maxi = 0
for x in s.split():
    if x[0] != '0':
        if maxi < len(x):
            maxi = len(x)
            print(maxi, x)
print(maxi)
'''

# endregion Разобрать: *************************************************************


# Марк = [1, 2, 3, 6, 4, 5, 7, 8, 9, 12, 14, 15, 16, 17, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 14, 16, 23, 24, 25]
# на следующем уроке:

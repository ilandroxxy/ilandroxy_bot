# region Домашка: ************************************************************

# endregion Домашка: *********************************************************

# region Урок: ************************************************************


# максимальное количество идущих подряд символов, среди которых символ T встречается ровно 3 раз.
'''
s = 'xxxxxxTxxxxTxxxxxxxxxTxxxxTxxxxxxxTxxxTxxxxxxxxxxx'
# ['xxxxxx', 'xxxx', 'xxxxxxxxx', 'xxxx', 'xxxxxxx', 'xxx', 'xxxxxxxxxxx']
# xxxxxxTxxxxTxxxxxxxxxTxxxx 26
# xxxxTxxxxxxxxxTxxxxTxxxxxxx 27
# xxxxxxxxxTxxxxTxxxxxxxTxxx 26
# xxxxTxxxxxxxTxxxTxxxxxxxxxxx 28
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
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



# минимальное количество идущих подряд символов, среди которых символ T встречается ровно 3 раз.
'''
s = 'xxxxxxTxxxxTxxxxxxxxxTxxxxTxxxxxxxTxxxTxxxxxxxxxxx'
# ['xxxxxx', 'xxxx', 'xxxxxxxxx', 'xxxx', 'xxxxxxx', 'xxx', 'xxxxxxxxxxx']
# TxxxxxxTxxxxT 13
# TxxxxTxxxxxxxxxT 16
# TxxxxxxxxxTxxxxT 16
# TxxxxTxxxxxxxT 14
# TxxxxxxxTxxxT 13
# TxxxTxxxxxxxxxxxT 17

s = s.split('T')
mini = 99999999
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)


s = 'xxxxxxTxxxxTxxxxxxxxxTxxxxTxxxxxxxTxxxTxxxxxxxxxxx'
s = s.split('T')
M = []
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    M.append(len(r))
print(min(M))
'''

# Тип 24 №59792
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 100 символов "Т".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
M = []
for i in range(len(s)-98):
    r = 'T' + 'T'.join(s[i:i+99]) + 'T'
    M.append(len(r))
print(min(M)
      '''
# Ответ: 1523

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# todo разобрать Тип 24 №59729 Максим
# Текстовый файл состоит из символов, обозначающих заглавные буквы латинского алфавита.
# Определите минимальное количество идущих подряд символов, среди которых пара символов T встречается ровно 150 раз.

# endregion Разобрать: *************************************************************


# Максим = [2, 6, 5, 8, 9, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке: Разбираем сложные задачи 24 номера + на кол-во и строки

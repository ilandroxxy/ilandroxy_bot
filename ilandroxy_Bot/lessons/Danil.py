# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************


# Тип 24 № 33494
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.
'''
s = open('24.txt').readline()
M = []
for i in range(0, len(s)-1):
    if s[i] == 'E':
        M.append(s[i+1])

print(len(M))
maxi = 0
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for a in alphabet:
    if maxi < M.count(a):
        maxi = M.count(a)
        print(a, maxi)
'''
# Ответ: Y



# Тип 24 № 35482 i
# Текстовый файл содержит строки различной длины. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
mini = 99999
s = open('24.txt').readlines()
r = ''
for x in s:
    if mini > x.count('G'):
        mini = x.count('G')
        r = x
maxi = 0
alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
for a in alphabet:
    if maxi <= r.count(a):
        maxi = r.count(a)
        print(a, maxi)
# Ответ: T



mini = 99999
maxi = 0
alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
s = open('24.txt').readlines()

for x in s:
    if mini > x.count('G'):
        mini = x.count('G')
        for a in alphabet:
            if maxi <= r.count(a):
                maxi = r.count(a)
                print(a, maxi)
'''
# Ответ: T


# Тип 24 № 35998 i
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
s = open('24.txt').readlines()
alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
maxi = -99999
for x in s:
    if x.count('A') < 25:
        for a in alphabet:
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: Ответ: 1004



# endregion Урок: ******************************************************************************


# todo: Данил = [2, 5, 7.1, 8, 9.1, 12, 14+, 15+, 16, 17, 23, 24, 25.2]
# на прошлом уроке: Данил сам прорешал 19-21 номера на одну кучу
# на следующем уроке:

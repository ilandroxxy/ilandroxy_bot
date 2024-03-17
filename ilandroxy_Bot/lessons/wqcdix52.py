# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 24 №27696
# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов L.
# Хотя бы один символ L находится в последовательности.
'''
# Вариант 1
s = open('24.txt').readline()
count = 1  # счетчик промежуточной последовательности
maxi = 0  # счетчик мксимальной последовательности
for i in range(len(s)-1):
    if s[i] == 'L' and s[i+1] == 'L':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)

# Вариант 2
s = open('24.txt').readline()
s = s.replace('D', ' ').replace('R', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 3 - решение через поиск ctrl + F
print(open('24.txt').readline())
print(len('LLLLLLL'))
'''
# Ответ: 7


# Тип 24 №27690
# Текстовый файл состоит не более чем из 106 символов A, B и C.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''
# Ответ: 42


# Тип 24 №58329
# Текстовый файл состоит не более чем из 106 символов арабских цифр (0,1,..., 9).
# Определите максимальное количество идущих подряд цифр,
# среди которых сумма двух идущих подряд чисел больше числа следующего за ними.
'''
s = open('24.txt').readline()
count = 2
maxi = 0
for i in range(len(s)-2):
    if int(s[i]) + int(s[i+1]) > int(s[i+2]):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''

# Тип 24 №39253
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы D.
'''
s = open('24.txt').readline().split('D')
print(s)
maxi = 0
for i in range(len(s)-1):
    maxi = max(maxi, len(s[i] + s[i+1])+1)
print(maxi)
'''
# Ответ: 354

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Артур = [2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

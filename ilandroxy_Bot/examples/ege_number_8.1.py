
# region Тип 8 № 9302

# Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О?
# Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.

# Вариант 1
'''
import itertools
sogl = 'МТР'
glas = 'ЕО'
count = 0
s = itertools.product('МЕТРО', repeat=4)
for temp in s:
    if temp[0] in sogl and temp[3] in glas:
        count += 1
print(count)
'''

# Вариант 2
'''
import itertools
count = 0
s = itertools.product('МЕТРО', repeat=4)
for temp in s:
    if temp[0] in 'МТР' and temp[3] in 'ЕО':
        count += 1
print(count)
'''

# Вариант 3
'''
s = 'МЕТРО'
sogl = 'МТР'
glas = 'ЕО'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if a in sogl and d in glas:
                    count += 1
print(count)
'''

# Вариант 4
'''
s = 'МЕТРО'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                if a in 'МТР' and d in 'ЕО':
                    count += 1
print(count)
'''
# Ответ: 150
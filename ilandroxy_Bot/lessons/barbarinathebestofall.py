# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# № 13298 (Уровень: Средний)
# (М. Паршиков) Алиса составила все пятибуквенные слова из букв П, Р, И, В, Ы, Ч, К, А,
# записала их в алфавитном порядке и пронумеровала.
# После этого Алиса удалила каждое пятое слово и пронумеровала новый список.
# Вот начало списка:
# 1. ААААА
# 2. ААААВ
# 3. ААААИ
# 4. ААААК
# 5. ААААР (удалилось слово ААААП)
#
# Под каким номером идет первое слово, в котором все буквы различные и согласные?
'''
s = sorted('ПРИВЫЧКА')
num = 1
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    k += 1
                    if k == 5:
                        k = 0
                        continue
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):
                        if 'И' not in slovo and 'А' not in slovo and 'Ы' not in slovo:
                            print(num, slovo)
                            exit()
                    num += 1
'''
# Ответ: 4754


# № 13253 (Уровень: Базовый)
# (Я. Рябков) Павел составляет два списка из слов: в одном всевозможные 5-буквенные слова,
# составленные из набора букв К, О, Н, Е, Ц, в другом всевозможные 5-буквенные слова,
# составленные из набора букв Д, Р, А, К, О, Н. Каждая из допустимых букв может
# встречаться в словах любое количество раз или не встречаться совсем.
# Найдите количество слов, которые присутствуют только в одном из списков.
'''
from itertools import *
A = set([''.join(s) for s in product('КОНЕЦ', repeat=5)])
B = set([''.join(s) for s in product('ДРАКОН', repeat=5)])
print(len(A.union(B)) - len(A.intersection(B)))
'''
# Ответ: 10415


# Операции множества set():
'''
print({1, 2, 3, 4}.union({3, 4, 5, 6}))  # {1, 2, 3, 4, 5, 6} - объединение
print({1, 2, 3, 4}.intersection({3, 4, 5, 6}))  # {3, 4} - пересечение
print({1, 2, 3, 4}.difference({3, 4, 5, 6}))  # {1, 2} - разность
'''


# № 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?
'''
from itertools import *
cnt = set()
for s in permutations('ПРОСТО'):  # перестановки букв в слове ПРОСТО
    slovo = ''.join(s)
    if 'ОО' not in slovo:
        cnt.add(slovo)
print(len(cnt))
'''
# 240







# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Варя = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14]
# на следующем уроке:


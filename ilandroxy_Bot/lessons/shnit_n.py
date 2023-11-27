# region Домашка: ************************************************************
'''
from itertools import permutations
for elem in permutations('123'):
    s = ''.join(elem)
    print(s)

from itertools import product
for elem in product('123', repeat=3):
    s = ''.join(elem)
    print(s)
'''

# КЕГЭ № 2573 (Уровень: Средний)
# Дана программа для исполнителя Редактор:
#
# ПОКА нашлось(55555)
#    заменить(55555, 88)
#    заменить(888, 55)
# КОНЕЦ ПОКА
# Известно, что начальная строка состоит более чем из 300 цифр 5
# и не содержит других цифр.
# При какой наименьшей длине исходной строки результат работы этой
# программы будет содержать наибольшее возможное число цифр 5?
'''
def my_prime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


def my_sum(s):
    return sum([int(x) for x in s])


from itertools import product
for n in range(41, 50):
    for elem in product('12', repeat=n):
        s = '0' + ''.join(elem)
        summ_0 = my_sum(s)
        while '01' in s or '02' in s:
            s = s.replace('02', '1110', 1)
            s = s.replace('01', '220', 1)
        if my_prime(my_sum(s)):
            print(summ_0)
'''
# Ответ: 42

# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Тип 8 №15795
# Все четырёхбуквенные слова, составленные из букв П, А, Р, У, С,
# записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Начало списка выглядит так:
# 1.  АААА
# 2.  АААП
# 3.  АААР
# 4.  АААС
# 5.  АААУ
# 6.  ААПА
#
# Под каким номером в списке идёт первое слово, в котором нет буквы А?

'''
s = sorted('ПАРУС')
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if 'А' not in slovo:    # if slovo.count('А') == 0:
                    print(k, slovo)
                    exit()
                k += 1
'''
'''
from itertools import product
k = 1
for elem in product(sorted('ПАРУС'), repeat=4):
    slovo = ''.join(elem)
    if 'А' not in slovo:  # if slovo.count('А') == 0:
        print(k, slovo)
        exit()
    k += 1
'''
# Ответ: 157


# Тип 8 №59713
# Составляют 5-буквенные слова из букв слова ПЯТНИЦА.
# Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я.
# Буквы в слове могут повторяться.
'''
s = 'ПЯТНИЦА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if a != 'Н':
                        if slovo.count('Я') == 1:
                            count += 1
print(count)


from itertools import product
count = 0
for elem in product('ПЯТНИЦА', repeat=5):
    slovo = ''.join(elem)
    if slovo[0] != 'Н':
        if slovo.count('Я') == 1:
            count += 1
print(count)
'''
# Ответ: 5616


# Тип 8 №58237
# Сколько существует различных четырёхзначных чисел, записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?
'''
count = 0
from itertools import permutations
for elem in permutations('0123456', 4):
    if list(elem) == sorted(elem, reverse=True):
        count += 1
print(count)
'''
# Ответ: 35

# todo продолжить рассматривать 8-ые номера и 14-ый номер

# endregion Урок: ************************************************************


# Никита = [8.1, 12.1, 14.1]
# КЕГЭ = []
# на следующем уроке:

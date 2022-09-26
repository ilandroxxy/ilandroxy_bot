# Разбор домашки 26.09


# Тип 5 № 18582 Добавить в вариант
'''
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1.Строится двоичная запись числа N без ведущих нулей.
#
# 2.Если в полученной записи единиц больше, чем нулей, то справа приписывается единица. Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
#
# 3.Полученное число переводится в десятичную запись и выводится на экран.

# Какое наименьшее число, превышающее 100, может получиться в результате работы автомата?\
M = []
for n in range(1, 100):
    temp = n

    N = []
    while n > 0:
        N.append(n % 2)  # 1. Строится двоичная запись числа N без ведущих нулей.
        n //= 2
    N.reverse()

    while N[0] == 0:  # условие интересное и правильное, но можно и без него
       del N[0]

    if N.count(1) > N.count(0):  # 2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица.
        N.append(1)
    if N.count(0) >= N.count(1):  # Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
        N.append(0)

    r = 0
    N.reverse()
    for i in range(len(N)):  # 3. Полученное число переводится в десятичную запись и выводится на экран.
        r += N[i] * 2 ** i
    if r > 100:  # Какое наименьшее число, превышающее 100, может получиться в результате работы автомата?\
        M.append(r)
print(min(M))
'''



# n, l = int(input()), []
'''
n = int(input('N: '))
L = []
for i in range(0, n):
  L.append(int(input('Введите числа в список:')))
print(L)

for a in L:
  if a != min(L) and a != max(L):
    print(a)
'''

'''
n = int(input())
L = []
for i in range(0, n):
  L.append(int(input()))
#print(L)

"""
M = []
for a in L:
  if a != min(L) and a != max(L):
    M.append(a)
print(a)
"""

for j in range(0, len(L)):
    if L[j] == min(L):
        del L[j]
        break

for j in range(0, len(L)):
    if L[j] == max(L):
        del L[j]
        break

for a in L:
    print(a)
'''

'''
weather = 'облачно'
temperature = 24
# Привет, сегодня облачно, но жарко, температура 24
print('Привет, сегодня', weather, ', но жарко, температура', temperature)
print('Привет, сегодня ' + weather + ', но жарко, температура ' + str(temperature))
print('Привет, сегодня {}, но жарко, температура {}'.format(weather, temperature))
print('Привет, сегодня %s, но жарко, температура %d'%(weather, temperature))
print(f'Привет, сегодня {weather}, но жарко, температура {temperature}')
'''


# Тип 8 № 15105
'''
# Все четырёхбуквенные слова, составленные из букв П, А, Р, У, С, записаны в алфавитном порядке и пронумерованы,
# начиная с 1. Начало списка выглядит так:
#
# 1.АААА
# 2.АААП
# 3.АААР
# 4.АААС
# 5.АААУ
# 6.ААПА
#
# Под каким номером в списке идёт первое слово, которое начинается с буквы Р?

s = 'АПРСУ'

count = 1
for a in s:  # 5
    for b in s:  # 5 * 5 = 25
        for c in s:  # 25 * 5 = 125
            for d in s:  # 125 * 5 = 625
                temp = a + b + c + d
                if a == 'Р':
                    print(count, temp)
                # if temp == 'РААА':
                #
                count += 1
'''
# Ответ: 251



# Тип 8 № 13540
'''
# Пётр составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Пётр использует все пятибуквенные слова в алфавите {A, B, C, D, E, F}, удовлетворяющие
# такому условию: кодовое слово не может (начинаться с буквы F и заканчиваться буквой A).
# Сколько различных кодовых слов может использовать Пётр?

# 1 вариант
s = 'ABCDEF'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    # temp = a + b + c + d + e
                    if a != 'F' and e != 'A':
                        count += 1
print(count)  # 5400

# 2 вариант
s = 'ABCDEF'
count = 0
for a in 'ABCDE':
    for b in s:
        for c in s:
            for d in s:
                for e in 'BCDEF':
                    count += 1
print(count)  # 5400
'''
# Ответ: 5400



# Тип 8 № 27295
'''
# Света составляет 5-буквенные коды из букв С, В, Е, Т, А.
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные.
# Сколько различных кодов может составить Света?

s = 'СВЕТА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if 'С' in temp and 'В' in temp and 'Е' in temp and 'Т' in temp and 'А' in temp:
                        if 'АА' not in temp and 'ЕЕ' not in temp and 'АЕ' not in temp and 'ЕА' not in temp:
                            count += 1
print(count)
'''
# Ответ: 72



# Тип 8 № 47005
'''
# Светлана составляет коды из букв слова ПАРАБОЛА.
# Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
# Сколько кодов может составить Светлана?

s = 'ПАРАБОЛА'
s1 = 'ПРБЛ'
s2 = 'АО'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        for g in s1:
                            for h in s2:
                                temp = a + b + c + d + e + f + g + h
                                if temp.count('А') == 3 and temp.count('О') == 1 and temp.count('П') == 1 and temp.count('Л') == 1 and temp.count('Р') == 1 and temp.count('Б') == 1:
                                    print(temp)
                                    count += 1
print(count * 2)
'''
# Ответ: 192













# region Домашка: ************************************************************



# № 6040 ФИПИ 04.02.23 (Уровень: Базовый)
# Определите количество шестизначных чисел, записанных в семеричной системе счисления,
# в записи которых ровно одна цифра 6, при этом чётные и нечётные цифры чередуются.
'''
from itertools import product
nums = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
s = '0123456'
for i in product(nums[:7], repeat=2):
    pair = ''.join(i)
    if (pair[0] in '0246' and pair[1] in '0246') or (pair[0] in '1357' and pair[1] in '1357'):
        M.append(pair)

counter = 0
for i in product(nums[:7], repeat=6):
    temp = ''.join(i)
    if temp.count('6') == 1 and temp[0] != '0':
        if all(x not in temp for x in M):
            counter += 1
print(counter)
'''
# 1296


# № 6018 ФИПИ 03.02.23 (Уровень: Базовый)
# При регистрации в компьютерной системе каждому объекту присваивается идентификатор,
# состоящий из 35 символов и содержащий только десятичные цифры и символы из
# 2050-символьного специального алфавита. В базе данных для хранения каждого идентификатора
# отведено одинаковое и минимально возможное целое число байт.
# При этом используется посимвольное кодирование идентификаторов, все символы кодируются
# одинаковым и минимально возможным количеством бит.
#
# Определите объём памяти (в Кбайт), необходимый для хранения 32 768 идентификаторов.
# В ответе запишите только целое число – количество Кбайт.
'''
from math import log, ceil
K = 35
i = ceil(log(2050, 2))
I = K * i   # 420
byte = ceil(I / 8)
print((byte * 32768) / (2**10))
'''
# Показать ответ: 1696

# № 6054 ФИПИ 04.02.23 (Уровень: Базовый)
# Текстовый файл состоит из символов A, B, C.
#
# Определите максимальную длину подпоследовательности подряд идущих символов, состоящую из троек вида
# согласная + согласная + гласная
'''
s = open('24.txt').readline()
s = s.replace('C', 'B')
s = s.replace('BBA', '***')
s = s.replace('A', 'B').replace('B', ' ')
s = [len(i) for i in s.split()]
print(max(s))
'''
# Ответ: 6





# endregion Урок: ************************************************************


# todo:   Василий    = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# todo: Василий КЕГЭ = [25]
# на прошлом уроке:  Разбирали домашку и вопросы по ней: 17, 14 номера. Немного поговорили про 25-ые.
# на следующем уроке:

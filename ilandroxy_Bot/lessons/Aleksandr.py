# region Домашка:  ******************************************************************************



# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

'''
s = '372yrf478t376y4r9348hf398hj4f'
print(sum([int(i) for i in s if i.isdigit()]))
'''


# № 5669 Вариант 09.01.23 (Уровень: Средний)
'''
for x in '0123456789abcdef':
    p = int('8569' + x, 16) + int('12' + x + '48', 16)
    M = []
    while p > 0:
        M.append(p % 8)
        p //= 8
    M.reverse()
    chet = [i for i in M if i % 2 == 0]
    if len(chet) <= 2:
        print(M)

for x in '0123456789abcdef':
    p = int(f'8569{x}', 16) + int(f'12{x}48', 16)
    s = oct(p)[2:]
    chet = [int(i) for i in s if int(i) % 2 == 0]
    if len(chet) <= 2:
        print(s)
'''
# 2275735

# записанного в 8-ричной системе счисления, не встречается более двух чётных цифр.



s = open('24.txt').readline()
print(s)
print(len('DADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
print(len('DDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
print(len('ADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))

# Ответ: 99

# endregion Урок:  ******************************************************************************


# todo: Александр = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24+, 25]
# todo: Никита КЕГЭ = [5, 8, 9, 12, 14, 15, 25]
# на прошлом уроке: Разобрали сложные задачи с домашки: 14, 24 повторили с самопрорешиванием
# на следующем уроке:
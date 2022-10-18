

# region Тип 12 № 19063
'''
# Какая строка получится в результате применения приведённой
# ниже программы к строке, состоящей из 70 идущих подряд цифр 8?
# В ответе запишите полученную строку.
# ПОКА нашлось (2222) ИЛИ нашлось (8888)
    # ЕСЛИ нашлось (2222)
    #   ТО заменить (2222, 88)
    # ИНАЧЕ заменить (8888, 22)
# КОНЕЦ ПОКА

s = '8' * 70
# print(len(s), s)
while '2222' in s or '8888' in s:
    if '2222' in s:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)
print(s)
'''
# Ответ: 22
# endregion Тип 12 № 19063


# region Тип 12 № 47009
'''
# Дана программа для редактора:
#
# НАЧАЛО
#   ПОКА НЕ нашлось (00)
#       заменить (01, 210)
#       заменить (02, 3101)
#       заменить (03, 2012)
#   КОНЕЦ ПОКА
# КОНЕЦ
#
# Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними
# содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка,
# содержащая 61 единицу, 50 двоек и 18 троек.
# Сколько цифр было в исходной строке?

for a in range(0, 100):
    for b in range(0, 50):
        for c in range(0, 20):
            s = '0' + '1' * a + '2' * b + '3' * c + '0'
            temp = s
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18: #  содержащая 61 единицу, 50 двоек и 18 троек.
                print(len(temp), s)
'''
# Ответ: 38
# endregion Тип 12 № 47009


# region Тип 12 № 15854
'''
# Определите количество нулей в строке, получившейся в результате применения
# приведённой ниже программы к входной строке, состоящей из единицы, за которой следуют 80 нулей подряд.
# В ответе запишите только количество нулей в получившейся строке.
#
# НАЧАЛО
# ПОКА нашлось (10) ИЛИ нашлось (1)
#     ЕСЛИ нашлось (10)
#         ТО заменить (10, 001)
#     ИНАЧЕ
#         ЕСЛИ нашлось(1)
#              ТО заменить (1, 000)
#         КОНЕЦ ЕСЛИ
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
s = '1' + '0' * 80
# print(s, len(s))
while '10' in s or '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    elif '1' in s:  #ИНАЧЕ ЕСЛИ нашлось(1)
        s = s.replace('1', '000', 1)
print(s.count('0'))
'''
# Ответ: 163
# endregion Тип 12 № 15854


# region Тип 12 № 27299
'''
# Дана программа для Редактора:
# НАЧАЛО
# ПОКА нашлось (111)
#     заменить (111, 2)
#     заменить (222, 11)
# КОНЕЦ ПОКА
# КОНЕЦ
# К исходной строке, содержащей более 60 единиц и не содержащей других символов,
# применили приведённую выше программу. В результате получилась строка 221.
# Какое наименьшее количество единиц могло быть в исходной строке?
for i in range(1, 1000):
    s = (i + 60) * '1'
    temp = s
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
    if s == '221':
        print(temp.count('1'), s)
'''
# Ответ: 63
# endregion Тип 12 № 27299


# region Тип 12 № 33757
'''
# Дана программа для редактора:
#
#
# НАЧАЛО
#     ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#         заменить (01, 30)
#         заменить (02, 101)
#         заменить (03, 202)
#     КОНЕЦ ПОКА
# КОНЕЦ
#
# Известно, что исходная строка начиналась с нуля, а далее содержала только единицы,
# двойки и тройки. После выполнения данной программы получилась строка,
# содержащая 20 единиц, 10 двоек и 70 троек.
# Сколько единиц было в исходной строке?
for a in range(0, 60):
    for b in range(0, 50):
        for c in range(0, 80):
            s = '0' + '1' * a + '2' * b + '3' * c
            temp = s
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 20 and s.count('2') == 10 and s.count('3') == 70:
                print(temp.count('1'), s)
'''
# Ответ: 50
# endregion Тип 12 № 33757
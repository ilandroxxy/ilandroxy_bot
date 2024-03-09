# region Домашка: ******************************************************************


# Дана программа для Редактора:
#   ПОКА нашлось (12) ИЛИ нашлось (322) ИЛИ нашлось (222)
#     ЕСЛИ нашлось (12)
#       ТО заменить (12, 2)
#     ЕСЛИ нашлось (322)
#       ТО заменить (322, 21)
#     ЕСЛИ нашлось (222)
#       ТО заменить (222, 3)

# На вход приведённой выше программе поступает строка, начинающаяся с цифры «1»,
# а затем содержащая n цифр «2» (3 < n < 10 000).
# Определите наибольшее возможное значение суммы числовых значений цифр в строке,
# которая может быть результатом выполнения программы.
'''
R = []
for n in range(4, 10000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:  # ЕСЛИ нашлось (1122)
            s = s.replace('222', '3', 1)

    # print(s, [int(x) for x in s])
    R.append(sum([int(x) for x in s]))

print(max(R))
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************



# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Тип 12 №48433 Тимур
#     ПОКА НЕ нашлось (00)
#         заменить (011, 20)
#         заменить (022, 10)
#         заменить (01, 220)
#         заменить (02, 110)

# Известно, что исходная строка A содержала ровно два нуля — на первом
# и на последнем месте, а также поровну единиц и двоек.
# После выполнения данной программы получилась строка B,
# содержащая 40 единиц и больше 50 двоек.
# Какое наименьшее количество двоек может быть в строке B?
'''
for n in range(0, 2000):
    s = '0' + '1' * n + '2' * n + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
    if s.count('1') == 40 and s.count('2') > 50:
        print(s)
'''

# endregion Разобрать: *************************************************************


# Тимур = [2.1, 5.1, 6.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:

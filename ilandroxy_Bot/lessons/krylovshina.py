# region Домашка: ******************************************************************

# КЕГЭ № 376 (Уровень: Базовый)
#
# НАЧАЛО
#    ПОКА нашлось (11)
#       заменить (112, 4)
#       заменить (113, 2)
#       заменить (42, 3)
#       заменить (43, 1)
#    КОНЕЦ ПОКА
# КОНЕЦ

# Какая строка получится в результате применения приведённой программы
# к строке вида 1…13…32…2 (170 единиц, 100 троек и 7 двоек)?
'''
s = '1' * 170 + '3' * 100 + '2' * 7
while '11' in s:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)
print(s)
'''
# Ответ: 22


# КЕГЭ № 1751 Danov2102 (Уровень: Сложный) (А. Богданов)
# Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
#
# ПОКА нашлось(10) ИЛИ нашлось(20)
#    ЕСЛИ нашлось(20)
#       ТО заменить(20,00)
#       ИНАЧЕ заменить(10,200)
#    КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

# Определите максимально возможное количество цифр 0,
# которое может получиться в результате применения представленного ниже алгоритма к строке,
# состоящей из 19 цифр 0, 13 цифр 1 и 17 цифр 2, идущих в произвольном порядке.
'''
s = '2' * 17 + '1' * 13 + '0' * 19

while '10' in s or '20' in s:
    if '20' in s:
        s = s.replace('20', '00', 1)
    else:
        s = s.replace('10', '200', 1)

print(s.count('0'))
'''
# Ответ: 62

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# todo Разобрать номера: 1-7, 10-14 (Письменные задачи: 1, 4, 7, 11, 13; Excel: 3, 10; Python: 2, 5, 12, 14)


# Единицы измерения информации
# Компьютеры бинарные - то есть используют для работы только 0 и 1

# минимальная единица измерения: 1 бит
# 1 байт = 8 бит = 2**3 бит
# 1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
# 1 Мбайт = 1024 Кбайт = 2**10 Кбайт = 2**20 байт = 2**23 бит
# 1 Гбайт = 1024 Мбайт = 2**10 Мбайт = 2**30 байт = 2**33 бит


# endregion Урок: ******************************************************************


# todo: Анастасия = [1.1, 2.1, 4.1, 7.1, 11.1, 12.1, 14.1]
# todo:  КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке: На след. уроке продолжаем 13; Excel: 3, 10

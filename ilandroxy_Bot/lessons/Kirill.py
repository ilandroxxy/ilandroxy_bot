# region Домашка:  **************************************************

# Тип 24 № 45258 Добавить в вариантСообщить об ошибкеi
# Текстовый файл состоит из символов A, B и C.
#
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
#
# Искомая подпоследовательность должна состоять только из пар AB,
# или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.
#
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.replace('AB', '*').replace('CB', '*')
s = s.replace('A', ' ').replace('C', ' ').replace('B', ' ')
R = [len(i) for i in s.split()]
print(max(R))
'''
# Ответ: 65


# № 5677 Вариант 09.01.23 (Уровень: Средний)
# (А. Игнатюк) В текстовом файле дана последовательность латинских букв.
# Необходимо найти в этой последовательности самую длинную подстроку, состоящую из комбинации DAD,
# при этом первый и последний элементы могут быть неполными.
'''
s = open('24.txt').readline()
print(s)
print(len('DADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
print(len('DDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
'''
'''
s = open('24.txt').readline()
for n in range(1, 1000):
    if 'DAD' * n not in s:
        print(3*(n - 1))
        break
'''
# Ответ: 99

# endregion Домашка: **************************************************


# region Урок:  **************************************************



# endregion Урок:  **************************************************

import useful
print(useful.who_is_name())

# todo: Кирилл = [1, 2, 3, 4, 5, 8, 9, 12, 13, 14+, 15, 16, 17, 19-21, 22, 23, 24, 25], на следующем уроке:
# на прошлом уроке:
# на следующем уроке:



# Тип 6 № 33751
'''
# Определите, при каком наименьшем введённом значении переменной s программа выведет число 66.
# Для Вашего удобства программа представлена на четырёх языках программирования.

for i in range(7, 1000):
    s = i
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    if n == 66:
        print(i, n)
'''
# Ответ 20


# Тип 22 № 17338
'''
# Ниже на пяти языках программирования записан алгоритм, который вводит натуральное число x,
# выполняет преобразования, а затем выводит одно число.
# Укажите наименьшее возможное значение x, при вводе которого алгоритм выведет число 7.

for i in range(1, 1000):
    x = i
    a=0
    b=10
    while x > 0:
        d = x % 6
        if d > a:
            a = d
        if d < b:
            b = d
        x = x // 6
    if a+b == 7:
        print(i, a+b)
'''
# Ответ 17


# Тип 12 № 18495
# Какая строка получится в результате применения приведённой ниже программы к строке вида 1…12…2 (40 единиц и 40 двоек)?
#
# НАЧАЛО
# ПОКА нашлось (111)
#     заменить (111, 2)
#     заменить (222, 1)
# КОНЕЦ ПОКА
# КОНЕЦ

s = '1' * 40 + '2' * 40
print(s)

while '111' in s:   # ПОКА нашлось (111)
    s = s.replace('111', '2', 1)
    s = s.replace('222', '1', 1)
print(s)

# Ответ: 2112
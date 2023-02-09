
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************


# s = '11111111111'
# s = s[:4] + '****' + s[8:]
# # s = s.replace('1', '*', 4)
# print(s)
#
# x = '5,8'
# x = float(x.replace(',', '.'))
# print(x)


# Тип 12 № 14229
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 85 идущих подряд цифр 9?
# В ответе запишите полученную строку.
#
# ПОКА нашлось (666) ИЛИ нашлось (999)
    # ЕСЛИ нашлось (666)
        # ТО заменить (666, 9)
    # ИНАЧЕ заменить (999, 6)
    # КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
'''
s = '9' * 85
while '666' in s or '999' in s:
    if '666' in s:
        s = s.replace('666', '9', 1)
    else:
        s = s.replace('999', '6', 1)
print(s)
'''
# Ответ: 699


# Тип 12 № 35901
# Дана программа для редактора:
#     ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#         заменить (01, 2302)
#         заменить (02, 10)
#         заменить (03, 201)
#     КОНЕЦ ПОКА

# Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 50 единиц, 12 двоек и 7 троек.
# Сколько единиц было в исходной строке?
'''
for x in range(0, 50):
    for y in range(0, 50):
        for z in range(0, 50):
            s = '0' + '1' * x + '2' * y + '3' * z

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)

            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(x)
                exit()
  '''
# Ответ: 2



# Тип 12 № 27240
# Дана программа для Редактора:
#
# ПОКА нашлось (11)
#     ЕСЛИ нашлось (112)
#         ТО заменить (112, 6)
#         ИНАЧЕ заменить (11, 3)
# КОНЕЦ ПОКА
#
# Исходная строка содержит десять единиц и три двойки, других цифр нет, точный порядок расположения единиц и двоек неизвестен.
# Какую наибольшую сумму цифр может иметь строка, которая получится после выполнения программы?
'''
import itertools
maxi = -99999  # наибольшую сумму цифр
for s in itertools.product('12', repeat=13):
    s = ''.join(s)
    if s.count('1') == 10 and s.count('2') == 3:
        while '11' in s:
            if '112' in s:
                s = s.replace('112', '6', 1)
            else:
                s = s.replace('11', '3', 1)
        maxi = max(maxi, sum([int(i) for i in s]))
        # if maxi < sum([int(i) for i in s]):
        #     maxi = sum([int(i) for i in s])
print(maxi)


import itertools
L = []
for s in itertools.product('12', repeat=13):
    s = ''.join(s)
    if s.count('1') == 10 and s.count('2') == 3:
        while '11' in s:
            if '112' in s:
                s = s.replace('112', '6', 1)
            else:
                s = s.replace('11', '3', 1)
        L.append(sum([int(i) for i in s]))
print(max(L))
'''
# Ответ: 24


# Тип 12 № 47216
# Дана программа для Редактора:
# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>0)
#         ТО заменить (>0, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
#
# На вход приведённой выше программе поступает строка, начинающаяся с символа «>»,
# а затем содержащая 39 цифр «0», n цифр «1» и 39 цифр «2», расположенных в произвольном порядке.
#
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки, получившейся в результате выполнения программы, является простым числом.

'''
def prime(x):
    # for j in range(2, x):
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    summ = sum([int(i) for i in s[:-1]])
    if prime(summ) == True:
        print(n)
        break
'''
# Ответ: 5




# Теория для 25 номера
'''
def D1(x):
    M = []
    for j in range(2, x):
        if x % j == 0:
            M.append(j)
    return M

def D2(x):
    M = set()
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            M.add(j)
            M.add(x // j)
    return sorted(M)



print(D2(1_000_000_000_000))
'''


def prime(x: int) -> bool:  # анотация типов данных
    '''
Функция для проверки числа на простоту
:param x: Принимает число на проверку
:return: Возвращает Истину, если число простое
    '''
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


print(f'Документация к функции len(): {len.__doc__}')
M = []
print(f'Документация к методу .append(): {M.append.__doc__}')

print(f'\nДокументация к методу prime(): {prime.__doc__}')

# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 12, 14]
# на прошлом уроке: Разобрали 12 номера всех типов, начали говорить про функции
# на следующем уроке: Разбираем функции и задачи 16, 23

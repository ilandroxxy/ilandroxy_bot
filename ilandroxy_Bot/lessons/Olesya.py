# region Домашка:  **************************************************



# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Тип 8 № 16813
'''
# Левий составляет 5-буквенные коды из букв Л, Е, В, И, Й.
# Каждую букву нужно использовать ровно 1 раз, при этом код не может начинаться с буквы Й и не может содержать сочетания ЕИ.
# Сколько различных кодов может составить Левий?

s = 'ЛЕВИЙ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if a != 'Й' and "ЕИ" not in temp:
                        M = [i for i in temp]
                        if len(set(M)) == 5:
                            print(set(M))
                            count += 1
print(count)
'''
# Ответ: 78


# Тип 12 № 9365
'''
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 68 идущих подряд цифр 8?
# В ответе запишите полученную строку.
#
#  ПОКА нашлось (222) ИЛИ нашлось (888)
#     ЕСЛИ нашлось (222)
#         ТО заменить (222, 8)
#         ИНАЧЕ заменить (888, 2)
#     КОНЕЦ ЕСЛИ
#  КОНЕЦ ПОКА

s = '8' * 68

while '222' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s)
'''
# Ответ: 28


# Тип 14 № 18497
'''
# Значение выражения 6*343*5 + 5*49*7 − 50 записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?

x = 6*343*5 + 5*49*7 - 50
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M, M.count(6))
'''
# Ответ: 3


# Тип 16 № 4646
'''
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
#
# F(1) = 1
# F(2) = 3
# F(n) = F(n−1) * F(n−2) + (n−2), при n > 2
#
# Чему равно значение функции F(5)?
# В ответе запишите только натуральное число.

def F(n):
    if n > 2:
        return F(n-1) * F(n-2) + (n-2)
    if n == 1:
        return 1
    if n == 2:
        return 3

print(F(5))
'''
# Ответ: 59












# endregion Урок:  **************************************************


# todo: Олеся = [], на следующем уроке: Теория на типы данных
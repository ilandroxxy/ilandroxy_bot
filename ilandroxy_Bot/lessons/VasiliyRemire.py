
# region Домашка: ******************************************************************

# № 7083 OpenFIPI (Уровень: Базовый)
'''
s = "1" + "0" * 55

while "1" in s:
    if "10" in s:
        s = s.replace("10", "001", 1)
    else:
        s = s.replace("1", "00", 1)

print(s.count('0'))
'''
# Ответ: 112

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 8952 Джобс 02.06.2023 (Уровень: Базовый) (Е. Джобс)
#
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14&5 = 11102&01012 = 01002 = 4.
# Найдите минимальное значение А, при котором значение выражения
#
# (x & 103 = 0) ∧ (x & 94 ≠ 0) → (x & A ≠ 0)
#
# тождественно истинно, то есть принимает значение 1 при любом натуральном значении х.

def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)


print(min([A for A in range(0, 1000) if all(F(x, A) for x in range(0, 1000))]))

'''
def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)


for A in range(0, 100000):
    if all(F(x, A) for x in range(0, 1000)):
        print(A)
        break
'''

'''
for A in range(0, 100000):
    flag = True
    for x in range(0, 1000):
        F = (((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0))
        if F == False:
            flag = False
            break
    if flag == True:
        print(A)
        break

'''
# endregion Урок: ******************************************************************


# todo: Василий = [2.1, 5.1, 8.1, 12.1, 14.1]
# todo:   КЕГЭ  = []
# на прошлом уроке: Разобрали все 12-ые номера с РЕШУ ЕГЭ от и до.
# на следующем уроке: Повторяем и проверяем домашки по 5, 14, 8, 12 номерам!

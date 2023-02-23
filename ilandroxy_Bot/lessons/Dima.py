
# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 18 № 29666
# Дана последовательность вещественных чисел.
# Из неё необходимо выбрать несколько подряд идущих чисел так,
# чтобы каждое следующее число было меньше предыдущего.
# Какую максимальную сумму могут иметь выбранные числа?
#
# В ответе запишите только целую часть максимально возможной суммы.
# Исходная последовательность записана в виде одного столбца электронной таблицы.
'''
M = [float(i.replace(',', '.')) for i in open('18.txt').readlines()]
maxi_summ = 0
summ = 0
for i in range(0, len(M)-1):
    if M[i+1] < M[i]:
        summ += M[i+1]
        maxi_summ = max(maxi_summ, summ)
    else:
        summ = M[i+1]
print(int(maxi_summ))
'''
# Ответ: 358

# endregion Урок: ******************************************************************************


# todo: Дмитрий = [2, 3, 5, 8, 9.1, 12, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25.2]
# на прошлом уроке: Разбирали 18 номера. Рассмотрели почти все задачи кроми стенок.
# на следующем уроке: На следующем уроке добить 18 номер со стенками + повторение. Письменная часть.
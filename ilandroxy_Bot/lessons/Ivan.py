# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 14 № 48379
# Числа M и N записаны в системе счисления с основанием 9 соответственно.
#
# M = 842x5_9, N = 8x725_9
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита девятеричной системы счисления.
# Определите наименьшее значение натурального числа A, при котором существует такой x, что M + A кратно N.
# for x in '012345678':
'''
for A in range(1, 1000):
    for x in range(0, 8+1):
        M = int(f'842{x}5', 9)  # перевод из 9-ной в 10-ную
        N = int(f'8{x}725', 9)
        if (M + A) % N == 0:
            print(A)
            exit()
'''




# endregion Урок: ******************************************************************************


# todo: Иван = [2, 3, 6, 8, 10, 12, 13, 14+, 15+, 16, 17, 19-21, 23]
# на прошлом уроке: Прорешивали (совместно) 14 и 8 номера
# на следующем уроке:
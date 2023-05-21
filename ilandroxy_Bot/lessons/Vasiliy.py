# region Домашка: ************************************************************

# endregion Домашка: ************************************************************



# region Урок: ************************************************************

#
# № 6903 (Уровень: Базовый)
# (Д. Статный) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
#
# 2. Далее эта запись обрабатывается по следующему правилу:
#
# а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 00,
# а затем два левых разряда заменяются на 11;
#
# б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 11,
# а затем два левых разряда заменяются на 10.
#
# 3. Пункт 2 повторяется ещё раз к записи, полученной после второго пункта.
#
# Полученная таким образом запись является двоичной записью искомого числа R.
# Найдите максимальное число R, которое получается при обработке N, меньших 100. В ответе укажите R.
'''
for n in range(1, 100):
    s = bin(n)[2:]

    for _ in range(2):
        if s.count('1') % 2 == 0:
            s = '11' + s[2:] + '00'
            # s = s.replace(s[2:], '11', 1)
        else:
            s = '10' + s[2:] + '11'

    r = int(s, 2)
    print(r)
'''
# Показать ответ: 1584


# № 6925 (Уровень: Сложный)
# (Д. Статный) Откройте файл электронной таблицы, содержащей в каждой строке шесть неотрицательных целых чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнено только одно из условий:
#
# – в строке только одно число повторяется дважды, а остальные не повторяются;
#
# – в строке среднее арифметическое чётных чисел отличается от среднего арифметического нечётных чисел более чем на 50.
#
# В ответе запишите только число.
#
# *Среднее арифметическое для 0 чисел принять равным нулю.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    flag1 = False
    flag2 = False
    if len(set(M)) == len(M)-1:
        flag1 = True
    chet = [i for i in M if i % 2 == 0]
    nechet = [i for i in M if i % 2 != 0]
    try:
        if abs((sum(chet) / len(chet)) - (sum(nechet) / len(nechet))) > 50:
            flag2 = True
    except ZeroDivisionError:
        if (sum(M) / len(M)) > 50:
            flag2 = True

    if flag1 + flag2 == 1:
        count += 1
print(count)
'''
# Ответ: 862


# endregion Урок: ************************************************************




# todo:   Василий    = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# todo: Василий КЕГЭ = [25]
# на прошлом уроке: Посмотрели на домашку: 7, 26 номера. И прорешивали сложные 24 номера с КЕГЭ
# на следующем уроке:

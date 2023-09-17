

# Тип 25 №55821
#
# Назовём маской числа последовательность цифр,
# в которой также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# соответствующие маске 12??36*1, делящиеся на 273 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им результаты деления этих чисел на 273.
#
# Количество строк в таблице для ответа избыточно.

from fnmatch import *
for x in range(273, 10**8, 273):
    if fnmatch(str(x), '12??36*1'):
        print(x, x//273)

# 1271361 4657
# 12633621 46277
# 12663651 46387
# 12693681 46497


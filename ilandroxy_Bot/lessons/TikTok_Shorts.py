# РЕШУ ЕГЭ Тип 14 № 8664
# Сколько единиц содержится в двоичной записи
# значения выражения: 8**2020 + 4**2017 + 26 - 1?
'''
x = 8**2020 + 4**2017 + 26 - 1
s = bin(x)[2:]
print(s.count('1'))
'''

s = '47236ergh472h36'
summ = 0
for x in s:
    if x.isdigit():
        summ += int(x)
print(summ)

summ = sum([int(x) for x in '47236ergh472h36' if x.isdigit()])
print(summ)
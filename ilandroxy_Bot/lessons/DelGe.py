
# region Домашка: ************************************************************
'''
s = input()
print(f"Символ + встречается {s.count('+')} раз")
print(f"Символ * встречается {s.count('*')} раз")
'''

# На  вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.

num = input()  # str
summ = 0
for i in range(len(num)):  # 0, 1, 2, 3
    summ += int(num[i])
print(summ)


print(sum([int(x) for x in input()]))

n = int(input())
if (n%4 == 0 and n%100 == 0) or (n%400 == 0):
    print("Да")
else:
    print('Нет')


# endregion Домашка: ************************************************************


# region Урок: ************************************************************


# endregion Урок: ************************************************************


# todo: Евгений = [2.1, 8.1]
# на прошлом уроке:
# на следующем уроке:

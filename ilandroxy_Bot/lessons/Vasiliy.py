# region Домашка: ************************************************************


# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество пар последовательности, в которых только одно число оканчивается на 3,
# а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3.
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

'''
f = open('17.txt')
nums = [int(i) for i in f]
max_square_sum = max_square = counter = 0
for i in range(len(nums)):
    if nums[i] % 10 == 3 and max_square < nums[i] ** 2:
        max_square = nums[i] ** 2
print(max_square)  # 18515809 - 99460729
for i in range(len(nums) - 1):
    #if ((nums[i] % 10 == 3 and nums[i + 1] % 10 != 3) or (nums[i] % 10 != 3 and nums[i + 1] % 10 == 3)):
    # if (abs(nums[i]) % 10 == 3 and abs(nums[i + 1]) % 10 != 3) or abs((nums[i]) % 10 != 3 and abs(nums[i + 1]) % 10 == 3):
    if (str(nums[i])[-1] == "3" and str(nums[i + 1])[-1] != "3") or (str(nums[i])[-1] != "3" and str(nums[i + 1])[-1] == "3"):
        if nums[i] ** 2 + nums[i + 1] ** 2 >= max_square:
            print(nums[i], nums[i+1])
            counter += 1
            max_square_sum = max(max_square_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(counter, max_square_sum)
'''


'''
f = open('17.txt')
nums = [int(i) for i in f]
max_square_sum = max_square = counter = 0
for i in range(len(nums)):
    if nums[i] % 10 == 3 and max_square < nums[i]:
        max_square = nums[i]

max_square = max_square ** 2

for i in range(len(nums) - 1):
    # if (nums[i] % 10 == 3 and nums[i + 1] % 10 != 3) or (nums[i] % 10 != 3 and nums[i + 1] % 10 == 3):
    if (abs(nums[i]) % 10 == 3 and abs(nums[i + 1]) % 10 != 3) or abs((nums[i]) % 10 != 3 and abs(nums[i + 1]) % 10 == 3):
    # if (str(nums[i])[-1] == "3" and str(nums[i+1])[-1] != "3") or (str(nums[i])[-1] != "3" and str(nums[i+1])[-1] == "3"):
            if (nums[i] ** 2 + nums[i + 1] ** 2) >= max_square:
                counter += 1
                max_square_sum = max(max_square_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(counter, max_square_sum)
'''

'''
A = [int(i) for i in open("17.txt") if int(i) % 10 == 3]
maxi_square = max(A) ** 2

M = [int(i) for i in open("17.txt")]
counter = 0
maxi = 0
for i in range(len(M) - 1):
    if (abs(M[i]) % 10 == 3 and abs(M[i + 1]) % 10 != 3) or abs((M[i]) % 10 != 3 and abs(M[i + 1]) % 10 == 3):
        if M[i] ** 2 + M[i+1] ** 2 >= maxi_square:
            counter += 1
            # print(counter, M[i] ** 2 + M[i + 1] ** 2, maxi_square, M[i] ** 2 + M[i+1] ** 2 >= maxi_square)
            maxi = max(maxi, M[i] ** 2 + M[i+1] ** 2)
print(counter, maxi)
'''
# Ответ: 733 190203010
# Должно быть: 180 190360573


# 24
# Текстовый файл состоит из символов
# A, C, D, F, O.
# Определите максимальное количество идущих подряд пар символов вида
# cогласная + гласная в прилагаемом файле.
# Для выполнения этого задания следует написать программу
'''
f = open('24.txt')
n = f.read()
sogl = 'CDF'
gl = 'AO'
counter = max_counter = 0

for i in range(0, len(n)-1):
    if (n[i] in gl and n[i+1] in sogl) or (n[i] in sogl and n[i+1] in gl):
        counter += 1
        if max_counter < counter:
            max_counter = counter
    else:
        counter = 0

print(max_counter / 2)
'''

'''
n = open('24.txt').readline()
sogl, gl = 'CDF', 'AO'
counter = max_counter = 0

for i in range(0, len(n)-1):
    if (n[i] in gl and n[i+1] in sogl) or (n[i] in sogl and n[i+1] in gl):
        counter += 1
        max_counter = max(max_counter, counter)
    else:
        counter = 0

print(max_counter / 2)
'''
# Ответ: 122
# Должно быть: 95


# endregion Домашка: ************************************************************


# region Урок: ************************************************************



# endregion Урок: ************************************************************


# todo: Василий = [2, 5, 6, 8, 12, 14+, 15, 17, 19, 20, 22, 24]
# на прошлом уроке: Разобрали задачи 17, 24 и 13 из пробника ЕГЭ, научились решать задачки с цикличными путями (13)
# на следующем уроке:  Проговорить 9 Пайтон, 15 перерешать, 25, Эксель

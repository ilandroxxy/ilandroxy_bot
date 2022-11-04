
# region Домашка



# endregion Домашка


# region Урок


# Тип 24 № 27691
'''
# Текстовый файл состоит не более чем из 10**6 символов A, B и C. Определите максимальное количество идущих подряд символов A.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readline()

# s = 'AAAbAAAAABbAAA'
count = 1
MaxCount = 0
for i in range(0, len(s)-1):
    if s[i] == 'A' and s[i+1] == 'A':
        count += 1
        if count > MaxCount:
            MaxCount = count
    else:
        count = 1
print(MaxCount)
'''
# Ответ: 7

f = open('24.txt', 'r')
s = f.readline()

s = 'LDRLDRLDRRRLDR'
count = 2
for i in range(0, len(s)-1):
    if s[i:i+3] == 'LDR':
        count += 1
    elif s[i:i+3] == 'RDL':
        count += 1
    elif s[i:i+3] == 'DLR':
        count += 1
    else:
        pass




# endregion Урок


# todo: Иван = [2, 5, 8, 12, 13, 14, 16, 17], на следующем уроке: добиваем 17, 24 номера, если останутся вопросы











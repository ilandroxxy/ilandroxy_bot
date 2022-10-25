# region Домашка:

# Был запрос на составление табличек от 2 номера.

# endregion Домашка:


# region Урок:
'''
A = {int(i) for i in input().split()}
B = {int(i) for i in input().split()}

if A == B:
    print('YES')
else:
    print('NO')
'''

'''
A = {i for i in input().split()}
B = {i for i in input().split()}

M = A | B
M = sorted(M)
print(*M)
'''

# endregion Урок:



# todo: на следующем уроке коммитим изменения которые сделали на ее компьютере и добавляем кнопки "отмена"
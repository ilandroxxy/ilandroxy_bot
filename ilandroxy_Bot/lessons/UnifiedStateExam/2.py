
# region Тип 2 № 16878
# Операции Математической логики
# отрицание (инверсия): ¬y  <---->  (not(y))
# логическое умножение (конъюнкция):  x ∧ y   <---->  x and y
# логическое сложение (дизъюнкция): x ∨ y  <---->  x or y
# импликация: x → y  <---->  x <= y
# тождество: x ≡ y  <---->  x == y
# Логическая функция F задаётся выражением (x≡¬y)→(z≡(y∨w))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not(y))) <= (z == (y or w))
                if F == False:
                    print(x, y, z, w, F)
''''''
#  Ответ: zwyx
# endregion Тип 2 № 16878

# region Тип 2 № 27287
'''
# Логическая функция F задаётся выражением ((¬z ∨ w) ∧ (¬x ≡ y))→(x∧z).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((not(z)) or w) and ((not(x)) == y)) <= (x and z)
                if not(F):
                    print(x, y, z, w, F)
'''
# Ответ: wzyx
# endregion Тип 2 № 27287
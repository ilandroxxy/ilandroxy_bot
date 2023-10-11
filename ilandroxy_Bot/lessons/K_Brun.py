
# region Домашка: ******************************************************************

# # ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))
# F=((X <= Y) and (y<=w)) or (z==(x or y))
# https://inf-ege.sdamgia.ru/problem?id=15787
#
# # (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))
# F=(x==(w or y)) or ((w<=z) and (y<=w))
# https://inf-ege.sdamgia.ru/problem?id=15814
#
# # (z ∧ y) ∨ ((x → z ) ≡ (y → w))
# F=(z and y) or ((x<=z)==(y<=w))
# https://inf-ege.sdamgia.ru/problem?id=15939
#
# # ((y → x) ≡ (x → w)) ∧ (z ∨ x)
# F= ((y <= x) == (x <= w)) and (z or x)
# https://inf-ege.sdamgia.ru/problem?id=16431
#
# # (x≡¬y)→(z≡(y∨w))
# F=(x == (not y))<=(z == (y or w))
# https://inf-ege.sdamgia.ru/problem?id=16878
#
# # ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z))
# F=((x and  y)or(y and z)) == ((x<=w) and (w<=z))
# https://inf-ege.sdamgia.ru/problem?id=17320
#
# # (z ∧ y) ∨ ((x → z ) ≡ (y → w))
# F=(z and y) or ((x<=z) == (y<=w))
# https://inf-ege.sdamgia.ru/problem?id=15939
#
# # (x ∧ ¬y) ∨ (y ≡ z ) ∨ w
# F=(x and (not y)) or (y == z) or w
# https://inf-ege.sdamgia.ru/problem?id=15970
#
# #  ((x → y) ≡ (y → z)) ∧ (y ∨ w)
# F=((x<=y) == (y<=z)) and (y or w)
# https://inf-ege.sdamgia.ru/problem?id=16377
#
# # ((y → x) ≡ (x → w)) ∧ (z ∨ x)
# F=((y<=x) == (x<=w)) and (z or x)
# https://inf-ege.sdamgia.ru/problem?id=16431


x, y, z, w = 1, 1, 1, 1
# ¬(((x → y ∧ w) ∧ (z → x ∨ y)) ≡ w)
F = not(((x <= (y and w)) and (z <= (x or y))) == w)

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 2 №56502
# Логическая функция F задаётся выражением:
# ((x→y)∨(z→w))∧((z≡y)→(w≡x))
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) or (z <= w)) and ((z == y) <= (w == x))
                if not F:
                    print(x, y, z, w, int(F))

'''

# Тип 2 №51971
# Логическая функция F задаётся выражением:
# (x≡¬y)→((z→¬w)∧(w→y))
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not y)) <= ((z <= (not w)) and (w <= y))
                print(x, y, z, w, int(F))
'''

#  ((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= z) or ((not x) and w)) == (w == z)
                if F:
                    print(x, y, z, w, int(F))

# endregion Урок: ******************************************************************


# todo: Екатерина = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:

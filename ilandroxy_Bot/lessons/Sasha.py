# region Домашка: ************************************************************

# endregion Домашка: ************************************************************


# region Урок: *************************************************************

ST = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
for A in range(1, 10000):
    cnt_NO = 0
    for s, t in ST:
        if (s > 10) or (t > A):
            continue
            # print("YES")
        else:
            cnt_NO += 1
            # print("NO")
    if cnt_NO == 5:
        print(A)

# Ответ: 11



ST = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
cnt = 0
for A in range(1, 10000):
    cnt_NO = 0
    for s, t in ST:
        if (s > 10) or (t > A):
            continue
            # print("YES")
        else:
            cnt_NO += 1
            # print("NO")
    if cnt_NO == 5:
        print(A)
        cnt += 1
print(cnt)




# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Александра = []
# КЕГЭ = []
# на следующем уроке:

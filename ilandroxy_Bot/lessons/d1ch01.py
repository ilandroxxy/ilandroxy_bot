

# КЕГЭ № 7623 Досрочная волна 2023 (Уровень: Базовый)
# A. Прибавить 1
# B. Умножить на 2
# C. Умножить на 3
#
# Сколько существует программ, для которых при исходном числе 2 результатом является число 25,
# и при этом траектория вычислений содержит число 15, но не содержит число 11?

# Вариант 1
def F(a, b):
    if a > b or a == 11:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(2, 15) * F(15, 25))


# Вариант 2
def F(a, b):
    if a >= b or a == 11:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(2, 15) * F(15, 25))

# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:20]:
    if all((int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)) % 15 == 0 for y in alphabet[:20]):
        print((int(f'5{8}4{x}{8}4HJ4', 20) + int(f'4{8}6B{8}{x}1', 20)) )

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Лев = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [22]
# на следующем уроке:

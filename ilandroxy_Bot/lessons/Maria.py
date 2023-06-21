
# region Домашка:  ************************************************************


# endregion Домашка: ************************************************************


# region Урок:  ************************************************************

'''
def troich(x):
    s = ""
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

for n in range(1, 1000):
    s = troich(n)

    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + troich(5 * (n % 3))

    r = int(s, 3)

    if r >= 146:
        print(n)
        break
'''
'''
import turtle as t
t.speed(20)
l = 20
t.left(90)
for i in range(2):
    t.forward(9*l)
    t.right(90)
    t.forward(15*l)
    t.right(90)
t.up()
t.forward(12*l)
t.right(90)
t.down()
for j in range(2):
    t.forward(6*l)
    t.right(90)
    t.forward(12*l)
    t.right(90)
t.color('blue')
t.pu()
for x in range(0, 20):
    for y in range(0, 15):
        t.goto(x*l, y*l)
        t.dot(3, 'red')
t.done()
'''
# ответ: 70


'''
s = sorted('ПЯТНИЦА')
k = 1
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a != 'Ц' and slovo.count('И') == 2:
                            if k % 2 != 0:
                                count += 1
                                print(k, slovo)
                        k += 1
print(count)
'''
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
'''



# endregion Урок: ************************************************************


# todo: Мария = [1, 2, 3, 4, 5, 6, 7.1, 8, 9.1, 10, 12, 13, 14+, 16+, 17, 18, 19-21, 22, 23, 24+, 25.1]
# на прошлом уроке: Повторяли номера 5, 9, 17 с домашней работы
# на следующем уроке:

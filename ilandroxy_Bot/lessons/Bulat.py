# region Домашка: ******************************************************************************

# Тип 23 № 6965
'''
def F(a,b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b) + F(2 * a + 1, b)
print(F(2,16))
'''
#Ответ: 40

# Тип 23 № 5977
'''
def F(a,b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1,b) + F(a + 10, b)
print(F(10,33))
'''
# Ответ: 25


#Тип 6 № 47406
'''
import turtle as t
t.left(90)
t.speed(10)
l = 50
for i in range(4):
    t.forward(12 * l)
    t.right(90)

t.color('blue')
for i in range(3):
    t.forward(12 * l)
    t.right(120)
t.up()
for x in range(0, 13):
    for y in range(0, 13):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''
#Ответ: 65



# Тип 6 № 47391
'''
import turtle as t
t.left(90)
t.speed(10)
l = 30
for i in range(14):
    t.right(60)
    t.forward(2 * l)
    t.right(60)
    t.forward(2 * l)
    t.right(270)
t.color('blue')
t.up()
for x in range(-9, 12):
    for y in range(-15, 3):
        t.goto(x * l, y * l)
        t.dot(3, 'red')
t.done()
'''
# почему то точки не туда ставятся

# endregion Домашка: ******************************************************************************



# region Урок: ******************************************************************************

#

# endregion Урок: ******************************************************************************


# todo: Булат = [2, 8, 10, 12, 14+, 15, 16, 19-21, 25]
# на прошлом уроке: Разбирали теорию игр 19-21 на 1 и 2 кучи
# на следующем уроке:

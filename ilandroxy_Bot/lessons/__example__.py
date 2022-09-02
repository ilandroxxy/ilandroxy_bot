n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())

summ = 0

summ += z
summ += m - x
summ += n - y
summ += k - y
summ += y

print(summ)
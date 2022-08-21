
m = -1000
n = -1000
while m < 1000:
    while n < 1000:
        if m == 0 or n == 0:
            continue
        if (1/m) - (1/n) == 1 and (3/m) + (2/n) == -7:
            print(m, n)
        m += 0.01
        n += 0.01
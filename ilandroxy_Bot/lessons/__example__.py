countdown_str = ''

for i in range(10, -1, -1):
    countdown_str = countdown_str + str(i) + ', '

countdown_str = countdown_str + 'поехали!'

print(countdown_str)
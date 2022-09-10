english = {'рука': 'Саша', 'нога': 'Наташа','хвост': 'tail','питон': 'python', 'бэкенд-разработчик': 'back-end developer',
           683943897:'ghbdtn', 0:'oegjke', 1891281816:"Killo", 811476623:'hard', 1314375732:'Milo' }
for i in english:
    if i == 683943897:
        print(english[i])

if 683943897 in english:
    print("YES")

for i in range(0, 5):
    if english[i] == 683943897:
        print(english[i])


Students = list(english)
print(Students)
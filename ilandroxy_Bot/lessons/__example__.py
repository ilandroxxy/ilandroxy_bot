'''
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',' ']

s = input()
s = s.upper()
print(s)
res = []
for i in s:
    ind = letters.index(i)

    res.append(morse[ind])
R = ' '.join(res)
print(R)
'''

x = True # bool - boolean 
print(type(x))
Text = 'Привет, сегодня солнечно! Как у тебя дела. Ты видел, что у меня есть: игрушки, зажигалки, всякий мусор в голове : )'
SymbolForDelete = '.,!?@*:;)(-+'
ArrayText = [i for i in Text]

for i in range(0, len(ArrayText)):
    if ArrayText[i] in SymbolForDelete:
        ArrayText[i] = ' '

NewText = ''.join(ArrayText)
print(NewText)

RES = [i for i in NewText.split()]
print(RES)
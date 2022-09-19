Text = "Привет, сегодня солнечно! Как у тебя дела. Ты видел, что у меня есть: ; ? ! : + - % :-)"
SymbolForDelete = '.,!?@*:;)(-+%'

ArrayText = [i for i in Text]
print(ArrayText)  # ['П', 'р', 'и', 'в', 'е', 'т', ',', ' ', 'с', 'е', 'г', 'о', 'д', 'н', 'я', ' ', ...]
for i in range(0, len(ArrayText)):
    if ArrayText[i] in SymbolForDelete:
        ArrayText[i] = ' '

NewText = ''.join(ArrayText)
print(NewText)  # Привет  сегодня солнечно  Как у тебя дела  Ты видел  что у меня есть

RES = [i for i in NewText.split()]
print(RES)  # ['Привет', 'сегодня', 'солнечно', 'Как', 'у', 'тебя', 'дела', 'Ты', 'видел', 'что', 'у', 'меня', 'есть']



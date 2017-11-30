word = "достопримечательность"
vowels = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
consonants = "йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"
stopi = len(word)
s =''
i1 = 0
y = 0
for i in range(0, len(word)):
    if word[i] in vowels:
        print(word[i])
        s = word[y:i+1]
        y = i+1
        print(s)






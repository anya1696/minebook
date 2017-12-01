def get_syllables(word):
    vowels1 = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
    consonants1 = "цкнгшщзхфвпрлджчсмтбЦКНГШЩЗХФВПРЛДЖЧСМТБ"
    exclusions1 = "ЙЫЬЪйыъь"
    result = []
    stopi = len(word)
    s1 = ''
    counter = 0
    numnerOfVowels =0
    for c in word:
        if c in vowels1:
            numnerOfVowels +=1
    for i in reversed(range(0,len(word))):
        if  (word[i] in vowels1) and (counter >= numnerOfVowels-1):
            s1 = word[0 : stopi+1]
        elif word[i] in vowels1 :
            if word[i-1] in consonants1:
                s1 = word[i-1:stopi+1]
                stopi = i - 2
            if (word[i-1] in vowels1) or (i == 0) or (word[i-1] in exclusions1):
                s1 = word[i:stopi + 1]
                stopi = i - 1
        if s1 !='':
            result.append(s1)
            counter += 1
        s1 = ''
    return(result[::-1])


#word = raw_input('слово:').decode('utf-8')
word = 'разыскать'
print (get_syllables(word))
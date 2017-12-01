globalLineLenght = 111
numberOfLines = 11
distanceBetweenCharacters = 1
vowels = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
consonants = "йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"
characterWithLength = [["!:;.,", 1 ],["абвгдеёжзийклмопрстуфхчшьэяцАБВГДЕЁЖЗИЙКЛМОПРСТУФХЧШЬЭЯ" , 5],
                       ["нщъюыНЩЪЮЫЦ", 6],["()*", 4], ['+=-?%“',5],[" ",3],
                       ["1234567890", 5]]
inputFileName = "input.txt"
outputFileName = "output.txt"
counter = 0
linesCounter = 0
wordLength = 0
lineLenght = 0
s = ""
s1 = ""
s2 = ""
c2Lenght = 0

def get_syllables(word):
    vowels1 = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
    consonants1 = "цкнгшщзхфвпрлджчсмтбЦКНГШЩЗХФВПРЛДЖЧСМТБ"
    exclusions1 = "ЙЫЬЪйыъь"
    result = []
    stopi = len(word)
    s1 = ''
    counter = 0
    numnerOfVowels = 0
    for c in word:
        if c in vowels1:
            numnerOfVowels += 1
    for i in reversed(range(0, len(word))):
        if (word[i] in vowels1) and (counter >= numnerOfVowels - 1):
            s1 = word[0: stopi + 1]
        elif word[i] in vowels1:
            if word[i - 1] in consonants1:
                s1 = word[i - 1:stopi + 1]
                stopi = i - 2
            if (word[i - 1] in vowels1) or (i == 0) or (word[i - 1] in exclusions1):
                s1 = word[i:stopi + 1]
                stopi = i - 1
        if s1 != '':
            result.append(s1)
            counter += 1
        s1 = ''
    return (result[::-1])


def charLenght(char):
    for group in characterWithLength:
        if char in group[0]:
            return group[1]


with open(inputFileName,'r') as inputFile:
    with open(outputFileName, "w") as outFile:
        for inputLine in inputFile.readlines():
            text = inputLine.split()
            for word in text:
                for character in word:
                    for group in characterWithLength:
                        if character in group[0]:
                            wordLength = wordLength + group[1] + 1
                if lineLenght + charLenght(' ') + wordLength < globalLineLenght:
                    if s == '':
                        s = word
                    else:
                        s = s + ' ' + word
                    lineLenght = lineLenght + charLenght(' ') + wordLength
                    wordLength = 0
                else:
                    temporaryWordLenght = 0
                    syllablesLength = 0
                    syllables = get_syllables(word)
                    for syllable in syllables:
                        for syllableCharacter  in syllable:
                            temporaryWordLenght = temporaryWordLenght + charLenght(syllableCharacter)+1
                            syllablesLength = syllablesLength + charLenght(syllableCharacter)+1

                        if lineLenght + temporaryWordLenght + charLenght("-") < globalLineLenght:
                            s1 = s1 + syllable
                        else:
                            s2 = s2 + syllable
                            c2Lenght = syllablesLength + c2Lenght
                        syllablesLength = 0
                    if s1 != '':
                        if linesCounter < numberOfLines:
                            outFile.write(s + ' ' + s1 + '-' + '\n')
                            linesCounter = linesCounter + 1
                        else:
                            outFile.write(s + ' ' + s1 + '-' + '\n\n')
                            linesCounter = 0
                    else:
                        if linesCounter < numberOfLines:
                            outFile.write(s + '\n')
                            linesCounter = linesCounter + 1
                        else:
                            outFile.write(s + '\n\n')
                            linesCounter = 0

                    s = s2
                    s1 = ''
                    s2 = ''
                    wordLength = 0
                    lineLenght = c2Lenght
                    c2Lenght = 0
            if s !='':
                if linesCounter < numberOfLines:
                    outFile.write(s + '\n')
                    linesCounter = linesCounter + 1
                else:
                    outFile.write(s + '\n\n')
                    linesCounter = 0

import re
globalLineLenght = 111
numberOfLines = 11
#globalLenght = globalLineLenght*numberOfLines
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
    vowels = set(u'аеёиоуыэюя')
    sign_chars = set(u'ъь')
    pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]


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
                    print("word: ", word)
                    print('linesCounter: ', linesCounter)
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
                            print("s1: ", s1)
                            print("syllable: ", syllable)
                        else:
                            s2 = s2 + syllable
                            print("s2: ", s2 )
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
                    # print("c2Lenght: ",c2Lenght)
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

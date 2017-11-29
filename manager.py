globalLineLenght = 111
numberOfLines = 11
#globalLenght = globalLineLenght*numberOfLines
distanceBetweenCharacters = 1
vowels = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"
consonants = "йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"
characterWithLength = [["!:;.,", 1 ],["абвгдеёжзийклмопрстуфхчшьэяцАБВГДЕЁЖЗИЙКЛМОПРСТУФХЧШЬЭЯ" , 5],
                       ["нщъюыНЩЪЮЫЦ", 6],["()*", 4], ['+=-?%“',5],[" ",3]]
inputFileName = "input.txt"
outputFileName = "output.txt"
counter = 0
linesCounter = 0
worlLength = 0
lineLenght = 0
s = ""



with open(inputFileName,'r') as inputFile:
    with open(outputFileName, "w") as outFile:
        for inputLine in inputFile.readlines():
            #text = inputLine.split()
            for character in inputLine:
                for group in characterWithLength:
                    if character in group[0]:
                        if lineLenght + group[1] < globalLineLenght:
                            lineLenght = lineLenght + group[1] + 1
                            s = s + character
                        else:
                            outFile.write(s+"\n")
                            s = character
                            lineLenght = group[1]
                            if linesCounter < numberOfLines:
                                linesCounter = linesCounter +1
                            else:
                                outFile.write("\n\n")
                                linesCounter = 0
            if s !='':
                outFile.write(s + "\n")
                print("worlLength = ", worlLength)
                print("linesCounter = ", linesCounter)




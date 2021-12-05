import math

textFile = open('input.txt', 'r')
textFileLines = textFile.readlines()

numberOfIncreases = 0
previousNumber = int(textFileLines[0]) + int(textFileLines[1]) + int(textFileLines[2])

for lineNumber in range(2, len(textFileLines)-2):
    currentNumber = int(textFileLines[lineNumber]) + int(textFileLines[lineNumber + 1]) + int(textFileLines[lineNumber + 2])
    if int(currentNumber) > int(previousNumber):
        numberOfIncreases += 1

    previousNumber = currentNumber

print(numberOfIncreases)
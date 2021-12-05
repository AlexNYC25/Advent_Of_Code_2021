import math

textFile = open("input.txt", "r")
textFileLines = textFile.readlines()

numberOfIncreases = 0
previousNumber = textFileLines[0]

for lineNumber in range(1, len(textFileLines)):
    if float(textFileLines[lineNumber]) > float(textFileLines[lineNumber - 1]):
        numberOfIncreases += 1
    previousNumber = textFileLines[lineNumber]

print(numberOfIncreases)
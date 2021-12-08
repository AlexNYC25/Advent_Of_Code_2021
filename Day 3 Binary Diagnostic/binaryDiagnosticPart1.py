
from collections import Counter

binaryInputFile = open("input.txt", "r")
binaryInputNumbers = binaryInputFile.read().splitlines()

gammaRate = ""
epsilonRate = ""

for postition in range(len(binaryInputNumbers[0])):

    bit0Count = 0
    bit1Count = 0

    totalString = ""

    for line in binaryInputNumbers:
        totalString += line[postition]

    bitCounter = Counter(totalString)

    bit0Count = bitCounter["0"]
    bit1Count = bitCounter["1"]

    if bit0Count > bit1Count:
        gammaRate += "0"
        epsilonRate += "1"
    else:
        gammaRate += "1"
        epsilonRate += "0"


print(int(gammaRate, 2) * int(epsilonRate, 2))


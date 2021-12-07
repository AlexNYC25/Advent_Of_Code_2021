
commandsFile = open("input.txt", "r")
commandsFileLines = commandsFile.readlines()

horizontal = 0
depth = 0

for line in commandsFileLines:
    commandBreakDown = line.split(' ')
    commandWord = commandBreakDown[0]
    commandValue = commandBreakDown[1]

    if(commandWord == "down"):
        depth += int(commandValue)
    elif(commandWord == "up"):
        depth -= int(commandValue)
    elif(commandWord == "forward"):
        horizontal += int(commandValue)

    
print(horizontal * depth)
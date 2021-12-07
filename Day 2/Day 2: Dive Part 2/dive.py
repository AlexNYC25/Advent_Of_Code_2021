
commandsFile = open("input.txt", "r")
commandsFileLines = commandsFile.readlines()

horizontal = 0
depth = 0
aim = 0

for line in commandsFileLines:
    commandBreakDown = line.split(' ')
    commandWord = commandBreakDown[0]
    commandValue = int(commandBreakDown[1])

    if(commandWord == "down"):
        aim += commandValue
    if(commandWord == "up"):
        aim -= commandValue
    if(commandWord == "forward"):
        horizontal += commandValue
        depth += aim * commandValue

print(horizontal * depth)
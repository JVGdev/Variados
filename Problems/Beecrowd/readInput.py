def readInput(filePath):
    InputFile = open(filePath, "r")

    sizes = []
    boards = []
    turn = 0

    with InputFile as f:
        for i in f.read().split():
            if turn == 0:
                sizes.append(i)
                turn = 1
            else:
                boards.append(i)
                turn = 0

    return sizes, boards

def compareOutput(filePath, gotOutput):
    outputFile = open(filePath, "r")
    with outputFile as f:
        rightOutput = f.read().split()

    for i in range(len(rightOutput)):
        print(f"Your output: {gotOutput[i][0]}", 
                f"The right One: {rightOutput[i]}", 
                f"For the board and size of: {gotOutput[i][1]} -- {gotOutput[i][2]}")

            

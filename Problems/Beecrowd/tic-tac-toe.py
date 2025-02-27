### ---+--- Problably has smthng to do with dividing the boards and comparing the two divided sides, like are the 2 even or not.

from readInput import readInput, compareOutput

sizes, boards = readInput(r"../teste.txt")
#for i in range(len(boards)):
   # print(sizes[i], boards[i])

"""while True:
    try:    
        size = int(input())
        if size == 0:
            break
        board = list(input())

        blanks = len([1 for x in board if x == "." ])
        xs = size - blanks
        if size != xs + blanks:
            break

        if (size %2 == 0 and xs %2 == 0) or (size % 2 != 0 and xs % 2 != 0):
            print("N")
        else:
            print("S")
    except:
        break"""

# Debug version
outputs = []
for i in range(len(sizes)):
    
    size = int(sizes[i])
    if size == 0:
        break
    board = boards[i]

    blanks = len([1 for x in board if x == "." ])
    xs = size - blanks
    if size != xs + blanks:
        break

    if (size %2 == 0 and xs %2 == 0) or (size % 2 != 0 and xs % 2 != 0):
        outputs.append(["N", size, board])
    else:
        outputs.append(["S", size, board])
compareOutput(r"../output.txt", outputs)

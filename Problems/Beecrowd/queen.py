while True:
    #Need to check multiple times for input
    posis = list(input())
    moves = 0

    x1 = int(posis[0])
    y1 = int(posis[2])

    x2 = int(posis[4])
    y2 = int(posis[6])


    if x1 < 1 or y2 < 1 or x1 > 8 or y1 > 8:
        exit()


    if abs(x1 - x2) == abs(y1 - y2) and (x1 != x2 or y1 != y2):
        x1 = x2
        y1 = y2
        moves+=1

    if x1 != x2:
        x1 = x2
        moves+=1

    if y1 != y2:
        y1 = y2
        moves+=1


    print(moves)

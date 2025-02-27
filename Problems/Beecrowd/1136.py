while True:
    n, b = map(int, input().split(" "))
    if n == 0: break
    balls = [int(i) for i in input().split(" ")]
    bingo = []
    already_gone = []
    passed = ""

    for i in balls:
        for a in range(0, len(balls)):
            if abs(i-balls[a]) not in bingo and a not in already_gone:
                bingo.append(abs(i-balls[a]))
        already_gone.append(i)
        
        #balls.remove(i)
    
print(passed)


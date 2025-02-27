for i in range(int(input())):
    n = int(input())
    pos = n//2
    if 0 == pos or pos == n:
        steps = 1
    else:
        if pos < n-pos:
            steps = pos+1
        else: steps = pos
    
    print(steps)
        
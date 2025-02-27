for num in range(int(input())):
    n, k = map(int, input().split(" "))
    
    n = [i for i in range(n)]
    i = 0
    while len(n) > 1:
        i = (i + k-1) % len(n)
        n.pop(i)

    i = (i + k-1) % len(n)
    
    print(f"Case {num+1}: {n[0]+1}")
        
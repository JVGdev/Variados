while True:
    try:
        times = input().split(" ")
    except:
        break
    h1 = int(times[0])
    m1 = int(times[1])
    h2 = int(times[2])
    m2 = int(times[3])

    if h2 == 0 and h2 != h1:
        h2 = 24
    
    if h2 == 0 and h1 == 0 and m2 == 0 and m1 == 0:
        exit()

    # Find a better way to do this shit
    if (h1 == h2 and m1 < m2) or h1 < h2:
        t1 = (h1*60) + m1
        t2 = (h2*60) + m2
    else:
        t1 = (h1*60) + m1
        t2 = ((h2 + 24)*60) + m2

    print(abs(t2 - t1))
while True:
    msg = ""
    try:
        history = input("")
        if history == "": break
        procs = int(input())
        steps = 0
        add = 0

        for i in history:
            if i == "W":
                steps += 1
                add = 0
            elif i == "R" and add == 0:
                steps += 1
                add = 1
            else:
                add += 1
            if add == procs: add = 0
        print(steps)
    except:
        break


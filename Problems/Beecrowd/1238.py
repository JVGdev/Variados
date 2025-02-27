for i in range(int(input())):
    lines = input().split(" ")
    if lines[0].__len__() >= lines[1].__len__():
        top = lines[0].__len__()
    else: top = lines[1].__len__()
    
    for i in range(top):
        try:
            print(f"{lines[0][i]}", end="")
        except: pass
        try:
            print(f"{lines[1][i]}", end="")
        except: pass
    print("")
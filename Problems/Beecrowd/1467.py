while True:
    try:
        a, b, c = map(int, input().split(" "))
        if a == b and a == c:
            print("*")
        elif a == b:
            print("C")
        elif a == c:
            print("B")
        else:
            print("A")
    except:
        break
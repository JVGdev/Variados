import sys

r1, x1, y1, r2, x2, y2 = map(int, input().split(" "))

if x1+r1 <= x2+r2 or y1+r1 <= y2+r2:
    print("MORTO")
else:
    print("RICO")


"""try:
    while True:
        r1, x1, y1, r2, x2, y2 = map(int, input().split(" "))

        if x1+r1 <= x2+r2 or y1+r1 <= y2+r2:
            print("MORTO")
        else:
            print("RICO")
except EOFError:
    exit()"""
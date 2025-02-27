tabs, act = map(int, input().split(" "))
for i in range(act):
    match input():
        case "fechou" if tabs > 0:
            tabs += 1
        case "clicou":
            tabs -= 1
print(tabs)
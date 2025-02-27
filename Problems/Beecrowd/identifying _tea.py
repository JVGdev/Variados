right = int(input())
bets = list(input().split(" "))
g = [int(right == int(x)) for x in bets if int(x) - right == 0]
print(len(g))
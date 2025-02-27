mat = [[0 for i in range(12)] for i in range (12)]
col = int(input())
result = 0
op = input()
for i in range(12):
    for j in range(12):
        act = mat[i][j] = float(input())
        if j == col:
            result += act

if op == "M":
    result = result/12

print(f"{result:.1f}")
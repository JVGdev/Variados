total = 0
for i in range(int(input())):
    id, qnt = input().split(" ")
    total +=  (float(id[3]) + 0.5) * int(qnt)

print(f"{total:.2f}")
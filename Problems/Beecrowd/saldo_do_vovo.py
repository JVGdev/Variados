d, saldo = map(int, input().split(" "))
min = saldo
for i in range(d):
    saldo += int(input())
    if saldo < min:
        min = saldo
print(min)
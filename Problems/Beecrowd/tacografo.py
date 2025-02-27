tot = int(input())
total = 0
for i in range(tot):
    data = input().split()
    total += int(data[0]) * int(data[1])
print(total)
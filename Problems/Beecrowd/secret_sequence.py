size = int(input())
actual, total = 0, 0
for i in range(size):
    if (num:=int(input())) != actual:
        actual = num
        total += 1
        #print(num, (num != actual))

print(total)

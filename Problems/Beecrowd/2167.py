top = int(input())
speeds = list(map(int, input().split(" ")))

printed = False

for i in range(1, top):
    if speeds[i] <  speeds[i-1]:
        print(i+1)
        printed = True
        break 
if not printed:
    print(0)
    

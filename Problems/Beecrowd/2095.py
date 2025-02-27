
#-#-# Time limit #-#-#  

soldiers = int(input())

quadradonia = list(map(int, input().split(" ")))#[int(i) for i in input().split(" ")]
quadradonia.sort(reverse=True)
niglonia = list(map(int, input().split(" ")))#[int(i) for i in input().split(" ")]
niglonia.sort()
wins = 0

#print(quadradonia, niglonia)

i = 0
while niglonia != []:
    if i >= len(niglonia):
        niglonia.pop(0)
        quadradonia.pop(0)
        i = 0
    if niglonia[i] <= quadradonia[0]:
        i+=1
    else:
        niglonia.pop(i)
        quadradonia.pop(0)
        i = 0
        wins += 1
        #print(quadradonia, niglonia)
    #print(i)

    
print(wins)
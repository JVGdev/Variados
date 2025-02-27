# Melhorar circulação da lista #

max = 1
while max != 0:
    max = int(input())
    l = [i for i in range(0, max+1)]
    list1 = [i for i in l]
    for i in range(1, len(list1)+1):
        list1 = [i for i in l]
        a = 1
        while list1.count(13) == 1 and len(list1)>1:
            print(i , a, list1)
            if a >= len(list1):
                a = abs(a-(len(list1))-1)
            if list1[a] != 13:
                list1.pop(a)
                if len(list1) == 1:
                    print(i)
                    break
                a+=i-1
            else:
                break


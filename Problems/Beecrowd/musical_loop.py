while True:
    total = int(input())
    if total == 0: break
    
    sample = [int(i) for i in input().split(" ")]
    sample.insert(0, sample[len(sample)-1])
    sample.append(sample[1])
    peaks = 0

    for i in range(1, total+1):
        if sample[i-1] < sample[i] > sample[i+1] or sample[i-1] > sample[i] < sample[i+1]: peaks +=1
         
    print(peaks)
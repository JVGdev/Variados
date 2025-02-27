cont = 1
while True:
    qnt, max_weight = map(int, input().split(" "))
    if qnt == 0 == max_weight: break
    weights = []
    values = []

    for i in range(qnt):
        w, val = map(int, input().split(" "))
        weights.append(w)
        values.append(val)

    memo = [0 for i in range(max_weight+1)]

    for i in range(max_weight+1):
        for j in range(len(values)):
            if(weights[j] <= i):
                memo[i] = max(memo[i], memo[i - weights[j]] + values[j])

    print("Instancia", cont)
    print(memo[max_weight])
    print("")
    cont+=1
        



